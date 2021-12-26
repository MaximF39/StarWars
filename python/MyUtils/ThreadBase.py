import threading


class ThreadBase:
    all_func = []

    def start_timer_update(self, func, sec, *args):
        f_name_thread = f"{func.__name__}_thread"
        f_name_thread_true = f"{func.__name__}_thread_true"
        self.all_func.append(f_name_thread)
        setattr(self, f_name_thread, threading.Timer(sec, func, args=args))
        setattr(self, f_name_thread_true, True)
        getattr(self, f_name_thread).start()

    def start_update(self, func, *args):
        f_name_thread = f"{func.__name__}_thread"
        self.all_func.append(f_name_thread)
        setattr(self, f_name_thread, threading.Thread(func, args=args))
        getattr(self, f_name_thread).start()

    def del_update(self, func):
        if func in self.all_func:
            getattr(self, f'{func.__name__}_thread').cancel()
            delattr(self, f'{func.__name__}_thread')
            self.all_func.remove(func)
        else:
            raise NotImplemented(" Перепутал переменную? ")

    def del_all_update(self):
        for func in self.all_func:
            getattr(self, f'{func.__name__}_thread').cancel()
            delattr(self, f'{func.__name__}_thread')
            self.all_func.remove(func)
