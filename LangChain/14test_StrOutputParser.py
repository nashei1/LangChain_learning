from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate

model = ChatTongyi(model="qwen3-max")
prompt = PromptTemplate.from_template(
    "我的邻居姓{lastname}刚生了{gender}你帮我起一个名字,仅告诉我名字"
)


#模型结果是aimessage 不能直接输入模型
parser = StrOutputParser()  #字符串解析器，将输入解析成字符串
chain = prompt | model | parser | model

res = chain.invoke({"lastname":"李", "gender":"女孩"})
print(res.content)

chain1=prompt|model|parser|model|parser
res1=chain1.invoke({"lastname":"张","gender":"男孩"})
print(res1)