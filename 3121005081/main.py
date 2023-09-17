import array
import os
import re
import numpy as np
import jieba
from sklearn.feature_extraction.text import CountVectorizer
import sys

# 加载数据
# 限制了数据只能在data文件夹中，因此，只需要将对比的文件放入data文件夹中，然后直接通过文件名就可以调用
def load_data(localtion,enconding='utf8'):
    try:
        # 打开文件
        F=open(localtion,'r',encoding=enconding)
        # 返回文件内容
        data=F.read()
        F.close()
        return data
    except :

        # 如果所需要的文件名不存在

        print("你所输入的文件名并不存在‘data’文件夹中")
        #os.system('pause')
        exit()


# 过滤器
# 目的是过滤掉标点符号，换行符等没有什么意义的符号
def filter(data):

    result=[]

    # 遍历 ,data中所有的元素
    for index in data:
        # 用正则表达式将，a-z,A-Z,0-9,汉字,有意义的留下来
        if(re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]",index)):
            result.append(index)
        else:
            pass
    return result

# 分词
def seg(data):
    data=jieba.cut(data)
    data=filter(data)
    return " ".join(data)

# 计算余弦相似度
# 传入参数为numpy
def cos_similarity(vector1,vector2):
    dot=np.sum(np.dot(vector1,vector2))
    a=np.sum(vector1**2)**0.5
    b=np.sum(vector2**2)**0.5
    return dot/(a*b)

# 将词句转换为向量
def TF(data1,data2):
    count_vec=CountVectorizer()
    data=[data1,data2]
    vec_1=count_vec.fit_transform(data).toarray()[0]
    vec_2=count_vec.fit_transform(data).toarray()[1]
    return vec_1,vec_2

# 将结果写入文件
def save_result(localtion,result,encoding='utf-8'):
    F=open(localtion,'w',encoding=encoding)
    F.write("%.2f"%result)
    F.close()

def run(data1_location,data2_location,result_location3):
    data1=load_data(data1_location)
    data2=load_data(data2_location)
    data1=seg(data1)
    data2=seg(data2)

    vc1,vc2=TF(data1,data2)
    result=cos_similarity(vc1,vc2)

    save_result(result_location3,result)

if __name__=='__main__':
    data1=sys.argv[0]
    data2=sys.argv[1]
    result=sys.argv[2]
    run(data1,data2,result)

