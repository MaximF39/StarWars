import copy

class test:
    def create_class(self):
        fake = copy.copy(self)
        return fake

class Owner(test):

    def __init__(self):
        print('crate')

    def pr(self):
        print('e')



e = Owner()
s = e.create_class()
s.create_class()
s.pr()