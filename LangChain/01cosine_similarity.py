

def get_dot(a, b):
    #计算两个向量的点积
    if len(a) != len(b):
        raise ValueError("两个向量的维度必须相同")
    
    dot_sum=0
    for i,j in zip(a,b):
        dot_sum+=i*j

    return dot_sum

def get_norm(a):
    #计算向量的模长
    norm_sum=0
    for i in a:
        norm_sum+=i**2

    return norm_sum**0.5

def cosine_similarity(a, b):
    #计算两个向量的余弦相似度
    dot=get_dot(a,b)
    norm_a=get_norm(a)
    norm_b=get_norm(b)
    
    if norm_a==0 or norm_b==0:
        raise ValueError("向量的模长不能为零")
    
    return dot/(norm_a*norm_b)

if __name__ == "__main__":
    a=[0.5,0.5]
    b=[0.7,0.7]
    c=[0.7,0.5]
    d=[-0.6,-0.5]
    print("a和b的余弦相似度:",cosine_similarity(a,b))
    print("a和c的余弦相似度:",cosine_similarity(a,c))
    print("a和d的余弦相似度:",cosine_similarity(a,d))