from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

parser=StrOutputParser()

#将函数转化成Runnable接口
my_func=RunnableLambda(lambda ai_msg:{"name":ai_msg.content})

model=ChatTongyi(model="qwen3-max")

prompt1=PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请帮忙起名字，仅生成一个名字，并告知我名字，不要额外信息。"
)
prompt2=PromptTemplate.from_template(
    "姓名{name}，请帮我解析含义。"
)

chain = prompt1 | model | my_func | prompt2 | model | parser
#函数也可以直接入chain
chain1 = prompt1 | model | (lambda ai_msg:{"name":ai_msg.content}) | prompt2 | model | parser


# res=chain.invoke({"lastname":"李","gender":"女儿"})
# print(res)
for chunk in chain1.stream({"lastname":"李","gender":"女儿"}):
    print(chunk,end="",flush=True)


