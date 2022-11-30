#-*-coding:utf8-*-
#求一个数的阶乘4*3*2*1
def jc(n):
    ret=1
    for i in range(1,n+1):
        ret=ret*i
    return ret
#n!=n*(n-1)!
# jc_dg(n)=n*jc_dg(n-1)
#jc_dg(5)=5*jc_dg(4)  jc_dg(4)=4*jc_dg(3)
#jc_dg(3)=3*jc_dg(2)  jc_dg(2)=2*jc_dg(1)
def jc_dg(n):
    #递归调用的出口
    if n==1:
        return 1
    else:
        # 递归的规律n!=n*(n-1)!
        return n*jc_dg(n-1)
#print(jc_dg(5))#120
def showSjx(n):
    #递归的出口
    if n==1:
        print('*')
    else:
        #递归的规律
        print('*  '*n)
        showSjx(n-1)
#showSjx(6)
# *  *  *  *  *   *
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *

#汉诺塔游戏 通过mid柱子将n个盘子从begin柱子移动到end
def hnt(n,begin,mid,end):
    if n==1:
        print('%s-->%s'%(begin,end))
    else:
        hnt(n-1,begin,end,mid)
        print('%s-->%s' % (begin, end))
        hnt(n-1,mid,begin,end)
hnt(5,'x','y','z')
#斐波拉契
def F(n):
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return F(n-1)+F(n-2)
print(F(20))

