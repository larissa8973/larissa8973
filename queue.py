#-*-coding:utf8-*-
#最大空间max，只能存max-1
class Queue(object):
    def __init__(self,max):
        self.__items=[None]*max
        self.__max=max
        #把头尾置与列表最前面
        self.__head=0
        self.__tail=self.__head
    def isFull(self):
        return (self.__tail+1)%self.__max==self.__head
    def isEmpty(self):
        return self.__head==self.__tail
    #如此设计，尾指针指向空间是空的，没数据！！！
    def inq(self,data):
        if not self.isFull():
            # 把数据加到尾部
            self.__items[self.__tail] = data
            # 尾指针往后挪一个
            self.__tail = (self.__tail + 1) % self.__max
        else:
            print('full!')
    #头指针指向的空间是有数据的！！
    def outq(self):
        if not self.isEmpty():
            # 获得头部数据
            ret = self.__items[self.__head]
            # 头指针往后挪一个
            self.__head =(self.__head+1)%self.__max
            return ret
        else:
            print('empty!!!')
            return None
q=Queue(100)
for i in range(99):
    q.inq(9)
for i in range(50):
    q.outq()
for i in range(50):
    q.inq(9)
q.inq(4)
# q.inq(1)
# q.inq(3)
# q.inq(5)
# #
# head=99
# head=(head+1)%100
# print(head)