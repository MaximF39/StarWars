from datetime import datetime

from threading import Thread

def myPrint(*args):
    print(datetime.now(), args)

myPrint(1, 2, 3, [1, 2, 3], {'1':1, '2':2})
