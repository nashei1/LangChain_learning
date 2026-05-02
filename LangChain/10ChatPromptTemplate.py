from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.llms.tongyi import Tongyi
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

chat_prompt = chat_template.invoke({"history": history_data}).to_string()

print(chat_prompt)

model = Tongyi(model="qwen-max")
res=model.invoke(chat_prompt)
print(res)

model2=ChatTongyi(model="qwen-max")
res2=model2.invoke(history_data)
print("\n",res2)
print(res2.content,type(res2))