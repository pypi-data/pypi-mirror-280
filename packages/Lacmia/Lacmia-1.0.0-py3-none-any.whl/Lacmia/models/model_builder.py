import copy

import torch
import torch.nn as nn

from transformers import XLMRobertaModel,XLMRobertaConfig
from torch.nn.init import xavier_uniform_

from models.decoder import TransformerDecoder
from models.encoder import Classifier, ExtTransformerEncoder
from models.optimizers import Optimizer
import random

def save_vectors(csv_path, vector, src):
    pass

def select_half_parameters(model: nn.Module) -> nn.Module:
    param_indices = list(range(len(list(model.parameters()))))
    random.shuffle(param_indices)
    num_params_to_train = int(len(param_indices) / 2)

    for i, param in enumerate(model.parameters()):
        if i not in param_indices[:num_params_to_train]:
            param.requires_grad = False
    
    return model

def build_optim(args, model, checkpoint):
    """ Build optimizer """

    if checkpoint is not None:
        optim = checkpoint['optim'][0]
        saved_optimizer_state_dict = optim.optimizer.state_dict()
        optim.optimizer.load_state_dict(saved_optimizer_state_dict)
        if args.visible_gpus != '-1':
            for state in optim.optimizer.state.values():
                for k, v in state.items():
                    if torch.is_tensor(v):
                        state[k] = v.cuda()

        if (optim.method == 'adam') and (len(optim.optimizer.state) < 1):
            raise RuntimeError(
                "Error: loaded Adam optimizer from existing model" +
                " but optimizer state is empty")

    else:
        optim = Optimizer(
            args.optim, args.lr, args.max_grad_norm,
            beta1=args.beta1, beta2=args.beta2,
            decay_method='noam',
            warmup_steps=args.warmup_steps)

    optim.set_parameters(list(model.named_parameters()))


    return optim

def build_optim_bert(args, model, checkpoint):
    """ Build optimizer """

    if checkpoint is not None:
        optim = checkpoint['optims'][0]
        saved_optimizer_state_dict = optim.optimizer.state_dict()
        optim.optimizer.load_state_dict(saved_optimizer_state_dict)
        if args.visible_gpus != '-1':
            for state in optim.optimizer.state.values():
                for k, v in state.items():
                    if torch.is_tensor(v):
                        state[k] = v.cuda()

        if (optim.method == 'adam') and (len(optim.optimizer.state) < 1):
            raise RuntimeError(
                "Error: loaded Adam optimizer from existing model" +
                " but optimizer state is empty")

    else:
        optim = Optimizer(
            args.optim, args.lr_bert, args.max_grad_norm,
            beta1=args.beta1, beta2=args.beta2,
            decay_method='noam',
            warmup_steps=args.warmup_steps_bert)

    params = [(n, p) for n, p in list(model.named_parameters()) if n.startswith('xlm_r.model')]
    optim.set_parameters(params)


    return optim

def build_optim_dec(args, model, checkpoint):
    """ Build optimizer """

    if checkpoint is not None:
        optim = checkpoint['optims'][1]
        saved_optimizer_state_dict = optim.optimizer.state_dict()
        optim.optimizer.load_state_dict(saved_optimizer_state_dict)
        if args.visible_gpus != '-1':
            for state in optim.optimizer.state.values():
                for k, v in state.items():
                    if torch.is_tensor(v):
                        state[k] = v.cuda()

        if (optim.method == 'adam') and (len(optim.optimizer.state) < 1):
            raise RuntimeError(
                "Error: loaded Adam optimizer from existing model" +
                " but optimizer state is empty")

    else:
        optim = Optimizer(
            args.optim, args.lr_dec, args.max_grad_norm,
            beta1=args.beta1, beta2=args.beta2,
            decay_method='noam',
            warmup_steps=args.warmup_steps_dec)

    params = [(n, p) for n, p in list(model.named_parameters()) if not n.startswith('xlm_r.model')]
    print(f'params not xlmr:{params}')
    optim.set_parameters(params)


    return optim


