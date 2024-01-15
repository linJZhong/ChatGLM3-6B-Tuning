# ChatGLM-Instruct-Tuning

基于清华的 [ChatGLM3-6B](https://github.com/THUDM/ChatGLM3) + Alpaca中文预料part1部分数据集 方式进行finetune.

数据集: [alpaca中文数据集part](https://github.com/hikariming/alpaca_chinese_dataset/blob/main/%E7%BF%BB%E8%AF%91%E5%90%8E%E7%9A%84%E4%B8%AD%E6%96%87%E6%95%B0%E6%8D%AE/alpaca_data-0-3252-%E4%B8%AD%E6%96%87-%E5%B7%B2%E5%AE%8C%E6%88%90.json)


## 准备
- 显卡: 显存 >= 16G (最好24G或者以上)
- 环境：
- - python>=3.8
-  由于我本机显卡算力不足，我是在云平台租用的显卡，一般6B模型的话
租用一张3090/4090单卡（24G）即可，PyTorch镜像选尽量新的，我目前的2.0.1



### 安装依赖
```
pip install -r requirements.txt
```

### 下载数据
```
cd data
git clone https://github.com/hikariming/alpaca_chinese_dataset/blob/main/%E7%BF%BB%E8%AF%91%E5%90%8E%E7%9A%84%E4%B8%AD%E6%96%87%E6%95%B0%E6%8D%AE/alpaca_data-0-3252-%E4%B8%AD%E6%96%87-%E5%B7%B2%E5%AE%8C%E6%88%90.json
```

### 数据预处理


转化数据集为如下格式数据

```
[
  {
    "prompt": "<prompt text>",
    "response": "<response text>"
  }
  // ...
]
```

### 进行训练


```bash

lora:  bash scripts/finetune-lora.sh
p-tuning2 : bash scripts/finetune-pt2.sh

```

### 推理
```
# 要先把文件中的 "output/your_model_path"替换为你自己项目中具体的模型path
python infer.py
```

### ToDO
1、目前模型微调效果，会比原先模型在数据集知识领域回答的要好，但是存在大模型遗忘性缺陷，后续需要对此进行改善

2、增加全量微调流程

