""" Purpose: Prints the number of calls of a recursive Fabonacci 
and linear fabonacci function with problem size that double """


from counter import Counter

def fib_recursion(n, counter):
    """ Count the number of calls of the Fibonacci Function """
    counter.increment()
    if n < 3:
        return 1
    else:
        return fib_recursion(n - 1, counter) + fib_recursion(n - 2, counter)

def fib_Linear(n, counter):
    """ Count the number of iteration in the Fabonacci fuction """
    sum = 1
    first = 1
    second = 1
    count = 3
    while count <= n:
        counter.increment()
        sum = first + second
        first = second
        second = sum
        count += 1
    return sum

""" Recursion """
print("{0:=^50}".format("Recursion algorithm of Fabonacci"))
problemSize = 2
print("%12s%15s" % ("Problem Size", "Call"))
for count in range(5):
    counter = Counter()
    # The start of the algorithm
    fib_recursion(problemSize, counter)
    # The end of the algorithm
    print("%12s%15s" % (problemSize, counter))      # 返回的是实例化后输出的 unicode string
    problemSize *= 2

""" Linear """
print("{0:=^50}".format("Linear algorithm of Fabonacci"))
problemSize = 2
print("%12s%15s" % ("Problem Size", "Iterations"))
for count in range(5):
    counter = Counter()
    # The start of the algorithm
    fib_Linear(problemSize, counter)
    # The end of the algorithm
    print("%12s%15s" % (problemSize, counter))      # 返回的是实例化后输出的 unicode string
    problemSize *= 2
