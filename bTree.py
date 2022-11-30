#-*-coding:utf8-*-
class Node(object):
    def __init__(self,data,left=None,right=None):
        self.left=left
        self.data=data
        self.right=right
class BTree(object):
    def __init__(self,root=None):
        self.root=root
        self.create()
        self.num=0
    def create(self):

        G=Node('G')
        H=Node('H')
        D=Node('D',None,G)
        B=Node('B',D,None)
        F=Node('F',H,None)
        E=Node('E')
        C=Node('C',E,F)
        A=Node('A',B,C)
        self.root=A
    #node是二叉树的根节点
    def preOrder(self,node):
        #node==None就是递归的出口（什么都不做）
        if node:
            #遍历顺序就是递归的规律
            print(node.data),
    #遍历左子树（就是以左孩子为新的根节点进行遍历）
            self.preOrder(node.left)
            self.preOrder(node.right)
    def inOrder(self,node):
        if node:
            self.inOrder(node.left)
            print(node.data),
            self.inOrder(node.right)
    #求节点的数目
    def count(self,node):
        if node:
            self.count(node.left)
            self.num+=1
            self.count(node.right)
    #求树的高度
    #思路，
    #（递归退出条件），根节点为(node==)None，高度为0（return 0）
    # （递归规律）求左子树的高度和右子树的高度，取最大值+1
    def hight(self,node):
        if node==None:
            return 0
        else:
            lheiht=self.hight(node.left)
            rheiht=self.hight(node.right)
            max=lheiht
            if rheiht>lheiht:
                max=rheiht
            return max+1
tree=BTree()
#print(E.data)
# tree.preOrder(tree.root)
# print('')
# tree.inOrder(tree.root)
#tree.count(tree.root)
# print(tree.num)
