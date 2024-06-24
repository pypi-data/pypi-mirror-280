#!/usr/bin/env python
""" Translator Class and builder """
from __future__ import print_function
import codecs
import os
import math

import torch

from tensorboardX import SummaryWriter

from onmt.translate import GNMTGlobalScorer
from transformers import XLMRobertaTokenizer
from tqdm import tqdm

tokenizer = XLMRobertaTokenizer.from_pretrained("/mnt/raid5/lhy/project/PreSumm_cino/CINO")
def truncate_context_to_fit_tokenizer(context, tokenizer, max_length=512):
    # 首先对原始的context进行分词
    context_tokens = tokenizer.tokenize(context)
    # 如果分词后的长度小于或等于max_length，就直接返回原始context
    if len(context_tokens) < max_length:
        return context

    # 如果分词后的长度大于max_length，需要截断
    # 注意：这里我们不再添加空格，而是直接截取token列表
    truncated_tokens = context_tokens[:max_length]

    # 使用分词器的convert_tokens_to_string方法将token列表转换回字符串
    truncated_context = tokenizer.convert_tokens_to_string(truncated_tokens)

    #print(truncated_context)

    return truncated_context

def clean_text(generated_text):
    # 转换文本
    # 首先将原始文本分割成单词和标记列表
    tokens = generated_text.split(' ')

    # 然后将标记重新连接成正确的单词
    cleaned_text = ''
    for token in tokens:
        if token.startswith('▁'):
            # 如果标记以'▁'开始，我们在前面加一个空格
            cleaned_text += ' ' + token[1:]
        else:
            # 否则直接连接标记
            cleaned_text += token

    # 去除开头可能出现的多余空格
    cleaned_text = cleaned_text.strip()
    return cleaned_text

# def custom_collate_fn(batch):
#     # 假设batch是一个列表，其中每个元素是一个字典，拥有相同的键
#     # 例如：[{'input_ids': tensor1, 'segs': tensor2, ..., 'src_str': list1}, {...}, ...]

#     # 初始化字典以收集所有数据字段
#     batch_data = {
#         'src': [],
#         'segs': [],
#         'clss': [],
#         'mask_src': [],
#         'mask_cls': [],
#         'src_str': []
#     }

#     for item in batch:
#         batch_data['src'].append(item['src'])
#         batch_data['segs'].append(item['segs'])
#         batch_data['clss'].append(item['clss'])
#         batch_data['mask_src'].append(item['mask_src'])
#         batch_data['mask_cls'].append(item['mask_cls'])
#         # src_str 是一个句子列表，直接加入列表
#         batch_data['src_str'].append(item['src_str'])

#     # 对于前五个字段，我们使用torch.stack来合并列表中的tensor
#     for key in ['src', 'segs', 'clss', 'mask_src', 'mask_cls']:
#         batch_data[key] = torch.stack(batch_data[key], dim=0)

#     # src_str 保持为列表形式，不需要stack
#     # batch_data['src_str'] 本来就已经是列表了，不需要额外处理

#     return batch_data

# def process_text_2_test_iter(contexts, device, len_pred = 2, language='zh', batch_size=1, print_setences=False):
#     # 这将存储所有文本的处理结果
#     all_input_ids = []
#     all_attention_masks = []
#     all_segs = []
#     all_clss = []
#     all_mask_cls = []
#     all_src_str = []
#     max_length = 512

#     for context in contexts:

#         #尽量保留原文本
#         context = truncate_context_to_fit_tokenizer(context, tokenizer, max_length = max_length)

#         # tokenizer处理，获取input_ids和attention_mask
#         encoding = tokenizer(context, max_length=max_length, padding='max_length', truncation=True, return_tensors='pt')
#         input_ids = encoding['input_ids']
#         attention_mask = encoding['attention_mask']
        
#         # segs全零张量,CINO没有token_typeid
#         segs = torch.zeros(max_length, dtype=torch.long)
        
