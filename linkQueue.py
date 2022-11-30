#-*-coding:utf8-*-
class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkQueue(object):
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail
    def isEmpty(self):
        return self.head==None
    def inq(self,data):
        #空队列在头部添加！！！(addHead)
        if self.isEmpty():
            new=Node(data,self.head)
            self.head=new
            #!!!!让尾部tail也指向这个新的节点!!!
            self.tail=new
        else:
            #队列不为空，尾部添加（比addTail更简单）
            new=Node(data)
            self.tail.next=new
            #将tail移动到最后一个
            self.tail=new
    def outq(self):
        if self.isEmpty():
            print('队列空，不能出队！')
            return None
        else:
            #首先得到头部的数据
            ret=self.head.data
            #将头部删除（delHead）
            self.head=self.head.next
            return ret
lq=LinkQueue()
lq.inq('A')
lq.inq('B')
lq.inq('C')
print(lq.outq())
print(lq.outq())
print(lq.outq())
def dg(n):
    if n==1:
        return 1
    return n*dg(n-1)
a=dg(5)
print(a)