from python.Static.TypeStr.ClientRequestStr import ClientRequestStr
import time
import threading
from socket import socket
from loguru import logger
from . import ThreadBase
from . import StarWars
from python.Packages.ReadPackages import ReadPackages
from .Packages import PackagesManager
from .Packages.PackageDecoder import PackageDecoder
from python.Static.Type.ServerRequest import ServerRequest


class Server(ThreadBase):
    log: None
    time: int
    host: str = 'localhost'
    port: int = 10010
    users: list = []
    server: socket
    Game: StarWars

    def __init__(self):
        self.Game = StarWars()

    def main(self) -> None:
        self.write_to_log('Запуск сервера', True)
        self.server = socket()
        self.server.bind((self.host, self.port))
        self.server.listen(1)
        conn, addr = self.server.accept()
        self.users.append(conn)
        self.test()
        # s = PackagesManager(1, self.Game)
        # self.entrance_packages(s)

    b = bytearray()

    def SendPackage(self, byte_package):
        for i in byte_package:
            self.b.append(i)

    def sendAll(self):
        self.Game.create_player(self.id)
        from .Packages.__ReadPackagesServer.main import main
        main(self.b)
        self.users[0].send(self.b)
        self.b = bytearray()

    def entrance_packages(self, Packages_Manager):
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.VERSION))  # VERSION
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.ONLINE, len(self.users)))  # ONLINE
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.TOP_LIST))  # TOP_LIST
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.TOP_CLANS_LIST))  # TOP_CLANS_LIST
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.TOP_RATING_LIST))  # TOP_RATING_LIST
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.WEAPONS_PARAMETERS))  # WEAPONS_PARAMETERS
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.AMMOS_PARAMETERS))  # AMMOS_PARAMETERS
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.RESOURCE_PARAMETERS))  # RESOURCE_PARAMETERS
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.ENGINES_PARAMETERS))  # ENGINES_PARAMETERS
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.DEVICE_PARAMETERS))  # DEVICE_PARAMETERS
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.DROID_PARAMETERS))  # DROID_PARAMETERS
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.MAP))  # MAP
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.SHIP_PARAMETERS))  # SHIP_PARAMETERS
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.LOGGED))  # LOGGED
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.PLAYER))  # PLAYER
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.PLAYER_SHIP))  # PLAYER_SHIP
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.SHIPS_POSITION))  # SHIPS_POSITION
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.TO_GAME))  # TO_GAME
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.LOCATION_SYSTEM))  # LOCATION_SYSTEM
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.ACTIVE_DEVICES))  # ACTIVE_DEVICES
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.ACTIVE_WEPONS))  # ACTIVE_WEPONS
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.UPDATE_VALUE, 14, 7))  # UPDATE_VALUE
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.UPDATE_VALUE, 15, 25))  # UPDATE_VALUE
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.ACTIVE_DEVICES))  # ACTIVE_DEVICES
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.PLAYER_SKILLS_DATA))  # PLAYER_SKILLS_DATA
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.UPDATE_VALUE, 9, 28906))  # UPDATE_VALUE
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.UPDATE_VALUE, 10))  # UPDATE_VALUE
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.UPDATE_VALUE, 11))  # UPDATE_VALUE
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.UPDATE_VALUE, 14, 7))  # UPDATE_VALUE
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.UPDATE_VALUE, 15, 25))  # UPDATE_VALUE
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.ACTIVE_WEPONS))  # ACTIVE_WEPONS
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.ACTIVE_DEVICES))  # ACTIVE_DEVICES
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.CLAN))  # CLAN
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.UPDATE_VALUE, 3, 5903))
        for _ in range(5):
            self.SendPackage(Packages_Manager.processPackages(ServerRequest.SHIPS_POSITION))  # UPDATE_VALUE
            self.SendPackage(Packages_Manager.processPackages(ServerRequest.SHIPS_POSITION))  # SHIPS_POSITION
            self.SendPackage(Packages_Manager.processPackages(ServerRequest.SHIPS_STASE))  # SHIPS_POSITION
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.HIDE_SHIP))
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.SHIPS_POSITION))
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.SHIPS_POSITION))
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.SHIPS_STASE))
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.SHIPS_POSITION))
        self.SendPackage(Packages_Manager.processPackages(ServerRequest.SHIPS_POSITION))
        self.sendAll()
            # while True:
            #     self.SendPackage(self.Packages_Manager.processPackages(ServerRequest.SHIPS_POSITION, id_), conn)

    def test(self):
        a = threading.Thread(target=self.accept_pack)
        a.start()

    def read_login(self, data):
        _loc5_ = PackageDecoder()
        _loc5_.data = data
        data = []
        data.append(_loc5_.read_utf())  # Vk_user_id
        data.append(_loc5_.read_utf())  # don't use
        data.append(_loc5_.read_utf())  # Vk_auth_key
        data.append(_loc5_.read_utf())  # domain
        return data

    def accept_pack(self):
        print('accept')
        while True:
            data = self.users[0].recv(16)
            if data:
                pack_nub_to_str = ClientRequestStr()
                decoder = PackageDecoder()
                decoder.data = data
                PackageNumber, lenBytes = self.default_read_package(decoder)
                if PackageNumber == -2100000001:
                    res = self.read_login(self.users[0].recv(lenBytes))
                    self.id = int(res[0])
                    Packages_Manager = PackagesManager(self.id, self.Game)
                    print("Create", self.id)
                    self.Game.create_player(self.id)
                    a = threading.Thread(target=self.entrance_packages, args=(Packages_Manager, ))
                    a.start()
                else:
                    read_packages = ReadPackages(self.Game, self.id)
                    res = read_packages.main(PackageNumber, self.users[0].recv(lenBytes))
                    print(pack_nub_to_str.get_str(PackageNumber), res)

    def connect_new_user(self):
        while True:
            conn, addr = self.server.accept()
            if conn:
                self.users.append(conn)
                print('connect user', len(self.users))
                break

    @staticmethod
    def default_read_package(decoder):
        PackageNumber: int = decoder.read_int()
        decoder.read_int()
        decoder.read_int()
        lenBytes = decoder.read_int()
        return PackageNumber, lenBytes

    @staticmethod
    def write_to_log(p1: str, to_log: bool) -> None:
        if to_log:
            logger.add('log_test.log', format="{time:YYYY-MM-DD HH:mm:test.SSS}, {level}, {message}",
                       rotation="128 KB",
                       compression='zip', encoding='cp1251')
            logger.debug(p1)


def main() -> None:
    test = Server()
    test.main()
