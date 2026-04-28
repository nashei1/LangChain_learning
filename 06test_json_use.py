import json


# 将字典转换成json字符串 dumps()方法
d={
    "name":"张三",
    "age":18,
    "gender":"男"
}

print(str(d))
s1=json.dumps(d,ensure_ascii=False)
print(s1)



# 将列表转换成json字符串 dumps()方法
l=[
    {
    "name":"张三",
    "age":18,
    "gender":"男"
    },
    {
    "name":"李四",
    "age":12,
    "gender":"男"
    },
    {
    "name":"王五",
    "age":16,
    "gender":"男"
    },
]


s2=json.dumps(l,ensure_ascii=False)
print(s2)


# json转换成字典或者列表 loads()方法
json_s1='{"name": "张三", "age": 18, "gender": "男"}'
json_s2='[{"name": "张三", "age": 18, "gender": "男"}, {"name": "李四", "age": 12, "gender": "男"}, {"name": "王五", "age": 16, "gender": "男"}]'

d1=json.loads(json_s1)
l1=json.loads(json_s2)

print(d1,type(d1))      #注意引号
print(l1,type(l1))