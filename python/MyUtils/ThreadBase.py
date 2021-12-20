import threading


class ThreadBase:
    """
            def __init__(self):
                # ниже функций могут быть вызваны вне класса
                self.start_update('hello', 1) # self.hello будет работать в фоне
                self.del_update('hello') # self.hello перестанет работать

            @ThreadBase.end_thread # ОБЯЗАТЕЛЬНО ОБЯЗАТЕЛЬНО ОБЯЗАТЕЛЬНО
            def hello(self, f):
                # code

            # Нельзя вызывать функцию, если включён цикл, то потеряется управление
            # проверить включен ли цикл или нет можно с помощью
            # hasattr(self, {name_func}_thread_true)
            """
    all_name_func = []

    def end_thread(func):
        def wrapper(self, f=''):
            f = str(func).split()[1].split('.')[-1] + '_thread'
            if hasattr(self, f"{f}_true"):
                func(self)
                getattr(self, f'{f}').run()
            else:
                func(self)

        return wrapper

    def start_update(self, f_name: str, time_sec: float):
        if time_sec == -1:
            time_sec = 10 ** 6
        f_name_thread = f"{f_name}_thread"
        f_name_thread_true = f"{f_name}_thread_true"
        self.all_name_func.append(f_name_thread)
        setattr(self, f_name_thread, threading.Timer(time_sec, getattr(self, f_name)))
        setattr(self, f_name_thread_true, True)
        getattr(self, f_name_thread).start()

    def del_update(self, f: str):
        if not f.split('_')[-1] == 'thread':
            f += '_thread'
        if hasattr(self, f):
            self.all_name_func.remove(f)
            getattr(self, f).cancel()
            delattr(self, f)
            delattr(self, f + '_true')
        else:
            raise NotImplemented(" Перепутал название переменной ")

    def del_all_update(self):
        for i in self.all_name_func.copy():
            self.del_update(i)
