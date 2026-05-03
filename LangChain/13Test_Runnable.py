from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

promot = PromptTemplate.from_template("你是一个ai助手")
model=Tongyi(model="qwen3-max")

chain = promot | promot | promot | model
# chain.invoke()
# chain.stream()
print(type(chain))