def get_generator(vocab_size, dec_hidden_size, device):
    gen_func = nn.LogSoftmax(dim=-1)
    generator = nn.Sequential(
        nn.Linear(dec_hidden_size, vocab_size),
        gen_func
    )
    generator.to(device)

    return generator


class XLM_R(nn.Module):
    def __init__(self, large, temp_dir, finetune=True, num_languages=3):
        super(XLM_R, self).__init__()
        if large:
            self.model = XLMRobertaModel.from_pretrained("/mnt/raid5/lhy/project/PreSumm_cino/CINO")
        else:
            self.model = XLMRobertaModel.from_pretrained("/mnt/raid5/lhy/project/PreSumm_cino/CINO")
        self.finetune = finetune
        self.num_languages = num_languages
        self.language_embedding = nn.Embedding(num_embeddings=num_languages, embedding_dim=self.model.config.hidden_size)

    def forward(self, x, segs, mask, language_ids=None):
        if self.finetune:
            outputs = self.model(input_ids=x, attention_mask=mask)
        else:
            self.eval()
            with torch.no_grad():
                outputs = self.model(input_ids=x, attention_mask=mask)

        last_hidden_state = outputs.last_hidden_state

        # 如果提供了language_ids，则将语言嵌入添加到最后一层的隐藏状态中
        if language_ids is not None:
            # 获取语言嵌入
            lang_emb = self.language_embedding(language_ids)
            # 扩展语言嵌入以匹配隐藏状态的形状
            lang_emb = lang_emb.unsqueeze(1).expand(-1, x.size(1), -1)
            # 将语言嵌入与隐藏状态相加
            last_hidden_state = last_hidden_state + lang_emb

        return last_hidden_state


class ExtSummarizer(nn.Module):
    def __init__(self, args, device, checkpoint):
        super(ExtSummarizer, self).__init__()
        self.args = args
        self.device = device
        self.xlm_r = XLM_R(args.use_classfier, args.temp_dir, args.finetune_bert)
        
        xlmr_config = XLMRobertaConfig.from_pretrained("/mnt/raid5/lhy/project/PreSumm_cino/CINO")
        self.ext_layer = ExtTransformerEncoder(self.xlm_r.model.config.hidden_size, args.ext_ff_size, args.ext_heads,
                                               args.ext_dropout, args.ext_layers)
        if (args.encoder == 'baseline'):
            self.xlm_r.model = XLMRobertaModel(xlmr_config)
            self.ext_layer = Classifier(self.xlm_r.model.config.hidden_size)

        if(args.max_pos>512):
            my_pos_embeddings = nn.Embedding(args.max_pos, self.xlm_r.model.config.hidden_size)
            my_pos_embeddings.weight.data[:512] = self.xlm_r.model.embeddings.position_embeddings.weight.data
            my_pos_embeddings.weight.data[512:] = self.xlm_r.model.embeddings.position_embeddings.weight.data[-1][None,:].repeat(args.max_pos-512,1)
            self.xlm_r.model.embeddings.position_embeddings = my_pos_embeddings


        if checkpoint is not None:
            self.load_state_dict(checkpoint['model'], strict=True)
        else:
            if args.param_init != 0.0:
                for p in self.ext_layer.parameters():
                    p.data.uniform_(-args.param_init, args.param_init)
            if args.param_init_glorot:
                for p in self.ext_layer.parameters():
                    if p.dim() > 1:
                        xavier_uniform_(p)

        self.to(device)

    def forward(self, src, segs, clss, mask_src, mask_cls):
        top_vec = self.xlm_r(src, segs, mask_src)#, token_type_ids=segs
        sents_vec = top_vec[torch.arange(top_vec.size(0)).unsqueeze(1), clss]
        sents_vec = sents_vec * mask_cls[:, :, None].float()
        sent_scores = self.ext_layer(sents_vec, mask_cls).squeeze(-1)
        return sent_scores, mask_cls


