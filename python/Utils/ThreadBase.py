import threading


class ThreadBase:
    all_func = []

    def start_timer_update(self, func, sec, args=None):
        if not isinstance(args, tuple | None):
            raise NotImplementedError('args is not tuple')
        f_name_thread = f"{func.__name__}_thread"
        self.all_func.append(func)
        setattr(self, f_name_thread, threading.Timer(interval=sec, function=func, args=args))
        getattr(self, f_name_thread).start()

    def start_update(self, func, *args):
        f_name_thread = f"{func.__name__}_thread"
        self.all_func.append(func)
        setattr(self, f_name_thread, threading.Thread(target=func, args=args))
        getattr(self, f_name_thread).start()

    def del_thread_timer(self, func):
        if func in self.all_func:
            getattr(self, f'{func.__name__}_thread').cancel()
            delattr(self, f'{func.__name__}_thread')
            self.all_func.remove(func)
        else:
            raise NotImplemented(" Перепутал переменную? ")

