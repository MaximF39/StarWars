import threading
import time


class ThreadBase:

    def __init__(self):
        self.all_func = []

    def start_timer_update(self, func, sec, args=None):
        if not isinstance(args, tuple | None):
            raise NotImplementedError('args is not tuple')
        f_name_thread = self.__get_name(func)
        self.all_func.append(func)
        setattr(self, f_name_thread, threading.Timer(interval=sec, function=func, args=args))
        getattr(self, f_name_thread).start()

    def start_const_update(self, func, time, args:tuple=None):
        if args:
            args = tuple((func, time, *args))
            threading.Thread(target=self.__thread_update, args=args).start()
        else:
            threading.Thread(target=self.__thread_update, args=(func, time)).start()


    def start_update(self, func, *args):
        f_name_thread = self.__get_name(func)
        setattr(self, f_name_thread, threading.Thread(target=func, args=args))
        getattr(self, f_name_thread).start()

    def del_thread_timer(self, func):
        if func in self.all_func:
            getattr(self, f'{func.__name__}_thread').cancel()
            delattr(self, f'{func.__name__}_thread')
            self.all_func.remove(func)
        else:
            raise NotImplemented(" Перепутал переменную? ")

    def alive_thread_timer(self, func):
        return func in self.all_func

    @staticmethod
    def __thread_update(func, time_, args: tuple = None):
        while True:
            threading.Thread(target=func, args=args).start()
            time.sleep(time_)

    @staticmethod
    def __get_name(func):
        return f"{func.__name__}_thread"

