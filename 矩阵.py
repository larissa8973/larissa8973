#-*-coding:utf8-*-
a=[[1, 2, 3, 4, 5],
   [1, 2, 3, 4, 5],
   [1, 2, 3, 4, 5],
   [1, 2, 3, 4, 5],
   [1, 2, 3, 4, 5]]
b=[[0, 2, 3, 4, 5],
   [1, 2, 3, 4, 5],
   [1, 8, 3, 4, 5],
   [1, 2, 3, 4, 5],
   [1, 2, 3, 1, 5]]
def matrxAdd(m1,m2):
    m3=[]
    for i in range(len(m1)):
        m3.append([0]*len(m1))
    #m3 5x5
    for i in range(len(m3)):
        for j in range(len(m3)):
            data=m1[i][j]+m2[i][j]
            m3[i][j]=data
    return m3
def show(matrx):
    for i in range(len(matrx)):
        for j in range(len(matrx)):
            print(matrx[i][j]),
        print('')

# c=matrxAdd(a,b)
# show(a)
# print('------------')
# show(c)
