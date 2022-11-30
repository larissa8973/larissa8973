""" Algorithms configured for profiling 
(即在该模块中有可接收profiler探查器作为参数的排序函数算法)"""

""" 基本排序算法 """
def swap(lyst, i, j, profiler):
    """ Exchange the items at position i and j """
    profiler.exchange()                # Count the numbers of exchange if items increase
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

""" 选择排序法 """
def selectionSort(lyst, profiler):
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            profiler.comparison()       # Count the numbers of comparison if items increase
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap(lyst, minIndex, i, profiler)
        i += 1
