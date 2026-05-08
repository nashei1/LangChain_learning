from langchain_community.document_loaders import JSONLoader


loader1 = JSONLoader(
    file_path="./data/stu.json",
    jq_schema=".name",
)
document = loader1.load()
print(document)

loader2 = JSONLoader(
    file_path="./data/stu.json",
    jq_schema=".other.addr",
)
document = loader2.load()
print(document)

loader3 = JSONLoader(
    file_path="./data/stu_json_lines.json",
    jq_schema=".name",
    text_content=False,     # 告知JSONLoader 我抽取的内容不是字符串
    json_lines=True         # 告知JSONLoader 这是一个JSONLines文件（每一行都是一个独立的标准JSON）
)
document = loader3.load()
print(document)

