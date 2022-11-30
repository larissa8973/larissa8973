#-*-coding:utf8-*-
#lt=[[None]*8]#==[[None,None,None,None,None,None,None],
                 # ]
#[key]*8==[key,key,key,key,key,key,key,key,]
#key->[8,None,None,None,None,None,None]
# lt[0][0]=9
# lt[1][0]=8
# print(lt[0][0])
class Node(object):#链表类
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
head=None#默认头是没有的
def create():#定义链表
    E= Node('E')
    D = Node('D',E)
    C = Node('C', D)  # C.next=D
    B = Node('B', C)
    A = Node('A', B)
    global head
    head=A#头就是A
create()#调用函数
# for i in range(4):
#     print(head.data)
#     head = head.next
# print(head.next.next.data)
# head.next=head.next.next
def show():
    h1 = head
    #h1从头head处开始每次往后移动一个位置，
    #直到变成none，结束
    while h1:#等同于while h1!=None
        pri nt(h1.data),
        h1 = h1.next
    print('')
#要删除哪一个节点，必须找到它的上一个节点！！！
def delTail():
    h=head
    parent=h
    while h.next:
        parent=h
        h=h.next
        #print('%s->%s'%(parent.data,h.data))
    print(parent.data)
    parent.next=None
def deleteByData(data):
    h=head
    parent=h
    while h:
        #parent指向h的上一个结点
        #在h改变之前，让parent指向它之前的位置
        parent=h
        #h指向它的下一个
        h=h.next
        #找到要删除的数据，退出循环
        if h.data==data:
            break
    #print(parent.data)
    #循环退出后，h是要删除的节点
    #parent指向要删除的前一个节点
    parent.next=parent.next.next
def delete(index):
    #任何时候，head头指针都不能改变
    h=head
    #要删除位置index，首先要找到它的前一个
    for i in range(index-2):
        h=h.next
    #修改删除
    h.next=h.next.next
#delete(2)#A-B-D-E
#head=head.next
def addHead(data):
    #把数据data包装成Node new，让new.next-->head
    global head
    new=Node(data,head)
    #把头head移动到第一个new上
    head=new
def addTail(data):
    tail=head
    while tail.next:
        tail=tail.next
    #退出循环后，tail就是尾部
    new=Node(data)
    tail.next=new
addHead('a')
addTail('b')
#deleteByData('D')
show()
show()





