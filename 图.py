#-*-coding:utf8-*-
A=[[0, 5, 0, 2, 0],
   [5, 0, 6, 8, 0],
   [0, 6, 0, 3, 7],
   [2, 8, 3, 0, 9],
   [0, 0, 7, 9, 0]]
#1.查找给定节点有哪些相邻点 v2,v4
#用一个列表表示是否访问过,0 表示没访问，1表示访问过
#visit=[0,1,0,0,1]  下标定位节点visit[4]=1
#表示节点v4 已经访问过了
#2.加深要求，只显示没被访问过的节点
visit=[0,1,0,0,1,0]
def get_side(id):
    #j代表了第几列,id给定了行
    for j in range(5):
        if A[id-1][j]!=0 and visit[j+1]==0:
            print('v%s,'%(j+1)),
get_side(5)
#作业 v1->v2 v1->v6
B=[[1,2,5],[1,4,2],[2,3,6],[2,4,8],
   [3,4,3],[3,5,7],[4,5,9]]
#v1->v2=5
def display():
    for e in B:
        print('v%s->v%s=%s'%(e[0],e[1],e[2]))
#display()
A1=[[3,4],[5,6],[1,3],[1,4],[2,4]]

