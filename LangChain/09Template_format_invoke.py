from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate,ChatPromptTemplate

"""
1. PromptTemplate -> StringPromptTemplate -> ChatPromptTemplate -> Runnable
2. FewShotPromptTemplate -> StringPromptTemplate -> ChatPromptTemplate -> Runnable
3. ChatPromptTemplate -> StringPromptTemplate -> ChatPromptTemplate -> Runnable
"""

template = PromptTemplate.from_template("我的邻居是{neighbor}，他是一个{job}。")

res1=template.format(neighbor="张三", job="医生")       #传入参数，返回字符串
print(res1,type(res1))

res2=template.invoke({"neighbor":"李四","job":"教师"})  #传入字典，返回对象实例，可以进chain使用
print(res2,type(res2))