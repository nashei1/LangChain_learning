from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models import ChatTongyi

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个边塞诗人"),
        MessagesPlaceholder("history"),
        ("human", "请再写一首唐诗")
    ]
)

history_data = [
    ("human", "请写一首唐诗"),
    ("ai", "床前明月光，疑是地上霜。举头望明月，低头思故乡。"),
    ("human", "请再写一首唐诗"),
    ("ai", "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。")
]

model=ChatTongyi(model="qwen3-max")

#组成chain 每一个组件都是Runnable的子类 chain是RunnableSerializable对象
chain = chat_template | model

#通过chain调用invoke方法或stream方法
response = chain.invoke({"history": history_data})
print(response.content)

for i in chain.stream({"history": history_data}):
    print(i.content,end=" ",flush=True)