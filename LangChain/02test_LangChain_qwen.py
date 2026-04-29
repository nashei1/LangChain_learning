from langchain_community.llms.tongyi import Tongyi

#qwen3-max是聊天模型，qwen-max是大语言模型
model = Tongyi(model="qwen-max")

#调用invoke方法，传入问题
res = model.invoke(input="你是谁啊，能做什么")

print(res)