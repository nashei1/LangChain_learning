from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.tools import tool



agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[],
    system_prompt="你是一个聊天助手，可以回答用户问题。"
)

res = agent.invoke(
    {
        "messages" : [
            {"role": "user", "content": "明天长春的天气如何？"}
        ]
    }
)

print(res)

@tool(description="获取天气信息")
def get_weather() -> str:
    return "晴天"

agent2 = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[get_weather],
    system_prompt="你是一个聊天助手，可以回答用户问题。"
)
res2 = agent2.invoke(
    {
        "messages" : [
            {"role": "user", "content": "明天长春的天气如何？"}
        ]
    }
)
print(res2)

for msg in res2["messages"]:
    print(type(msg).__name__,msg.content)