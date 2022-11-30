#-*-coding:utf8-*-
class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkTable(object):
    def __init__(self,head=None,tail=None):
        #初始时链表是个空的，头指针为空
        self.head=head
        self.tail=tail
    def isEmpty(self):
        return self.head==None
    def show(self):
        h=self.head
        while h:
            print(h.data),
            h=h.next
        print('')
    def addHead(self,data):
        new=Node(data,self.head)
        self.head=new
    def addTail(self,data):
        if self.isEmpty():
            return self.addHead(data)
        tail=self.head
        while tail.next:
            tail=tail.next
        tail.next=Node(data)
    def delHead(self):
        if not self.isEmpty():
            self.head=self.head.next
        else:
            print('链表空，不能删除')
    def delTail(self):
        if self.isEmpty():
            print('链表空，不能删除')
            return
        tail = self.head
        parent=tail
        while tail.next:
            parent=tail
            tail = tail.next
        parent.next=None
    def delByIndex(self,index):
        pass
    def delByData(self,data):
        if self.head.data==data:
            #return 之后的代码不执行了
            return self.delHead()
        find=False
        h = self.head
        parent = h
        while h.next:
            parent = h
            h = h.next
            #前面的代码与deltail一样
            if h.data==data:
                find=True
                break
        if find:
            parent.next=h.next
lt=LinkTable()
lt.addHead(1)
lt.addHead(2)
lt.addTail(3)
lt.addTail(4)
lt.delHead()
lt.delTail()
lt.delByData(1)
lt.delByData(3)
lt.delHead()
lt.delTail()
lt.addTail(3)
lt.addTail(4)
lt.addHead(1)
lt.show()