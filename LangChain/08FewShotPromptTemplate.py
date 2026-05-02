from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_community.llms.tongyi import Tongyi

#示例提示词模板
example_prompt = PromptTemplate.from_template("单词：{word}，反义词：{meaning}")


#示例数据注入
examples = [
    {"word": "高兴", "meaning": "难过"},
    {"word": "快乐", "meaning": "悲伤"}
    ]

few_shot_prompt = FewShotPromptTemplate(
    example_prompt=example_prompt,                              #示例提示词模板
    examples=examples,                                          #示例数据
    prefix="请根据以下示例，找出下列单词的反义词：",                  #前缀
    suffix="基于以上示例告诉我，{input_word}的反义词是？",           #后缀
    input_variables=["input_word"]                              #输入变量
)

prompt_text = few_shot_prompt.format(input_word="开心")
print(prompt_text)
model=Tongyi(model="qwen-max")
response = model.invoke(input=prompt_text)
print(response)