#special method: __str__
class Food():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Food object (name: %s)' %self.name

    __repr__ = __str__

print (Food ('tuna'))