#         # clss为每个句子的起始位置
#         clss = [-1] * input_ids.size(1)  # 初始化clss列表
#         clss[0] = 0
            
        
#         clss = torch.tensor(clss)
#         # mask_cls
#         mask_cls = ~ (clss == -1)
#         clss[clss == -1] = 0
        
#         # 累积处理结果
#         all_input_ids.append(input_ids)
#         all_attention_masks.append(attention_mask)
#         all_segs.append(segs)
#         all_clss.append(clss)
#         all_mask_cls.append(mask_cls)
#         all_src_str.append(sentences)

#     num_samples = len(all_input_ids)
    
#     # Flatten all_input_ids, all_attention_masks, and all_segs, assuming they are lists of 2D tensors
#     all_input_ids = torch.cat(all_input_ids, dim=0)
#     all_attention_masks = torch.cat(all_attention_masks, dim=0)
    
#     # Flatten all_clss and all_mask_cls, and make sure they match the batch dimension
#     # Assuming all_clss and all_mask_cls are lists of 1D tensors
#     all_segs = torch.cat([segs.unsqueeze(0) for segs in all_segs], dim=0)
#     all_clss = torch.cat([cls.unsqueeze(0) for cls in all_clss], dim=0)
#     all_mask_cls = torch.cat([mask.unsqueeze(0) for mask in all_mask_cls], dim=0)


#     # Check that the batch dimension matches
#     assert all_input_ids.size(0) == num_samples
#     assert all_attention_masks.size(0) == num_samples
#     assert all_segs.size(0) == num_samples
#     assert all_clss.size(0) == num_samples
#     assert all_mask_cls.size(0) == num_samples

#     #print(f'all_input_ids:{all_input_ids.shape}')
#     #print(all_src_str)
#     #print(len(all_src_str))
#     # 创建TensorDatasets
#     dataset = CustomDataset(
#         all_input_ids,
#         all_segs,
#         all_clss,
#         all_attention_masks,
#         all_mask_cls,
#         all_src_str
#     )
    
#     # 使用DataLoader来处理batching
#     data_loader = DataLoader(dataset, batch_size=batch_size, collate_fn=custom_collate_fn, shuffle=False)

    
#     return data_loader


def tile(x, count, dim=0):
    """
    Tiles x on dimension dim count times.
    """
    perm = list(range(len(x.size())))
    if dim != 0:
        perm[0], perm[dim] = perm[dim], perm[0]
        x = x.permute(perm).contiguous()
    out_size = list(x.size())
    out_size[0] *= count
    batch = x.size(0)
    x = x.view(batch, -1) \
         .transpose(0, 1) \
         .repeat(count, 1) \
         .transpose(0, 1) \
         .contiguous() \
         .view(*out_size)
    if dim != 0:
        x = x.permute(perm).contiguous()
    return x


def build_predictor(args, tokenizer, symbols, model, logger=None):
    #scorer = GNMTGlobalScorer(args.alpha,length_penalty='wu')
    scorer = GNMTGlobalScorer(args.alpha, beta=0.1, coverage_penalty='none', length_penalty='wu')

    translator = Translator(args, model, tokenizer, symbols, global_scorer=scorer, logger=logger)
    return translator


