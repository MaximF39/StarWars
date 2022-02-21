#from test3 import b #ERROR most likely due to a circular import


class a:

    def __init__(self, count):
        self.s = count

    def __pr(self):
        print('hello', self.s)

    def _a__pr(self):
        pass

    def two(self):
        print(hasattr(self, '__pr'))


e = a(33)
print(e.__reduce__())
# e.__reduce_ex__()




