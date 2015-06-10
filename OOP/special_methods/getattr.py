#dynamic __getattr__
class Food():
    def __getattr__ (self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributError('\'Food\' object has no attribute \'%s\'' % attr)


