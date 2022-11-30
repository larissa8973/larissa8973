""" Purpose: Sets a class name counter to package methods using to calc the algorithm """


""" 类的定义 """
class Counter(object):
    """ models a counter """
    # Class variable
    instances = 0
    # Constructor
    def __init__(self):
        """ Sets up the counter """
        Counter.instances += 1
        self.reset()
    # Mutator methods
    def reset(self):
        """ Sets the counter to 0 """
        self._value = 0
    def increment(self, amount = 1):
        """ Adds amount to the counter """
        self._value += amount
    def decrement(self, amount = 1):
        """ Substracts amount to the counter """
        self._value -= amount
    # Accessor methods
    def getValue(self):
        """ Return the counter's value """
        return self._value
    def __str__(self):
        """ Return a string representation of the counter """
        return str(self._value)
    def __eq__(self, other):
        """ Returns True if self equals other of False otherwise """
        if self is other: return True
        if type(self) != type(other): return False
        return self._value == other._value
