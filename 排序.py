#-*-coding:utf8-*-
def insertSort():
    a=[64,5,7,89,6,24]
    print(a)
    #外循环次数确定
    for i in range(1,len(a)):
        #把待插入的数据保存
        temp=a[i]
        #把待插入的数据的前一个位置找到
        f=i-1
        #待比较的数比要插入的数据大，则继续循环
        #f的位置往前移动一个
        while a[f]>temp and f!=-1:
            #把位置f的数据覆盖它的下一个位置的值
            a[f+1]=a[f]
            #把待比较的位置往前移动一个
            f-=1
        #退出比较循环后，f+1的位置就是要插入的地方
        #不管哪种退出条件成立（a[f]<temp|f==-1），
        ## 以下逻辑都适用
        a[f+1]=temp
        print('第%s次排序：'%i),
        print(a)
    print(a)
#insertSort()
def min(begin,a):
    index=begin
    min = a[begin]
    for i in range(begin, len(a)):
        # 如果新的值比min小，那么让新的值取代min老的值
        if min > a[i]:
            min = a[i]
            index = i
    #print(min, index)
    return index
def exchange():
    a = [64, 5, 7, 89, 6, 24]
    x=0
    y=3
    temp=a[x]
    a[x]=a[y]
    a[y]=temp
    print(a)
def selectSort():
    a = [64, 5, 7, 89, 6, 24]
    print(a)
    for i in range(len(a)):
        #找到从i开始的列表a中的最小值的下标
        mindex=min(i,a)
        #i的位置的值与mindex位置的值交换
        temp=a[i]
        a[i]=a[mindex]
        a[mindex]=temp
        print('第%s次排序：'%(i+1)),
        print(a)
    print(a)
selectSort()