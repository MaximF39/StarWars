from .Packages.PackagesManager import PackagesManager
# from python.Packages.PackagesEntry import PackagesEntry
import time
import threading
from socket import socket
from loguru import logger
from . import ThreadBase
from . import StarWars
from python.Packages.ReadPackages import ReadPackages
from .Packages.PackageDecoder import PackageDecoder
from python.Static.Type.ServerRequest import ServerRequest


class Server(ThreadBase):
    time: int
    host: str = 'localhost'
    port: int = 10010
    users: list = []
    server: socket
    Game: StarWars
    id_to_conn = {}
    cnt_listen = 1

    def __init__(self):
        self.Game = StarWars()
        self.online = 0


    def main(self) -> None:
        server = socket()
        server.bind((self.host, self.port))
        server.listen(self.cnt_listen)
        self.conn, addr = server.accept()
        self.online += 1
        self.Game.update_online(self.online)
        my_thread = threading.Thread(target=self.get)
        my_thread.start()

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
        self.get_id(decoder.data)

    def get_id(self, data):
        d = PackageDecoder()
        d.data = data
        self.id = int(d.read_utf()) # id
        self.Game.connect_user(self.id, self.conn)
        print('Вошёл', self.id)
        print('AuthKey', d.read_utf()) # AuthKey
        self.create_player(self.id)
        self.get_entry_pack()

    def create_player(self, id_):
        self.Game.create_player(self.id)

    def get(self):
        self.entry()
        while True:
            try:
                decoder = PackageDecoder()
                decoder.data = self.conn.recv(16)
                PackageNumberGet = decoder.read_int()
                decoder.read_int() # секунды
                decoder.read_int() # Не известная хрень
                lenBytes = decoder.read_int()
                decoder.data = self.conn.recv(lenBytes)
                my_thread = threading.Thread(target=self.get_package, args=(PackageNumberGet, decoder.data))
                my_thread.start()
            except:
                import main
                main.main()
                exit()

    def get_package(self, pack_number, data):
        ReadPackages(self.Game, self.id, pack_number, data)

    def get_entry_pack(self):
        PacMan = PackagesManager(self.id, self.Game)
        barray = bytearray()
        entry_packs = [
            ServerRequest.VERSION,
            ServerRequest.ONLINE,
            ServerRequest.TOP_LIST,
            ServerRequest.TOP_CLANS_LIST,
            ServerRequest.TOP_RATING_LIST,
            ServerRequest.WEAPONS_PARAMETERS,
            ServerRequest.AMMOS_PARAMETERS,
            ServerRequest.RESOURCE_PARAMETERS,
            ServerRequest.ENGINES_PARAMETERS,
            ServerRequest.DEVICE_PARAMETERS,
            ServerRequest.DROID_PARAMETERS,
            ServerRequest.MAP,
            ServerRequest.SHIP_PARAMETERS,
            ServerRequest.LOGGED,
            ServerRequest.PLAYER,
            ServerRequest.PLAYER_SHIP,
            ServerRequest.TO_GAME,
            ServerRequest.LOCATION_SYSTEM,
            ServerRequest.ACTIVE_WEPONS,
            ServerRequest.ACTIVE_DEVICES,
            ServerRequest.CLAN,
            ServerRequest.SHIPS_POSITION,
            ServerRequest.SHIPS_STASE,
            ServerRequest.HIDE_SHIP,
            ]
        update_value = [
    (ServerRequest.UPDATE_VALUE, 3),
    (ServerRequest.UPDATE_VALUE, 13),
    (ServerRequest.UPDATE_VALUE, 9),
    (ServerRequest.UPDATE_VALUE, 10),
    (ServerRequest.UPDATE_VALUE, 11),
    (ServerRequest.UPDATE_VALUE, 14),
    (ServerRequest.UPDATE_VALUE, 15),
            ]

        for pack in entry_packs:
            for bytes_pack in PacMan.processPackages(pack):
                barray.append(bytes_pack)
        for pack in update_value:
            for bytes_pack in PacMan.processPackages(*pack):
                barray.append(bytes_pack)

        self.Game.id_to_conn[self.id].send(barray)

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
