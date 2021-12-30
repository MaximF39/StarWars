import copy
from time import sleep
import multiprocessing
import threading

class e:

    def __init__(self, text):
        self.text = text
        self.t()

    def t(self):
        print(self.text)

s = e('hello')

g = copy.deepcopy(s)

g.text = 'bad'
g.t()

s.t()

