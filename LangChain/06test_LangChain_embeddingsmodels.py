from langchain_community.embeddings import DashScopeEmbeddings

#阿里云嵌入模型 默认是 text-embedding-v1
model = DashScopeEmbeddings()

#embed_query单次转换、embed_documents批量转换
print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你", "我讨厌你","我喜欢吃苹果"]))