#-*-coding:utf8-*-
from stack import Stack
s='((1+2)*(3+4))'
def isOk():
    sk = Stack(100)
    for c in s:
        if c == '(':
            sk.push(c)
        if c == ')':
            d=sk.pop()
            if d==None:
                return False
    return sk.isEmpty()
if isOk():
    print('ok')
else:
    print('not ok')
#碰到一个（ push ，碰到一个）pop
#isEmpty()  中途出现pop None不匹配