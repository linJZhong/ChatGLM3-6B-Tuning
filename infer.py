import torch
from transformers import AutoTokenizer, AutoModel
from modeling_chatglm import ChatGLMForConditionalGeneration
from peft import PeftModel
tokenizer = AutoTokenizer.from_pretrained(
    "THUDM/chatglm3-6b", trust_remote_code=True)
model = ChatGLMForConditionalGeneration.from_pretrained(
    "output/your_model_file").half().cuda()

# Lora 训练模型 打开下面注释，加入lora model
# model = PeftModel.from_pretrained(model, "./output/")



response, history = model.chat(tokenizer, "你好", history=[],max_length=256)
print(response)
response, history = model.chat(tokenizer, "经常失眠怎么办", max_length=256,history=history)
print(response)
