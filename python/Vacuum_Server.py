import time
import threading
from socket import socket
from loguru import logger
from python.StarWars import StarWars
from python.Packages.ReadPackages import ReadPackages
from .DataBase.Database import DataBase
from .Packages.PackageDecoder import PackageDecoder
from python.Utils.ThreadBase import ThreadBase
from python.Class.Chat import Chat
from python.Static.cfg import cfg_server
if False:
    from python.Player.Player import Player

@final
class Server(ThreadBase):
    time: int
    host: str = cfg_server.host
    port: int = cfg_server.port
    server: socket
    Game: StarWars
    cnt_listen = 100
    online = 0

    def __init__(self):
        ThreadBase.__init__(self)
        self.users: list = []
        self.players:list["Player"] = []
        self.id_to_conn = {}
        self.conn_to_id = {}
        self.DB = DataBase()
        self.Game = StarWars(Chat(self))

    def main(self) -> None:
        self.server = socket()
        self.server.bind((self.host, self.port))
        self.server.listen(self.cnt_listen)
        self.wait_user()

    def wait_user(self):
        try:
            while True:
                conn, addr = self.server.accept()
                if conn:
                    ThreadBase.start_update(self, self.entry_user, conn)
        except Exception as e:
            print(10 * '\n', e)
            print("Отключаю сервер")

    def entry_user(self, conn):
        self.add_online()
        Player = self.authorisation_package(conn)
        self.players.append(Player)
        self.get_packages(conn)

    def add_online(self):
        self.__update_online(1)

    def remove_online(self):
        self.__update_online(-1)

    def __update_online(self, __value):
        self.online += __value

    def authorisation_package(self, conn):
        print('authorisation_package')
        PackageNumberGet, lenBytes = self.__default_get_pakage(conn)
        time.sleep(0.5)
        login, password = ReadPackages.login(lenBytes)
        id_ = self.DB.get_user_id(login, password)
        if id_:
            self.connect_user(id_, conn)
            print('Логин', login)
            print('Пароль', password)
            self.create_player(id_)
            return getattr(self.Game, f"Player_{id_}")

    def connect_user(self, id_, conn):
        self.id_to_conn[id_] = conn
        self.conn_to_id[conn] = id_

    @staticmethod
    def __default_get_pakage(conn):
        decoder = PackageDecoder()
        decoder.data = conn.recv(16)
        PackageNumberGet = decoder.read_int()
        decoder.read_int()
        decoder.read_int()
        lenBytes = decoder.read_int()
        return PackageNumberGet, lenBytes

    def get_packages(self, conn):
        while True:
            try:
                data = conn.recv(16)
                PackageNumberGet, lenBytes = self.__default_get_pakage(data)
                data = conn.recv(lenBytes)
                threading.Thread(target=self.get_package, args=(PackageNumberGet, data, Player)).start()
            except Exception as e:
                print("ERROR", e)
                self.exit_user(conn)
                print(f'Пользователь с {self.conn_to_id[conn]} id вышел')
                exit()

    def exit_user(self, conn):
        id_ = self.conn_to_id[conn]
        delattr(self.Game, f"Player_{id_}")
        conn.close()

    def get_package(self, pack_number, data, Player):
        ReadPackages(self.Game, Player, pack_number, data)

    @staticmethod
    def write_to_log(p1: str, to_log: bool) -> None:
        if to_log:
            logger.add('log_test.log', format="{time:YYYY-MM-DD HH:mm:ss.SSS}, {level}, {message}",
                       rotation="128 KB",
                       compression='zip', encoding='cp1251')
            logger.debug(p1)

    def create_player(self, id_):
        self.Game.create_player(id_)

def main() -> None:
    test = Server()
    test.main()
