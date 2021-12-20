from socket import socket
from threading import Thread
from . import Paths
from . import ResourceString
from . import Time
from datetime import datetime
from loguru import logger
from . import ThreadBase
from . import StarWars
from python.Packages.ReadPackages import ReadPackages
from .Packages import PackagesManager
from .Packages.PackageDecoder import PackageDecoder
from .Static.ServerRequest import ServerRequest


class Server(ThreadBase):
    log: None
    time: int
    host: str = '127.0.0.1'
    port: int = 10000
    users: list = []
    server: socket

    def __init__(self):
        Game = StarWars()

    def main(self) -> None:
        self.write_to_log('Запуск сервера', True)
        # тут буит ваш сервер
        self.server = socket()
        self.server.bind((self.host, self.port))
        self.server.listen(1)
        print('server started')
        self.upgrade()

    def upgrade(self):
        self.start_update('accept_socket', 1)
        self.start_update('send_socket', 1)

    @ThreadBase.end_thread
    def connect_new_user(self):
        while True:
            conn, addr = self.server.accept()
            self.users.append(conn)

    @ThreadBase.end_thread
    def accept_socket(self):
        while True:
            for i in range(len(self.users)):
                decoder = PackageDecoder()
                read_packages = ReadPackages()
                decoder.data = self.users[i].recv(16)
                PackageNumberGet: int = decoder.read_int()
                NaN = decoder.read_int()
                NaN = decoder.read_int()
                lenBytes = decoder.read_int()
                read_packages.main(PackageNumberGet, self.users[i].recv(lenBytes))


    @ThreadBase.end_thread
    def send_socket(self):
        def SendPackage(byte_package, id_):
            self.users[id_].send(byte_package)
        while True:
            for i in range(len(self.users)):
                send = PackagesManager()
                SendPackage(send.processPackages(ServerRequest.VERSION), i)
                SendPackage(send.processPackages(ServerRequest.ONLINE), i)
                SendPackage(send.processPackages(ServerRequest.TOP_LIST), i)
                SendPackage(send.processPackages(ServerRequest.TOP_CLANS_LIST), i)
                SendPackage(send.processPackages(ServerRequest.TOP_RATING_LIST), i)  #
                SendPackage(send.processPackages(ServerRequest.WEAPONS_PARAMETERS), i)
                SendPackage(send.processPackages(ServerRequest.AMMOS_PARAMETERS), i)  #
                SendPackage(send.processPackages(ServerRequest.RESOURCE_PARAMETERS), i)  #
                SendPackage(send.processPackages(ServerRequest.ENGINES_PARAMETERS), i)  #
                SendPackage(send.processPackages(ServerRequest.DEVICE_PARAMETERS), i)  #
                SendPackage(send.processPackages(ServerRequest.DROID_PARAMETERS), i)  #
                SendPackage(send.processPackages(ServerRequest.MAP), i)  #
                SendPackage(send.processPackages(ServerRequest.SHIP_PARAMETERS), i)
                SendPackage(send.processPackages(ServerRequest.LOGGED), i)  #
                SendPackage(send.processPackages(ServerRequest.PLAYER), i)  #
                SendPackage(send.processPackages(ServerRequest.PLAYER_SHIP), i)  #
                SendPackage(send.processPackages(ServerRequest.SHIPS_POSITION), i)  #
                SendPackage(send.processPackages(ServerRequest.TO_GAME), i)  #
                SendPackage(send.processPackages(ServerRequest.LOCATION_SYSTEM), i)
                SendPackage(send.processPackages(ServerRequest.ACTIVE_DEVICES), i)
                SendPackage(send.processPackages(ServerRequest.ACTIVE_WEPONS), i)
                SendPackage(send.processPackages(ServerRequest.UPDATE_VALUE, 14, 7), i)
                SendPackage(send.processPackages(ServerRequest.UPDATE_VALUE, 15, 25), i)
                SendPackage(send.processPackages(ServerRequest.ACTIVE_DEVICES), i)
                SendPackage(send.processPackages(ServerRequest.PLAYER_SKILLS_DATA), i)
                SendPackage(send.processPackages(ServerRequest.UPDATE_VALUE, 9, 28906), i)
                SendPackage(send.processPackages(ServerRequest.UPDATE_VALUE, 10, 0), i)
                SendPackage(send.processPackages(ServerRequest.UPDATE_VALUE, 11, 0), i)
                SendPackage(send.processPackages(ServerRequest.UPDATE_VALUE, 14, 7), i)
                SendPackage(send.processPackages(ServerRequest.UPDATE_VALUE, 15, 25), i)
                SendPackage(send.processPackages(ServerRequest.ACTIVE_WEPONS), i)
                SendPackage(send.processPackages(ServerRequest.ACTIVE_DEVICES), i)
                SendPackage(send.processPackages(ServerRequest.CLAN), i)
                SendPackage(send.processPackages(ServerRequest.UPDATE_VALUE, 3, 5903), i)
                SendPackage(send.processPackages(ServerRequest.SHIPS_POSITION), i)
                SendPackage(send.processPackages(ServerRequest.SHIPS_POSITION), i)
                SendPackage(send.processPackages(ServerRequest.SHIPS_STASE), i)
                SendPackage(send.processPackages(ServerRequest.HIDE_SHIP), i)


    @staticmethod
    def write_to_log(p1: str, to_log: bool) -> None:
        if to_log:
            logger.add('log_test.log', format="{time:YYYY-MM-DD HH:mm:test.SSS}, {level}, {message}",
                       rotation="128 KB",
                       compression='zip', encoding='cp1251')
            logger.debug(p1)



def main() -> None:
    test = Server()
    test.write_to_log('Запуск сервера', True)
    test.main()
    input()
    test.del_all_update()
    # test.del_update('accept_socket')
    # test.del_update('send_socket')
    # b.del_update('accept_socket')
    # b.del_update('send_socket')