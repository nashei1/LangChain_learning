from openai import OpenAI

#1 获取client对象 OpenAI类的对象

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

#2 调用模型

response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role":"system","content":"你是AI助手，回答很简洁"},
        {"role":"user","content":"小明有三只宠物狗"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"小红有两只宠物猫"},
        {"role":"assistant","content":"好的"},
        {"role":"user","content":"一共有多少只宠物"}
    ],
    stream=True
)

#3 处理结果
# print(response.choices[0].message.content)
for chunk in response:
    print(
        chunk.choices[0].delta.content,
        end=" ", #段间分隔
        flush=True #立即刷新缓冲区
    )