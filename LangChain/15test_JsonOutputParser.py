from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

str_parser = StrOutputParser()
json_parser = JsonOutputParser()

model =ChatTongyi(model="qwen3-max")

prompt1=PromptTemplate.from_template(
    "我邻居姓：{lastname}，刚生了{gender}，请帮忙起名字，"
    "并封装为JSON格式返回给我。要求key是name，value就是你起的名字，请严格遵守格式要求。"
)

prompt2=PromptTemplate.from_template(
    "姓名：{name}，请帮我解析含义。"
)

chain=prompt1|model|json_parser|prompt2|model|str_parser

res=chain.invoke({"lastname":"李","gender":"儿子"})

print(res)