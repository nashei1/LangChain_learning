from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi   

#提示词模板
prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}刚生了{gender}你帮我起一个名字,简单回答"
)

#调用format方法注入信息
prompt_text = prompt_template.format(lastname="张", gender="男孩")

print(prompt_text)

model=Tongyi(model="qwen-max")
response = model.invoke(input=prompt_text)
print(response)

chain = prompt_template | model

res=chain.invoke(input={"lastname":"李", "gender":"女孩"})
print(res)