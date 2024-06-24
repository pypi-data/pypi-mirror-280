from .model_builder import *
from .generate import *
import torch
from types import SimpleNamespace


class Config:
    def __init__(self, **entries):
        self.__dict__.update(entries)

# 定义参数的字典
args_dict = {
    'accum_count': 1,
    'alpha': 0.8,
    'batch_size': 8000,
    'beam_size': 5,
    'bert_data_path': '',
    'beta1': 0.9,
    'beta2': 0.999,
    'block_trigram': True,
    'dec_dropout': 0.2,
    'dec_ff_size': 2048,
    'dec_heads': 8,
    'dec_hidden_size': 1024,
    'dec_layers': 6,
    'enc_dropout': 0.2,
    'enc_ff_size': 512,
    'enc_hidden_size': 512,
    'enc_layers': 6,
    'encoder': 'bert',
    'ext_dropout': 0.2,
    'ext_ff_size': 2048,
    'ext_heads': 8,
    'ext_hidden_size': 1024,
    'ext_layers': 2,
    'finetune_bert': True,
    'generator_shard_size': 32,
    'gpu_ranks': [0],
    'label_smoothing': 0.1,
    'large': False,
    'load_from_extractive': '',
    'lr': 1,
    'lr_bert': 0.002,
    'lr_dec': 0.002,
    'max_grad_norm': 0,
    'max_length': 70,
    'max_pos': 512,
    'max_tgt_len': 140,
    'min_length': 30,
    'mode': 'test',
    'optim': 'adam',
    'param_init': 0,
    'param_init_glorot': True,
    'recall_eval': False,
    'report_every': 1,
    'report_rouge': True,
    'save_checkpoint_steps': 5,
    'seed': 666,
    'sep_optim': True,
    'share_emb': True,
    'task': 'abs',
    'temp_dir': '../temp',
    'test_all': False,
    'test_batch_size': 8000,
    'test_from': '',#../results/Abs/combine-3/all/model_step_80000.pt
    'test_start_from': -1,
    'train_from': '',
    'train_steps': 1000,
    'use_bert_emb': False,
    'use_classfier': False,
    'use_interval': True,
    'visible_gpus': 0,
    'warmup_steps': 8000,
    'warmup_steps_bert': 8000,
    'warmup_steps_dec': 8000,
    'world_size': 1
}


class Lacmia(nn.Module):
    """
    Lacama类，继承自PyTorch的nn.Module，用于多语言摘要生成任务。

    参数:
    - device (str): 指定模型运行的设备，默认为'cpu'。
    - model_path (str): 指定预训练模型的路径，默认为None值。
    - language (str): 模型处理的目标语言，默认为'zh'（中文）。
    - load_pretrained_bert (bool): 是否加载训练的模型，默认为True。

    属性:
    - args: 通过initialize_args函数初始化的参数对象。
    - language: 模型处理的语言。
    - model_path: 预训练模型的文件路径。
    - config: 使用XLMRobertaConfig加载的模型配置对象。
    - model: AbsSummarizer模型实例。
    - device: 模型运行的设备。
    - if_load: 标记模型是否已加载，避免重复加载。

    方法:
    - __init__: 类的构造函数，用于初始化模型及其相关配置。

    注意:
    - 若model_path为空或None，则会跳过加载模型的步骤，使用随机初始化的模型。
    - 需要事先导入PyTorch相关模块和XLMRobertaConfig，以及定义AbsSummarizer模型。
    """
    def __init__(self, device='cpu', model_path = None, language = 'zh', load_pretrained_bert = True):
        super(Lacmia, self).__init__()

        self.args = Config(**args_dict)

        self.language = language
        self.model_path = model_path

        self.config = XLMRobertaConfig.from_pretrained("/mnt/raid5/lhy/project/PreSumm_cino/CINO")
        self.model = AbsSummarizer(self.args, device)
        self.device = device
        
        self.if_load = False
        #不使用训练过的模型,使用随机初始化的模型
        if model_path == '' or model_path == None:
            print('Use a random model')
            self.if_load = True
        self.language_dict = {
                        'zh': 0,
                        '中文': 0,
                        'bo': 1,
                        '藏文': 1,
                        'ug': 2,
                        '维文': 2
                    }

    def Abstractive(self,contexts, language='zh', batch_size=1, min_length=30,max_length=140):
        """
        运行生成式摘要过程。

        参数:
        - self: 类实例的引用。
        - contexts (list of str): 需要进行摘要提取的文本列表。
        - batch_size (int, optional): 在模型推理过程中一次处理的文本数量，默认为1。
        - language (str, optional): 输入文本的语言，默认为'zh'（中文）。
        - len_pred (int, optional): 预期生成摘要的句子数量，默认为2。

        返回:
        - condidate_list (list of str): 模型生成的摘要列表。

        过程描述:
        - 首先检查模型是否已加载，如果尚未加载，则加载模型并设置为评估模式。
        - 使用生成函数生成摘要，该函数接受模型、文本、设备等参数。
        - 返回生成的摘要列表。

        """
        if self.if_load == False:
            checkpoint = torch.load(self.model_path, map_location=lambda storage, loc: storage)
            self.model = AbsSummarizer(self.args, self.device, checkpoint)
            self.model.eval()
            self.if_load = True
            print(f'load model success. load from{self.model_path}')
        condidate_list = generate(self.model, self.args, contexts, self.device, batch_size=batch_size, language=language, min_length=min_length, max_length=max_length)
        
        return condidate_list