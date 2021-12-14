import threading
from time import sleep


class ThreadBase:
    def __init__(self):
        self.update()
        # raise 'Напиши лучше инит. \nи не забывай, что при работе функций фоном, тебе надо указывать f_name'

    def hello(self, f):
        print("hello")
        self.end_update(f)

    def update(self):
        """
        def __init__(self):
            # ниже функций могут быть вызваны вне класса
            self.start_update('hello') # self.hello будет работать в фоне
            self.del_update('hello') # self.hello перестанет работать

        @end_thread # ОБЯЗАТЕЛЬНО ОБЯЗАТЕЛЬНО ОБЯЗАТЕЛЬНО
        def hello(self, f):
            # code
        """
        # raise 'Чё тоби надо в фоне?'

    def start_update(self, f_name: str):
        f_name_thead = f"{f_name}_thead"
        setattr(self, f_name_thead, threading.Timer(1, eval(f"self.{f_name}"), args=[f_name_thead]))
        eval(f'self.{f_name_thead}').start()

    def end_update(self, f_name_thead: str):
        eval(f'self.{f_name_thead}').run()

    def del_update(self, f: str):
        if f.split('_')[-1] == 'thead':
            eval(f'self.{f}').cancel()
        else:
            eval(f'self.{f}_thead').cancel()


x = ThreadBase()
x.start_update('hello')
sleep(3)
x.del_update('hello_thead')
