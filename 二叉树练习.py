#-*-coding:utf8-*-
class Node(object):
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
class BTree(object):
    def __init__(self,root=None):
        self.root=root
        self.create()
    def create(self):
        p4=Node(4)
        p5=Node(5)
        p6=Node(6)
        p8=Node(8)
        pp5=Node(5,p6,p8)
        p9=Node(9,pp5)
        p2=Node(2,p4,p5)
        p1=Node(1,p2,p9)
        self.root=p1
#打印小于8的数
def show(node):
    #在前序遍历的基础上，判断，然后打印
    if node:
        if node.data<8:
            print(node.data),
        show(node.left)
        show(node.right)
#对树的节点求和（方法1）
sum=0
def get_sum(node):
    if node:
        global sum
        sum+=node.data
        get_sum(node.left)
        get_sum(node.right)
#方法2
def get_sum2(node):
    if node:
        ls=get_sum2(node.left)
        rs=get_sum2(node.right)
        return node.data+ls+rs
    else:
        return 0

#将链式二叉树转换成顺序存储的
A=[0]*15
def putin(node,id):
    #递归退出条件
    if node:
        #递归规律，将根节点放好，再将左右子树
        #按对应位置编号放好
        A[id]=node.data
        putin(node.left,id*2)
        putin(node.right,id*2+1)
#将列表形式（顺序存储）的二叉树变成链式存储
A=[0,'A',0,'B',0,0,'C','D',0,0,0,0,'E']
def create(id):
    if id>len(A)-1 or A[id]==0:
        return None

    #根据id列表下标生成一个根节点
    node=Node(A[id])
    #递归生成左右子树（改变参数）
    leftTree=create(id*2)
    rightTree=create(id*2+1)
    #让根节点把左右子树链接上
    node.left=leftTree
    node.right=rightTree
    #返回这个根节点
    return node
def bianli(node):
    if node:
        print(node.data),
        bianli(node.left)
        bianli(node.right)
# root=create(1)
# bianli(root)
tree=BTree()
print(get_sum2(tree.root))
# putin(tree.root,1)
# print(A)
#show(tree.root)
#get_sum(tree.root)
#print(sum)