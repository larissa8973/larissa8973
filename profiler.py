""" Defines a class for profiling sort algorithms. A Profiler object tracks the list, the numbers of 
comparisons and exchanges, and the running time. The Profiler can also print a trace and can 
create a list of unique or duplicate numbers. """

""" API of Profiler:
p.test(function, lyst=None, size=10, unique=True, comp=True, exch=True, trace=False) 
    -> 用给定的设置运行function并输出结果
p.comparison()
    -> 如果指定了该项，自增比较的次数
p.exchange()
    -> 如果指定了该项，自增交换的次数
p.__str__()
    -> 和str(p)相同，根据该项，返回结果的字符串表示 """

import time
import random

class Profiler(object):
    def test(self, function, lyst=None, size=10, 
            unique=True, comp=True, exch=True, 
            trace=False):
        """ 
        fuction: the algorithm being profiled
        target: the search target if profiling a search
        lyst: allows the caller to use her list
        size: the size of the list, 10 by default
        unique: if True, list contains unique integers
        comp: if True, count comparisons
        exch: if True, count exchanges
        trace: if True, print the list after each exchange

        Run the function with the given attributes and print its profile results
        """
        self._comp = comp
        self._exch = exch
        self._trace = trace
        if lyst != None:
            self._lyst = lyst
        elif unique:
            self._lyst = list(range(1, size+1))
            random.shuffle(self._lyst)
        else:
            self._lyst = []
            for count in range(size):
                self._lyst.append(random.randint(1, size))
        self._exchCount = 0
        self._cmpCount = 0
        self._startClock()
        function(self._lyst, self)
        self._stopClock()
        print(self)

    def exchange(self):
        """ Counts exchanges if on """
        if self._exch:
            self._exchCount += 1
        if self._trace:
            print(self._lyst)

    def comparison(self):
        """ Counts comparison if on """
        if self._comp:
            self._cmpCount += 1

    def _startClock(self):
        """ Record the starting time """
        self._start = time.time()

    def _stopClock(self):
        """ Stop the clock and computes the elapsed time in seconds, to the nearest millisecond """
        self._elapsedTime = round(time.time() - self._start, 3)

    def __str__(self):
        """ Returns the results as a string """
        result = "Problem Size: "
        result += str(len(self._lyst)) + "\n"
        result += "Elapsed time: "
        result += str(self._elapsedTime) + "\n"
        if self._comp:
            result += "Comparison: "
            result += str(self._cmpCount) + "\n"
        if self._exch:
            result += "Exchanges: "
            result += str(self._exchCount) + "\n"
        return result

