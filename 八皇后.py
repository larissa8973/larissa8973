#-*-coding:utf8-*-
A=[]
for i in range(8):
    A.append([0]*8)
#这里面将用来放成功以后的皇后的坐标位置
result=[]
#将二维列表复制一份
def copy(s):
    t = []
    for i in range(8):
        t.append([0] * 8)
    for i in range(8):
        for j in range(8):
            t[i][j]=s[i][j]
    return t
#显示
def show(m):
    for i in range(8):
        for j in range(8):
            print('%s '%m[i][j]),
        print('')
    print('')
#在位置（x，y）处放入一个2，修改其它受影响的位置
def putOne(x,y,A):
    for i in range(8):
        for j in range(8):
            if i==x or y==j or \
                (i-x==j-y) or \
                (i-x == y-j):
                A[i][j]=1
    A[x][y] = 2
#根据result把皇后位置填上去2
def fillResult():
    for node in result:
        print(node)
        C[node[0]][node[1]]=2
#putOne(3,3,A)
#show()
def eightQ(n,A):
    if n==1:
        for i in range(8):
            for j in range(8):
                if A[i][j] == 0:
                    result.append([i,j])
                    return True
    for i in range(8):
        for j in range(8):
            if A[i][j]==0:
                #为什么要copy一份？？？
    #因为如果后面不成功，那么后面尝试的过程会把A里面
    #的值改变了，所以，如果后面不成功，那么要后面的
    #修改取消掉，让A从最初的状态开始（注意，是这一轮
    #最初的状态，而不是全部归0！！！ ）
                B = copy(A)
                putOne(i,j,B)
                ok=eightQ(n-1,B)
                if ok:
                    #成功了，添加
                    result.append([i, j])
                    return ok
    return False
C=copy(A)
eightQ(8,A)
fillResult()
show(C)