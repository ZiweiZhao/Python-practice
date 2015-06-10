#__iter__: a special method to iterate through classes

class Fib(object):
    def __init__(self):
        self.a = 0, self.b = 1 ＃initialize two counters
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration();
        return self.a

    def __getitem__(self, n):
        a, b = 1,1,
        for x in range(n):
            a, b = b, a+b
            return a


