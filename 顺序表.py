#-*-coding:utf8-*-
lb=[1,2,3,4,5]
lb.append(9)
lb.insert(2,2.3)#插入
del lb[1]#删除
lb[3]=90
#print(lb)
#今天的内容，不能使用列表类的函数，只能通过
#下标索引，实现插入和删除
#插入和删除时要确保，参数位置合理合法
class Array(object):
    def __init__(self,max,list=None):
        #max是列表的最大容量
        self.items=[None]*max
        self.max=max
        #把list的数据放到items中
        if list:
            # 列表的有效数据个数
            self.cnt = len(list)
            for i in range(self.cnt):
                self.items[i] = list[i]
        else:
            self.cnt=0
    #只显示有效数据
    def show(self):
        for i in range(self.cnt):
            print(self.items[i]),
        print('')
    def insert(self,index,object):
        if self.cnt==self.max:
            print('full')
            return
        if 0<=index<=self.cnt:
            # 循环范围从有（效数据长度-1）的位置开始
            # 到index位置结束，往后挪数据
            # rang函数第三个参数-1表示从大到小的范围
            for i in range(self.cnt - 1, index - 1, -1):#右闭左开
                self.items[i + 1] = self.items[i]#索引加一个
            # 把你要插入的数据插入指定位置
            self.items[index] = object
            # 修改有效数据的长度
            self.cnt += 1
        else:
            print('位置非法！')
    def delete(self,index):#删除操作
        if 0<=index<self.cnt:
            for i in range(index + 1, self.cnt):
                self.items[i - 1] = self.items[i]#索引减一个
            self.cnt -= 1
        else:
            print('位置非法！')
li=[0]*100
b=Array(100,li)
b.insert(4,1)
b.show()
b.delete(2)
b.show()
# lt=[4,5,2,7]
# a=Array(100,lt)
# a.show()
# a.insert(4,0)
# a.show()
# a.delete(5)
# a.show()

