from __future__ import division

import argparse
import glob
import os
import random
import signal
import time

import torch
from transformers import XLMRobertaTokenizer


from models import model_builder
# from models.data_loader import load_dataset
# from models.loss import abs_loss
from torch.utils.data import DataLoader, TensorDataset
from torch.utils.data import Dataset
from models.model_builder import AbsSummarizer
from models.predictor import build_predictor
from torchsummary import summary
from transformers import XLMRobertaTokenizer

tokenizer = XLMRobertaTokenizer.from_pretrained("/mnt/raid5/lhy/project/PreSumm_cino/CINO")



language_dict = {
            'zh': 0,
            '中文': 0,
            'bo': 1,
            '藏文': 1,
            'ug': 2,
            '维文': 2
        }

class CustomDataset(Dataset):
    def __init__(self, src, segs, clss, attention_masks, mask_cls, language_ids, batch_size = 1):
        self.src = src
        self.segs = segs
        self.clss = clss
        self.mask_src = attention_masks
        self.mask_cls = mask_cls
        self.language_ids = language_ids
        self.batch_size = batch_size

    def __len__(self):
        return len(self.src)

    def __getitem__(self, index):
        return {
            'src': self.src[index],
            'segs': self.segs[index],
            'clss': self.clss[index],
            'mask_src': self.mask_src[index],
            'mask_cls': self.mask_cls[index],
            'language_ids': self.language_ids[index] 
        }

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

def custom_collate_fn(batch):
    # 假设batch是一个列表，其中每个元素是一个字典，拥有相同的键
    # 例如：[{'input_ids': tensor1, 'segs': tensor2, ..., 'src_str': list1}, {...}, ...]

    # 初始化字典以收集所有数据字段
    batch_data = {
        'src': [],
        'segs': [],
        'clss': [],
        'mask_src': [],
        'mask_cls': [],
        'language_ids':[]
    }

    for item in batch:
        batch_data['src'].append(item['src'])
        batch_data['segs'].append(item['segs'])
        batch_data['clss'].append(item['clss'])
        batch_data['mask_src'].append(item['mask_src'])
        batch_data['mask_cls'].append(item['mask_cls'])
        batch_data['language_ids'].append(item['language_ids'])

    # 对于前六个字段，我们使用torch.stack来合并列表中的tensor
    for key in ['src', 'segs', 'clss', 'mask_src', 'mask_cls','language_ids']:
        # 确保所有元素都是Tensor
        batch_data[key] = [torch.tensor(item) if not isinstance(item, torch.Tensor) else item for item in batch_data[key]]
        batch_data[key] = torch.stack(batch_data[key], dim=0)

    # src_str 保持为列表形式，不需要stack
    # batch_data['src_str'] 本来就已经是列表了，不需要额外处理

    return batch_data

def process_text_2_test_iter(contexts, device, language='zh', batch_size=1):
    # 这将存储所有文本的处理结果
    all_input_ids = []
    all_attention_masks = []
    all_segs = []
    all_clss = []
    all_mask_cls = []
    all_src_str = []
    all_language = []

    max_length = 512

    for context in contexts:

        #尽量保留原文本
        context = truncate_context_to_fit_tokenizer(context, tokenizer, max_length = max_length)

        # tokenizer处理，获取input_ids和attention_mask
        encoding = tokenizer(context, max_length=max_length, padding='max_length', truncation=True, return_tensors='pt')
        input_ids = encoding['input_ids']
        attention_mask = encoding['attention_mask']
        
        # segs全零张量,CINO没有token_typeid
        segs = torch.zeros(max_length, dtype=torch.long)
        
        # clss为每个句子的起始位置
        clss = [-1] * input_ids.size(1)  # 初始化clss列表
        clss[0] = 0
            
        
        clss = torch.tensor(clss)
        # mask_cls
        mask_cls = ~ (clss == -1)
        clss[clss == -1] = 0
        
        # 累积处理结果
        all_input_ids.append(input_ids)
        all_attention_masks.append(attention_mask)
        all_segs.append(segs)
        all_clss.append(clss)
        all_mask_cls.append(mask_cls)

        language_id = language_dict[language]
        all_language.append(torch.tensor(language_id))

    num_samples = len(all_input_ids)
    
    # Flatten all_input_ids, all_attention_masks, and all_segs, assuming they are lists of 2D tensors
    all_input_ids = torch.cat(all_input_ids, dim=0)
    all_attention_masks = torch.cat(all_attention_masks, dim=0)
    
    # Flatten all_clss and all_mask_cls, and make sure they match the batch dimension
    # Assuming all_clss and all_mask_cls are lists of 1D tensors
    all_segs = torch.cat([segs.unsqueeze(0) for segs in all_segs], dim=0)
    all_clss = torch.cat([cls.unsqueeze(0) for cls in all_clss], dim=0)
    all_mask_cls = torch.cat([mask.unsqueeze(0) for mask in all_mask_cls], dim=0)


    # Check that the batch dimension matches
    assert all_input_ids.size(0) == num_samples
    assert all_attention_masks.size(0) == num_samples
    assert all_segs.size(0) == num_samples
    assert all_clss.size(0) == num_samples
    assert all_mask_cls.size(0) == num_samples

    #print(f'all_input_ids:{all_input_ids.shape}')
    #print(all_src_str)
    #print(len(all_src_str))
    # 创建TensorDatasets
    dataset = CustomDataset(
        all_input_ids,
        all_segs,
        all_clss,
        all_attention_masks,
        all_mask_cls,
        all_language,
        batch_size = batch_size
    )
    
    # 使用DataLoader来处理batching
    data_loader = DataLoader(dataset, batch_size=batch_size, collate_fn=custom_collate_fn, shuffle=False)

    
    return data_loader

def generate(model, args, contexts, device, model_path='', batch_size=1, language='zh', min_length =30, max_length=140):
    
    args.min_length = min_length
    args.max_length = max_length

    if (model_path != ''):
        test_from = model_path
    else:
        test_from = args.test_from

    try:
        step = int(model_path.split('.')[-2].split('_')[-1])
    except:
        step = 0

    

    #checkpoint = torch.load(test_from, map_location=lambda storage, loc: storage)
    #opt = vars(checkpoint['opt'])
    # for k in opt.keys():
    #     if (k in model_flags):
    #         setattr(args, k, opt[k])
    #print(args)

    #model = AbsSummarizer(args, device, checkpoint)
    model.eval()
    test_iter = process_text_2_test_iter(contexts, device, batch_size=batch_size, language = language)
    # test_iter = data_loader.Dataloader(args, load_dataset(args, 'test', shuffle=False),
    #                                    args.test_batch_size, device,
    #                                    shuffle=False, is_test=True)
    tokenizer = XLMRobertaTokenizer.from_pretrained("/mnt/raid5/lhy/project/PreSumm_cino/CINO")
    symbols = {
    'BOS': tokenizer.convert_tokens_to_ids(tokenizer.cls_token),
    'EOS': tokenizer.convert_tokens_to_ids(tokenizer.sep_token),
    'PAD': tokenizer.convert_tokens_to_ids(tokenizer.pad_token),
    'EOQ': tokenizer.convert_tokens_to_ids(tokenizer.sep_token)
}
    predictor = build_predictor(args, tokenizer, symbols, model)
    predictor.translate(test_iter, step, device)
    return predictor.Abstractive

