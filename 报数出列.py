#-*-coding:utf8-*-
class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
head=None
def createLink(num):
    global head
    tail=None
    for n in range(1,num+1):
        if n==1:
            new=Node(1)
            head=new
            tail=new
        elif n==num:
            # 参照addTail
            new = Node(n)
            tail.next = new
            tail = new
            #将最后一个节点的next指向头部
            tail.next=head
        else:
            #参照addTail
            new=Node(n)
            tail.next=new
            tail=new
createLink(12)
def show():
    h = head
    for i in range(30):
        print('%s->' % h.data),
        h = h.next
def count(num):
    global head
    #循环退出条件head==head.next，head就是最后一个了
    while head!=head.next:
        parent=head
        #报数num，循环num-1次，每次把head往后移动一个
        for i in range(num-1):
            #parent用来记录head的上一个节点
            #便于删除head
            parent = head
            head=head.next
        #for循环退出，及报数一轮，head指向报数为num
        #那个人，要把他从链表删除
        parent.next=head.next
        #让head指向下一轮报数的新的起点
        head=parent.next
    return head
print count(8).data
