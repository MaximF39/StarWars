import threading
import time
from datetime import datetime

class MyTime:
    LastTime: float

    def __init__(self):
        self.LastTime = self.Hash()

    def tick(self):
        OldLastTime = self.LastTime
        self.LastTime = self.Hash()
        return self.LastTime - OldLastTime

    @staticmethod
    def Hash() -> float:
        return (datetime.now() - datetime(1, 1, 1)).total_seconds()

class ThreadBase:
    all_func = []

    def start_timer_update(self, func, sec, id_, *args):
        f_name_thread = f"{func.__name__}_thread_{id_}"
        self.all_func.append(func)
        setattr(self, f_name_thread, threading.Timer(interval=sec, function=func, args=args))
        getattr(self, f_name_thread).start()
        # setattr(self, f'{f_name_thread}_delete', threading.Timer(interval=sec, function=self.del_thread_timer, args=(func, id_)))
        # getattr(self, f'{f_name_thread}_delete').start()


    def add_time_timer(self, func, sec, id_, *args):
        f_name_thread = f"{func.__name__}_thread_{id_}"
        getattr(self, f_name_thread).join(sec)
    #     print('sec', type(sec))
    #     getattr(self, f'{f_name_thread}_delete').join(sec)
    #     self.del_thread_timer(func, id_)
    #     self.start_timer_update(func, time, id_, *args)


    def start_update(self, func, *args):
        threading.Thread(target=func, args=args).start()

    def del_thread_timer(self, func, id_):
        if func in self.all_func:
            func_name = f'{func.__name__}_thread_{id_}'
            getattr(self, func_name).cancel()
            delattr(self, func_name)
            # getattr(self, f'{func_name}_delete').cancel()
            # delattr(self, f'{func_name}_delete')
            self.all_func.remove(func)

    def get_alive(self, func, id_):
        if func in self.all_func:
            if hasattr(self, f'{func.__name__}_thread_{id_}'):
                return True
        return False



class test(ThreadBase):

    def start(self, func, sec, id_):
        self.start_timer_update(func, sec, id_)

    def add_time(self, func, sec, id_):
        if self.get_alive(func, id_):
            self.add_time_timer(func, sec, id_)


    # def pr(self):
    #     print('i"m print', e.tick())



# t = test()
# func = t.pr
# id_ = 1
#
#
# e = MyTime()
# t.start(func, 1.01, id_)
# t.add_time(func, 1, id_)
# time.sleep(2)
# for i in t.__dir__():
#     print(i)
import random

# def get_random(cnt_number):
#     for i in range(cnt_number):
#         yield i


# for rand in get_random(5):
#     print(rand)
# g = get_random(5)
# print(next(g))
# print(next(g))
# print(next(g))

# gen = get_random(5)
# print(list(gen))

# i = iter([1, 2, 3])

# print(list(i))
# print(list(i))
# l = [1, 2, 3, 4, 5]
#
# def m(x):
#     return x**2
#
# print(list(map(lambda x: x**2, l)))
# print(list(map(m, l)))
# dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
# print(list(filter(lambda x : x['name'] == 'python', dict_a)))
#

# def t():
#     return iter([1, 2, 3, 4, 4, 'hello'])
#
# for i in t():
#     print(i)

# d = {'main':22}
# if not 'main2' in d:
#     raise NotImplementedError('Ты забыл переменную лох хаха тупой прогер')

# def avg(ranks):
#     assert len(ranks) == 0
#     # assert isinstance(ranks, list)
#     print('hello')
#     return round(sum(ranks)/len(ranks), 2)
#
# print('Debug var', __debug__)
# # python -O test2.py
# ranks = [62, 65, 75]
# print("Среднее значение:", avg(ranks))

# d = {'hello':22}
# d2 = {'hello':22}
# d3 = d
# d3['main'] = 33
# print(d2 == d) # True
# print(d3 is d) # False
# print(d)
# print(d3)



