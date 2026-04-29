from langchain_ollama import OllamaLLM

model = OllamaLLM(model="本地模型")

res = model.invoke(input="你是谁啊，能做什么")
print(res)