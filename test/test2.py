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


    def pr(self):
        print('i"m print', e.tick())



t = test()
func = t.pr
id_ = 1


e = MyTime()
t.start(func, 1.01, id_)
t.add_time(func, 1, id_)
# time.sleep(2)
# for i in t.__dir__():
#     print(i)


