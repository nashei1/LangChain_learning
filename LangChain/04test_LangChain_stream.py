from langchain_community.llms.tongyi import Tongyi

#qwen3-max是聊天模型，qwen-max是大语言模型
model = Tongyi(model="qwen-max")

#调用stream方法
res = model.stream(input="你是谁啊，能做什么")

for r in res:
    print(r,end="",flush=True)