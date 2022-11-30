#-*-coding:utf8-*-
class Stack(object):
    def __init__(self,__max):
        self.__max=__max
        #分配最大空间
        self.__items=[None]*__max
        #栈顶位置
        self.__top=-1
    #判断栈是否满
    def isFull(self):
        return self.__top==self.__max-1
    #判断是否为空
    def isEmpty(self):
        return self.__top==-1
    #入栈
    def push(self,data):
        if not self.isFull():
            # 先把栈顶位置+1
            self.__top += 1
            # 然后把数据放入新栈顶位置
            self.__items[self.__top] = data
        else:
            print('栈已满，不能入栈')

    # 出栈
    def pop(self):
        if not self.isEmpty():
            # 取得栈顶的数据
            data = self.__items[self.__top]
            # 然后修改把栈顶位置-1
            self.__top -= 1
            return data
        else:
            print('栈为空，没数据！')
            return None
# s=Stack(100)
# # for i in range(100):
# #     s.push(22)
#
# s.__max=1
# s.push('A')
# s.push('B')
# s.push('C')

# data=s.pop()
# print(data)
# print(s.pop())
# print(s.pop())