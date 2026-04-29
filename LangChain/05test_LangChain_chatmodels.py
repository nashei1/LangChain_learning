from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

#qwen3-max是聊天模型，qwen-max是大语言模型
model = ChatTongyi(model="qwen3-max")

#消息列表
messages = [
    SystemMessage(content="你是一个边塞诗人"),
    HumanMessage(content="写一首唐诗"),
    AIMessage(content="锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"),
    HumanMessage(content="按照上一个回复的格式再写一首唐诗")
]

messages1 = [
    #(角色，内容)   本质是langchain自己转换成了message对象  好处是可以使用变量占位
    ("system","你是一个边塞诗人"),
    ("user","写一首唐诗"),
    ("ai","锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦。"),
    ("user","按照上一个回复的格式再写一首唐诗")
]

# res=model.stream(input=messages)
res=model.stream(input=messages1)

#大语言模型的输出需要用.Content来获取内容
for r in res:
    print(r.content,end="",flush=True)