from profiler import Profiler
from algorithms import selectionSort
p = Profiler()
p.test(selectionSort)
print("=================================\n")
p.test(selectionSort, size=5, trace=True)
print("=================================\n")
p.test(selectionSort, size=100)
print("=================================\n")
p.test(selectionSort, size=1000)
print("=================================\n")
p.test(selectionSort, size=10000, exch=False, comp=False)
