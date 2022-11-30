#-*-coding:utf8-*-
A=[[0,  6, 0, 0, 10, 12],
   [6,  0, 3, 5,  0,  8],
   [0,  3, 0, 7,  0,  0],
   [0,  5, 7, 0,  9, 11],
   [10, 0, 0, 9,  0, 16],
   [12, 8, 0, 11, 16, 0],]
class Stack(object):
    def __init__(self,max):
        self.max=max
        self.items=[None]*max
        self.top=-1
    def isFull(self):
        return self.top==self.max-1
    def isEmpty(self):
        return self.top==-1
    def push(self,data):
        if not self.isFull():
            self.top+=1
            self.items[self.top]=data
        else:
            print('栈以满，不能入栈')
    def pop(self):
        if not self.isEmpty():
            data=self.items[self.top]
            self.top-=1
            return data
        else:
            print('栈以空，不能出栈！')
            return None
#深度遍历，用堆栈实现
#1.把节点1放入堆栈，如果堆栈不为空一直循环
#2.从堆栈取出一个数（一个节点），访问它（打印），
  #修改访问标记为已访问
#3.获得这个节点所有相邻节点，判断是否访问过，没有则
  #放入堆栈
#4.自动进入下一轮循环
vist=[0]*6
def depthV():
    print('深度遍历')
    a=Stack(100)
    a.push(3)
    while not a.isEmpty():
        b=a.pop()
        if vist[b-1]==0:
            print('V%s'%b),
        vist[b-1]=1
        for i in range(len(vist)):
            if A[b-1][i]!=0 and vist[i]==0:
                a.push(i+1)
#递归深度优先遍历
def depthVdg(id):
    #访问起始点，修改标记位
    print('V%s'%id),
    vist[id-1]=1
    #找到与id节点相邻的而且没有访问过的点，递归
    for i in range(len(vist)):
        if A[id - 1][i] != 0 and vist[i] == 0:
            depthVdg(i+1)
depthVdg(2)
#depthV()
#广度优先遍历
#1.将起始节点放入队列，修改放入标记为已放入，
  # 如果队列不空，一直循环
#2.从队列出来一个节点，访问它，修改访问标记
#3.获得这个节点的所有相邻点，判断（1）是否访问过，
#（2）是否放入队列中，都没有那么把它放入队列。
#自动进入下一轮循环
class Queue(object):
    def __init__(self,max):
        self.max=max
        self.items=[0]*max
        self.head=0
        self.tail=self.head
    def isEmpty(self):
        return self.tail==self.head
    def isFull(self):
        return self.head==(self.tail+1)%self.max
    def inq(self,data):
        if not self.isFull():
            self.items[self.tail]=data
            self.tail=(self.tail+1)%self.max
        else:
            print 'Full'
    def outq(self):
        if not self.isEmpty():
            data=self.items[self.head]
            self.head = (self.head + 1) % self.max
            return data
        else:
            print('Empty')

def broadV():
    print('广度优先遍历')
    #访问标记，放入标记初始值全为0,表示没被访问过
    isln=[0]*6
    vist=[0]*6
    #调用类，s为一个队列
    s=Queue(100)
    a=2
    #a为起始节点进队
    s.inq(a)
    #修改放入标记为为已放入
    isln[a-1]=1
    #如果队列不为空，进行循环
    while not s.isEmpty():
        #b为队列出来的第一个节点
        b=s.outq()
        #打印b
        print('V%s'%b),
        #修改访问标记为已访问
        vist[b-1]=1
        #找b的相邻节点，判断是否访问过，是否放入
        for i in range(len(vist)):
            if A[b-1][i]!=0 and vist[i]==0 \
                and isln[i]==0:
                #队列放入b的相邻节点
                s.inq(i+1)
                #修改放入标记为已放入
                isln[i]=1
#broadV()



