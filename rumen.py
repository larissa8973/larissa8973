#-*-coding:utf8-*-
n=10
cnt=0
for i in range(n):
    for j in range(n):
        print('数据结构')
        cnt+=1
print(cnt)
class Person(object):
    def __init__(self,sex,age):
        self.age=age
class Man(Person):
    def __init__(self,age):
        Person.__init__(self,'nan',age)
man=Man(50)
print(man.age)
#线性表（顺序存储，链式存储）
# 一个一维数组Ｍ，下标的范围是０到９，
# 每个数组元素用相邻的4个字节存储。
# 存储器按字节编址，
# 设存储数组元素Ｍ[０]的第一个字节的地址是８，
# 则Ｍ[9]的第一个字节的地址是