#-*-coding:utf8-*-
class Node(object):
    #x行下标，y列下标，data数据
    def __init__(self,x,y,data):
        self.x=x
        self.y=y
        self.data=data
mx1=[[1, 0, 0, 0, 0, 0, 0, 0, 0, 10],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 20],]
d1=Node(0,0,1)
d2=Node(2,0,2)
d3=Node(2,2,7)
d4=Node(3,2,8)
d5=Node(3,3,9)
a=[d1,d2,d3,d4,d5]
#吧稀疏矩阵转换成二维列表
def xs2list(xs):
    #第一步：找到行下标与列下标的最大值max
    max=0
    for node in xs:
        if node.x>max:
            max=node.x
        if node.y>max:
            max=node.y
    #print(max)
    #第二步：构造一个max*max大的列表lst，默认全为0
    A = []
    for i in range(max+1):
        A.append([0]*(max+1))
    #第三步：根据xs里面node的值，在lst相应位置赋值
    for node in xs:
        A[node.x][node.y]=node.data
    return A
#打印二维列表
def showMatrx(matrx):
    for i in range(len(matrx)):
        for j in range(len(matrx)):
            print(matrx[i][j]),
        print('')
b=xs2list(a)
showMatrx(b)
#A[0][0]=1
#A[2][0]=2
# 输入2维列表，转换成稀疏矩阵
def change(matrix):
    A=[]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            data=matrix[i][j]
    #对不为0的数据进行处理，跳过0的数据
            if data!=0:
    #构造一个Node，把行下标，列下标，数据填好
                node=Node(i,j,data)
                A.append(node)
    return A
def show(a):
    for node in a:
        print('A[%s][%s]=%s'%(node.x,node.y,
                              node.data))
        #print(node.x,node.y,node.data)
#把二维列表mx1变成稀疏矩阵xsm
# xsm=change(mx1)
#显示xsm
# show(xsm)
class LinkTable:
    pass
for i in range(4):
    lk=LinkTable()
    #........lk

lk1=LinkTable()#1-->None
lk2=LinkTable()#None
lk3=LinkTable()#(0,2)-->(2,7)->None
lk4=LinkTable()#8-->9-->None
table=[lk1,lk2,lk3,lk4]
