from .Packages.PackagesManager import PackagesManager
import time
import threading
from socket import socket
from loguru import logger
from python.StarWars import StarWars
from python.Packages.ReadPackages import ReadPackages
from .Packages.PackageDecoder import PackageDecoder
from python.Static.Type.ServerRequest import ServerRequest
from python.Class.Chat import Chat
if False:
    from python.Player.Player import Player

class Server:
    time: int
    host: str = 'localhost'
    port: int = 10010
    users: list = []
    server: socket
    Game: StarWars
    id_to_conn = {}
    cnt_listen = 100
    players:list["Player"] = []
    online = 0

    def __init__(self):
        self.Game = StarWars(Chat(self))

    def main(self) -> None:
        server = socket()
        server.bind((self.host, self.port))
        server.listen(self.cnt_listen)
        self.conn, addr = server.accept()
        self.online += 1
        self.Game.update_online(self.online)
        self.get()

    def entry(self):
        print('entry')
        decoder = PackageDecoder()
        decoder.data = self.conn.recv(16)
        PackageNumberGet = decoder.read_int()
        decoder.read_int()
        decoder.read_int()
        lenBytes = decoder.read_int()
        decoder.data = self.conn.recv(lenBytes)
        time.sleep(0.5)
        return self.get_id(decoder.data)

    def get_id(self, data):
        d = PackageDecoder()
        d.data = data
        id_ = int(d.read_utf()) # id
        self.Game.connect_user(id_, self.conn)
        print('Вошёл', id_)
        print('AuthKey', d.read_utf()) # AuthKey
        self.create_player(id_)
        return getattr(self.Game, f"Player_{id_}")

    def create_player(self, id_):
        self.Game.create_player(id_)

    def get(self):
        Player = self.entry()
        self.players.append(Player)
        while True:
            try:
                decoder = PackageDecoder()
                decoder.data = self.conn.recv(16)
                PackageNumberGet = decoder.read_int()
                decoder.read_int() # секунды
                decoder.read_int() # Не известная хрень
                lenBytes = decoder.read_int()
                decoder.data = self.conn.recv(lenBytes)
                my_thread = threading.Thread(target=self.get_package, args=(PackageNumberGet, decoder.data, Player))
                my_thread.start()
            except:
                import main
                main.main()
                exit()

    def get_package(self, pack_number, data, Player):
        ReadPackages(self.Game, Player, pack_number, data)

    @staticmethod
    def write_to_log(p1: str, to_log: bool) -> None:
        if to_log:
            logger.add('log_test.log', format="{time:YYYY-MM-DD HH:mm:ss.SSS}, {level}, {message}",
                       rotation="128 KB",
                       compression='zip', encoding='cp1251')
            logger.debug(p1)


def main() -> None:
    test = Server()
    test.main()
