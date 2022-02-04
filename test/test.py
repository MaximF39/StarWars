#from test3 import b #ERROR most likely due to a circular import

if False:
    from test3 import b

class a:

    def __init__(self):
        pass

    def pr(self):
        print("hello")

    def pr2(self, b2:"b"):
        print(b2.text)