class AbsSummarizer(nn.Module):
    def __init__(self, args, device, checkpoint=None, bert_from_extractive=None):
        super(AbsSummarizer, self).__init__()
        self.args = args
        self.device = device
        self.xlm_r = XLM_R(args.large, args.temp_dir, args.finetune_bert)

        xlmr_config = XLMRobertaConfig.from_pretrained("/mnt/raid5/lhy/project/PreSumm_cino/CINO")
        if bert_from_extractive is not None:
            self.xlm_r.model.load_state_dict(
                dict([(n[12:], p) for n, p in bert_from_extractive.items() if n.startswith('xlm_r.model')]), strict=True)

        if (args.encoder == 'baseline'):
            xlmr_config = XLMRobertaConfig.from_pretrained("/mnt/raid5/lhy/project/PreSumm_cino/CINO")
            self.xlm_r.model = XLMRobertaModel(xlmr_config)

        if(args.max_pos>512):
            my_pos_embeddings = nn.Embedding(args.max_pos, self.xlm_r.model.config.hidden_size)
            my_pos_embeddings.weight.data[:512] = self.xlm_r.model.embeddings.position_embeddings.weight.data
            my_pos_embeddings.weight.data[512:] = self.xlm_r.model.embeddings.position_embeddings.weight.data[-1][None,:].repeat(args.max_pos-512,1)
            self.xlm_r.model.embeddings.position_embeddings = my_pos_embeddings
            
        self.vocab_size = xlmr_config.vocab_size
        tgt_embeddings = nn.Embedding(self.vocab_size, self.xlm_r.model.config.hidden_size, padding_idx=1)
        if (self.args.share_emb):
            tgt_embeddings.weight = copy.deepcopy(self.xlm_r.model.embeddings.word_embeddings.weight)

        self.decoder = TransformerDecoder(
            self.args.dec_layers,
            self.args.dec_hidden_size, heads=self.args.dec_heads,
            d_ff=self.args.dec_ff_size, dropout=self.args.dec_dropout, embeddings=tgt_embeddings)

        self.generator = get_generator(self.vocab_size, self.args.dec_hidden_size, device)
        self.generator[0].weight = self.decoder.embeddings.weight


        if checkpoint is not None:
            self.load_state_dict(checkpoint['model'], strict=False)
        else:
            for module in self.decoder.modules():
                if isinstance(module, (nn.Linear, nn.Embedding)):
                    module.weight.data.normal_(mean=0.0, std=0.02)
                elif isinstance(module, nn.LayerNorm):
                    module.bias.data.zero_()
                    module.weight.data.fill_(1.0)
                if isinstance(module, nn.Linear) and module.bias is not None:
                    module.bias.data.zero_()
            for p in self.generator.parameters():
                if p.dim() > 1:
                    xavier_uniform_(p)
                else:
                    p.data.zero_()
            if(args.use_bert_emb):
                tgt_embeddings = nn.Embedding(self.vocab_size, self.xlm_r.model.config.hidden_size, padding_idx=1)
                tgt_embeddings.weight = copy.deepcopy(self.xlm_r.model.embeddings.word_embeddings.weight)
                self.decoder.embeddings = tgt_embeddings
                self.generator[0].weight = self.decoder.embeddings.weight

        self.to(device)

    def forward(self, src, tgt, segs, clss, mask_src, mask_tgt, mask_cls, language_ids):
        if language_ids is None:
            top_vec = self.xlm_r(src, segs, mask_src)
        else:
            top_vec = self.xlm_r(src, segs, mask_src, language_ids = language_ids)
        
        #save_vectors(csv_path=?,top_vec,src)
        dec_state = self.decoder.init_decoder_state(src, top_vec)
        decoder_outputs, state = self.decoder(tgt[:, :-1], top_vec, dec_state)
        return decoder_outputs, None
