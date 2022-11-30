#-*-coding:utf8-*-
#顺序查找
A=[3,6,9,23,67,77]
def find(data):
    for i in A:
        if i==data:
            return True
    return False
#print(find(77))
#折半查找(前提是A已经排好序从小到大)
#这个递归算法有两个出口
#1.找到了！  #id_begin>id_end(找不到)
def halfFind(data,id_begin,id_end):
    #中间位置的下标
    id_mid=(id_begin+id_end)/2
    #找到了，函数返回(出口1)
    if data==A[id_mid]:
        return True
    #找不到，返回（出口2）
    if id_begin>id_end:
        return False
    #把data与中间值比较
    if data<A[id_mid]:
        #data比中间值小，取前半部，开始位置不变
        #结束位置是中间位置-1
        id_end=id_mid-1
        #进行递归调用，参数id_end已经改变
        #halfFind(data,id_begin,id_end)
    if  data>A[id_mid]:
        #data比中间值大，取后半部，结束位置不变
        #开始位置是中间位置+1
        id_begin=id_mid+1
    return halfFind(data, id_begin, id_end)
#非递归折半查找
def halfFindF(data):
#退出循环的条件1.找到了
# 2.开始位置>结束位置（找不到）
#在循环中要改变开始位置与结束位置
#！！！在循环外面定义位置变量（初始值）
    id_begin=0
    id_end=len(A)-1
    while True:
        id_mid=(id_begin+id_end)/2
        #找到了
        if data==A[id_mid]:
            return True
        #找不到
        if id_begin>id_end:
            return False
        if data>A[id_mid]:
            id_begin=id_mid+1
        else:
            id_end=id_mid-1
print(halfFindF(233))
#print halfFind(78,0,len(A)-1)