class Translator(object):
    """
    Uses a model to translate a batch of sentences.


    Args:
       model (:obj:`onmt.modules.NMTModel`):
          NMT model to use for translation
       fields (dict of Fields): data fields
       beam_size (int): size of beam to use
       n_best (int): number of translations produced
       max_length (int): maximum length output to produce
       global_scores (:obj:`GlobalScorer`):
         object to rescore final translations
       copy_attn (bool): use copy attention during translation
       cuda (bool): use cuda
       beam_trace (bool): trace beam search for debugging
       logger(logging.Logger): logger.
    """

    def __init__(self,
                 args,
                 model,
                 vocab,
                 symbols,
                 global_scorer=None,
                 logger=None,
                 dump_beam=""):
        self.logger = logger
        self.cuda = args.visible_gpus != '-1'

        self.args = args
        self.model = model
        self.generator = self.model.generator
        self.vocab = vocab
        self.tokenizer = XLMRobertaTokenizer.from_pretrained("/mnt/raid5/lhy/project/PreSumm_cino/CINO")
        self.symbols = symbols
        self.start_token = symbols['BOS']
        self.end_token = symbols['EOS']

        self.global_scorer = global_scorer
        self.beam_size = args.beam_size
        self.min_length = args.min_length
        self.max_length = args.max_length


        self.dump_beam = dump_beam
        self.Abstractive = [] #用于储存结果

        # for debugging
        self.beam_trace = self.dump_beam != ""
        self.beam_accum = None

        if self.beam_trace:
            self.beam_accum = {
                "predicted_ids": [],
                "beam_parent_ids": [],
                "scores": [],
                "log_probs": []}

    def _build_target_tokens(self, pred):
        # vocab = self.fields["tgt"].vocab
        tokens = []
        for tok in pred:
            tok = int(tok)
            tokens.append(tok)
            if tokens[-1] == self.end_token:
                tokens = tokens[:-1]
                break
        tokens = [t for t in tokens if t < len(self.vocab)]
        tokens = self.vocab.DecodeIds(tokens).split(' ')
        return tokens

    def from_batch(self, translation_batch, batch_size):
        batch = translation_batch["batch"]



        assert (len(translation_batch["gold_score"]) ==
                len(translation_batch["predictions"]))
        #batch_size = batch.batch_size

        #preds, pred_score, gold_score, tgt_str, src =  translation_batch["predictions"],translation_batch["scores"],translation_batch["gold_score"],batch['tgt_str'], batch['src']
        preds, pred_score, gold_score, src =  translation_batch["predictions"],translation_batch["scores"],translation_batch["gold_score"], batch['src']
        translations = []
        
        for b in range(batch_size):
            #pred_sents = self.vocab.convert_ids_to_tokens([int(n) for n in preds[b][0]])
            pred_sents = [self.tokenizer.convert_ids_to_tokens(int(n)) for n in preds[b][0]]
            pred_sents = ' '.join(pred_sents).replace(' ##','')
            #gold_sent = ' '.join(tgt_str[b].split())
            
            raw_src = [self.tokenizer.convert_ids_to_tokens(int(t)) for t in src[b]][:500]
            raw_src = ' '.join(raw_src)
            #translation = (pred_sents, gold_sent, raw_src)
            translation = (pred_sents, raw_src)

            translations.append(translation)

        return translations

    def translate(self,
                  data_iter, step, device,
                  attn_debug=False):

        self.model.eval()

        ct = 0
        with torch.no_grad():
            for batch in tqdm(data_iter, desc="Processing", leave=True):
                #batch.to(device)
                if(self.args.recall_eval):
                    gold_tgt_len = batch['tgt'].size(1)
                    self.min_length = gold_tgt_len + 20
                    self.max_length = gold_tgt_len + 60
                batch_data = self.translate_batch(batch, device, data_iter.batch_size)
                translations = self.from_batch(batch_data, data_iter.batch_size)
                result = []
                for trans in translations:
                    pred, src = trans
                    pred_str = pred.replace('[unused0]', '').replace('[unused3]', '').replace('[PAD]', '').replace('[unused1]', '').replace(r' +', ' ').replace(' [unused2] ', '<q>').replace('[unused2]', '').strip()

                    pred_str = clean_text(pred_str)
                    pred_str = pred_str.replace("<s>","").replace("</s>","").replace("<unk>","").replace("<pad>","")
                    result.append(pred_str)
                    
                    if(self.args.recall_eval):
                        _pred_str = ''
                        gap = 1e3
                        for sent in pred_str.split('<q>'):
                            can_pred_str = _pred_str+ '<q>'+sent.strip()
                            
                self.Abstractive.append(result)



    def translate_batch(self, batch, device, batch_size=1, fast=False):
        """
        Translate a batch of sentences.

        Mostly a wrapper around :obj:`Beam`.

        Args:
           batch (:obj:`Batch`): a batch from a dataset object
           data (:obj:`Dataset`): the dataset object
           fast (bool): enables fast beam search (may not support all features)

        Todo:
           Shouldn't need the original dataset.
        """
        with torch.no_grad():
            return self._fast_translate_batch(
                batch,
                self.max_length,
                min_length=self.min_length,
                batch_size = batch_size,
                device=device)

    def _fast_translate_batch(self,
                              batch,
                              max_length,
                              min_length=0,
                              batch_size = 1,
                              device='cpu'):
        # TODO: faster code path for beam_size == 1.

        # TODO: support these blacklisted features.
        assert not self.dump_beam
        #print(batch)
        beam_size = self.beam_size
        #batch_size = batch.batch_size
        # src = batch.src
        # segs = batch.segs
        # mask_src = batch.mask_src
        # language_ids = batch.language_ids
        src = batch['src'].to(device)
        segs = batch['segs'].to(device)
        mask_src = batch['mask_src'].to(device)
        language_ids = batch['language_ids'].to(device)
        #language_ids = None

        src_features = self.model.xlm_r(src, segs, mask_src, language_ids = language_ids)
        dec_states = self.model.decoder.init_decoder_state(src, src_features, with_cache=True)
        #device = src_features.device

        # Tile states and memory beam_size times.
        dec_states.map_batch_fn(
            lambda state, dim: tile(state, beam_size, dim=dim))
        src_features = tile(src_features, beam_size, dim=0)
        batch_offset = torch.arange(
            batch_size, dtype=torch.long, device=device)
        beam_offset = torch.arange(
            0,
            batch_size * beam_size,
            step=beam_size,
            dtype=torch.long,
            device=device)
        alive_seq = torch.full(
            [batch_size * beam_size, 1],
            self.start_token,
            dtype=torch.long,
            device=device)

        # Give full probability to the first beam on the first step.
        topk_log_probs = (
            torch.tensor([0.0] + [float("-inf")] * (beam_size - 1),
                         device=device).repeat(batch_size))

        # Structure that holds finished hypotheses.
        hypotheses = [[] for _ in range(batch_size)]  # noqa: F812

        results = {}
        results["predictions"] = [[] for _ in range(batch_size)]  # noqa: F812
        results["scores"] = [[] for _ in range(batch_size)]  # noqa: F812
        results["gold_score"] = [0] * batch_size
        results["batch"] = batch

        for step in range(max_length):
            decoder_input = alive_seq[:, -1].view(1, -1)

            # Decoder forward.
            decoder_input = decoder_input.transpose(0,1)

            dec_out, dec_states = self.model.decoder(decoder_input, src_features, dec_states,
                                                     step=step)

            # Generator forward.
            log_probs = self.generator.forward(dec_out.transpose(0,1).squeeze(0))
            vocab_size = log_probs.size(-1)

            if step < min_length:
                log_probs[:, self.end_token] = -1e20

            # Multiply probs by the beam probability.
            log_probs += topk_log_probs.view(-1).unsqueeze(1)

            alpha = self.global_scorer.alpha
            length_penalty = ((5.0 + (step + 1)) / 6.0) ** alpha

            # Flatten probs into a list of possibilities.
            curr_scores = log_probs / length_penalty

            if(self.args.block_trigram):
                cur_len = alive_seq.size(1)
                if(cur_len>3):
                    for i in range(alive_seq.size(0)):
                        fail = False
                        words = [int(w) for w in alive_seq[i]]
                        words = [self.tokenizer.convert_ids_to_tokens(w) for w in words]
                        words = ' '.join(words).replace(' ##','').split()
                        if(len(words)<=3):
                            continue
                        trigrams = [(words[i-1],words[i],words[i+1]) for i in range(1,len(words)-1)]
                        trigram = tuple(trigrams[-1])
                        if trigram in trigrams[:-1]:
                            fail = True
                        if fail:
                            curr_scores[i] = -10e20

            curr_scores = curr_scores.reshape(-1, beam_size * vocab_size)
            topk_scores, topk_ids = curr_scores.topk(beam_size, dim=-1)

            # Recover log probs.
            topk_log_probs = topk_scores * length_penalty

            # Resolve beam origin and true word ids.
            #topk_beam_index = topk_ids.div(vocab_size)
            topk_beam_index = topk_ids // vocab_size
            topk_ids = topk_ids.fmod(vocab_size)
            

            # Map beam_index to batch_index in the flat representation.
            batch_index = (
                    topk_beam_index
                    + beam_offset[:topk_beam_index.size(0)].unsqueeze(1))
            select_indices = batch_index.view(-1)
            #print(f"select_indices:{select_indices}")
            # Append last prediction.
            alive_seq = torch.cat(
                [alive_seq.index_select(0, select_indices),
                 topk_ids.view(-1, 1)], -1)

            is_finished = topk_ids.eq(self.end_token)
            if step + 1 == max_length:
                is_finished.fill_(1)
            # End condition is top beam is finished.
            end_condition = is_finished[:, 0].eq(1)
            # Save finished hypotheses.
            if is_finished.any():
                predictions = alive_seq.view(-1, beam_size, alive_seq.size(-1))
                for i in range(is_finished.size(0)):
                    b = batch_offset[i]
                    if end_condition[i]:
                        is_finished[i].fill_(1)
                    finished_hyp = is_finished[i].nonzero().view(-1)
                    # Store finished hypotheses for this batch.
                    for j in finished_hyp:
                        hypotheses[b].append((
                            topk_scores[i, j],
                            predictions[i, j, 1:]))
                    # If the batch reached the end, save the n_best hypotheses.
                    if end_condition[i]:
                        best_hyp = sorted(
                            hypotheses[b], key=lambda x: x[0], reverse=True)
                        score, pred = best_hyp[0]

                        results["scores"][b].append(score)
                        results["predictions"][b].append(pred)
                non_finished = end_condition.eq(0).nonzero().view(-1)
                # If all sentences are translated, no need to go further.
                if len(non_finished) == 0:
                    break
                # Remove finished batches for the next step.
                topk_log_probs = topk_log_probs.index_select(0, non_finished)
                batch_index = batch_index.index_select(0, non_finished)
                batch_offset = batch_offset.index_select(0, non_finished)
                alive_seq = predictions.index_select(0, non_finished) \
                    .view(-1, alive_seq.size(-1))
            # Reorder states.
            select_indices = batch_index.view(-1)
            src_features = src_features.index_select(0, select_indices)
            dec_states.map_batch_fn(
                lambda state, dim: state.index_select(dim, select_indices))

        return results


