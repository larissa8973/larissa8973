""" 搜索最小值 """
def indexOfMin(lyst):
    """ Returns the index of minimum item """
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex

""" 顺序搜索一个列表 """
def sequentialSearch(target, lyst):
    """ Returns the position of the target in the lyst if found,
    or -1 otherwise """
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1

""" 有序列表的二叉搜索(相似于折半查找法) """
def binarySearch(target, sorrtedLyst):
    left = 0
    right = len(sorrtedLyst) - 1
    while left < right:
        midpoint = (left + right) // 2
        if target == sorrtedLyst[midpoint]:
            return midpoint
        elif target < sorrtedLyst[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1

""" 比较数据项 """
class SavingAccount(object):
    """ This class represents a saving accout with the owner's
    name, PIN, and balance """
    def __init__(self, name, pin, balance=0.0):
        self._name = name 
        self._pin = pin
        self._balance = balance
    def __lt__(self, other):    # 相当于使用__str__方法一样，对name进行比较
        return self._name < other._name

s1 = SavingAccount("Larissa", "0100", 0)
print(s1)
s2 = SavingAccount("Ken", "0101", 60)
# s3 = SavingAccount("Larissa", "0100", 0)   # 返回结果错误
s3 = s1
print("s1 < s2 : ", s1 < s2)
print("s1 > s2 : ", s1 > s2)
print("s1 == s2 : ", s1 == s2)
print("s1 == s3 : ", s1 == s3)

""" 基本排序算法 """
def swap(lyst, i, j):
    """ Exchange the items at position i and j """
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

print("{0:=^30}".format("选择排序法"))
""" 选择排序法:最小的前移，其复杂度为O(n^2) """
def selectionSort(lyst):
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i)
        i += 1
        print("Round【%d】" % i)
        for k in range(len(lyst)):
            print("%d " % lyst[k], end="")
        print("\n")
    # return lyst

s1 = selectionSort([32, 12, 41, 11, 5])
print(type(s1))
# for i in range(len(s)):
#     print("%d " % s[i])

print("{0:=^30}".format("冒泡排序法"))
""" 冒泡排序法:最大的沉底，其复杂度为O(n^2) """
def bubbleSort(lyst):
    n = len(lyst)
    while n > 1:
        i = 1
        while i < n:
            if lyst[i] < lyst[i-1]:
                swap(lyst, i ,i-1)
            i += 1
        n -= 1
        for k in range(len(lyst)):
            print("%d " % lyst[k], end="")
        print("\n")

s2 = bubbleSort([32, 12, 41, 11, 5])

print("{0:=^30}".format("插入排序法"))
""" 插入排序法:最大的沉底，其复杂度为O(n^2) """
def insertionSort(lyst):
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert
        i += 1
        for k in range(len(lyst)):
            print("%d " % lyst[k], end="")
        print("\n")

s3 = insertionSort([32, 12, 41, 11, 5])

""" 快速排序法:建立基准点和边界，将基准点放在最后与边界形成排序区间，每遍历一轮将小的数与第一项交换并前移边界, 
    最坏的情况下，其复杂度为O(n^2)，使用递归后是O(n)"""
print("{0:=^30}".format("快速排序法"))
def paritition(lyst, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # Exchange the pivot item and boundary item
    swap(lyst, right, boundary)
    return boundary

def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = paritition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation - 1)
        quicksortHelper(lyst, pivotLocation + 1, right)

def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst) - 1)
    for k in range(len(lyst)):
        print("%d " % lyst[k], end="")
    print("\n")

s4 = quicksort([32, 12, 41, 11, 5])

""" 合并排序法:用了递归、分而治之的策略突破复杂度为O(n^2)。
在一个列表中间分割成左右子列表，递归排序在合并，直至子列表不能分割为止 """
print("{0:=^30}".format("合并排序法"))
from numpy import array

""" To divdie into several sublists """
def mergeSortHelper(lyst, copyBuffer, low, high):
    # copyBuffer    temporary space needed during merge
    # low, high     bounds of sunblist
    # midddle       midpoint of sublist
    if low < high:
        middle = (low + high) // 2
        mergeSortHelper(lyst, copyBuffer, low, middle)
        mergeSortHelper(lyst, copyBuffer, middle+1, high)
        merge(lyst, copyBuffer, low, middle, high)

""" To sort all the sublists in order and return to one list """
def mergeSort(lyst):
    # copyBuffer temporary space needed during merge
    copyBuffer = array(len(lyst))
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst)-1)

""" Connact two sorted arrays into one list """
def merge(lyst, copyBuffer, low, middle, high):
    # Initialize i1 and i2 to the first items in each sublist
    i1 = low
    i2 = middle + 1
    # Interleave items from the sublist into the copyBuffer in such a way that order is maintained
    for i in range(low, high+1):
        if i1 > middle:
            copyBuffer[i] = lyst[i2]    # First sublist exhausted
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = lyst[i1]    # Second sublist exhausted
            i1 += 1
        elif lyst[i1] < lyst[i2]:
            copyBuffer[i] = lyst[i1]    # Item in the first sublist 
            i1 += 1
        else:
            copyBuffer[i] = lyst[i2]    # Item in the second sublist 
            i2 += 1
    for i in range(low, high+1):
        lyst[i] = copyBuffer[i]     # Copy sorted items back to proper position in lyst

l = [38]
l1 = mergeSort(l)
print(type(l1))

""" 早期的swap函数实现 """
import random
def paritition(lyst, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # Exchange the pivot item and boundary item
    swap(lyst, right, boundary)
    return boundary

def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = paritition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation - 1)
        quicksortHelper(lyst, pivotLocation + 1, right)

def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst) - 1)

def main(size = 20, sort = quicksort):
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size+1))
    print(lyst)
    sort(lyst)
    print(lyst)

if __name__ == "__main__":
    main()
