from socket import socket
from threading import Thread
from . import Paths
from . import ResourceString
from . import Time
from datetime import datetime
from loguru import logger
from . import ThreadBase

class Server(ThreadBase):
    log: None
    time: int
    host: str = '127.0.0.1'
    port: int = 10000
    clients: list = []
    s: socket

    def main(self) -> None:
        self.write_to_log('Запуск сервера', True)
        # тут буит ваш сервер
        self.s = socket()
        self.s.bind((self.host, self.port))
        self.s.listen(1)
        print('server started')
        self.start_update('accept_socket', -1)
        self.start_update('send_socket', 1)


    @ThreadBase.end_thread
    def accept_socket(self):
        while True:
            pass
            # self.data, self.conn = self.s.recvfrom(10240)
            # if self.conn not in self.clients:
            #     self.clients.append(self.conn)
            #
            # print(self.data)

    @ThreadBase.end_thread
    def send_socket(self):
        # self.conn.send(self.pack)
        print(1)
        # pass


    @staticmethod
    def write_to_log(p1: str, to_log: bool) -> None:
        if to_log:
            logger.add('log_test.log', format="{time:YYYY-MM-DD HH:mm:test.SSS}, {level}, {message}",
                       rotation="128 KB",
                       compression='zip', encoding='cp1251')
            logger.debug(p1)



def main() -> None:
    test = Server()
    # test.write_to_log('Запуск сервера', True)
    test.main()
    input()
    print('del')
    test.del_all_update()
    # test.del_update('accept_socket')
    # test.del_update('send_socket')
    # b.del_update('accept_socket')
    # b.del_update('send_socket')