class Translation(object):
    """
    Container for a translated sentence.

    Attributes:
        src (`LongTensor`): src word ids
        src_raw ([str]): raw src words

        pred_sents ([[str]]): words from the n-best translations
        pred_scores ([[float]]): log-probs of n-best translations
        attns ([`FloatTensor`]) : attention dist for each translation
        gold_sent ([str]): words from gold translation
        gold_score ([float]): log-prob of gold translation

    """

    def __init__(self, fname, src, src_raw, pred_sents,
                 attn, pred_scores, tgt_sent, gold_score):
        self.fname = fname
        self.src = src
        self.src_raw = src_raw
        self.pred_sents = pred_sents
        self.attns = attn
        self.pred_scores = pred_scores
        self.gold_sent = tgt_sent
        self.gold_score = gold_score

    def log(self, sent_number):
        """
        Log translation.
        """

        output = '\nSENT {}: {}\n'.format(sent_number, self.src_raw)

        best_pred = self.pred_sents[0]
        best_score = self.pred_scores[0]
        pred_sent = ' '.join(best_pred)
        output += 'PRED {}: {}\n'.format(sent_number, pred_sent)
        output += "PRED SCORE: {:.4f}\n".format(best_score)

        if self.gold_sent is not None:
            tgt_sent = ' '.join(self.gold_sent)
            output += 'GOLD {}: {}\n'.format(sent_number, tgt_sent)
            output += ("GOLD SCORE: {:.4f}\n".format(self.gold_score))
        if len(self.pred_sents) > 1:
            output += '\nBEST HYP:\n'
            for score, sent in zip(self.pred_scores, self.pred_sents):
                output += "[{:.4f}] {}\n".format(score, sent)

        return output
