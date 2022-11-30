#-*-coding:utf8-*-
class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkStack(object):
    def __init__(self,top=None):
        self.top=top
    def isEmpty(self):
        return self.top==None
    #push有参数 ，pop没参数但有返回值
    def push(self,data):
        #参照addHead代码
        new=Node(data,self.top)
        self.top=new
    def pop(self):
        if self.isEmpty():
            print('栈为空，不能出栈！')
            return None
        else:
            #参照delHead代码
            ret=self.top.data
            self.top=self.top.next
            return ret
ls=LinkStack()
ls.push(1)
ls.push(2)
ls.push(3)
print(ls.pop())
print(ls.pop())
print(ls.pop())
ls.push('r')
print(ls.pop())