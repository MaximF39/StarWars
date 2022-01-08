from .Packages.PackagesManager import PackagesManager
from .Packages.EntryPac import EntryPac
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
    log: None
    time: int
    host: str = 'localhost'
    port: int = 10010
    users: list = []
    server: socket
    Game: StarWars
    id:int
    id_to_conn = {}


    def __init__(self):
        self.Game = StarWars()
        self.online = 0


    def main(self) -> None:
        server = socket()
        server.bind(('localhost', 10010))
        server.listen(1)
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
        print(d.read_utf()) # don't use
        print(d.read_utf()) # AuthKey
        print(d.read_utf()) # domain
        self.create_player(self.id)
        print('create pack')
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

        for pack in PacMan.processPackages(ServerRequest.VERSION):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.ONLINE):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.TOP_LIST):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.TOP_CLANS_LIST):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.TOP_RATING_LIST):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.WEAPONS_PARAMETERS):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.AMMOS_PARAMETERS):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.RESOURCE_PARAMETERS):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.ENGINES_PARAMETERS):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.DEVICE_PARAMETERS):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.DROID_PARAMETERS):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.MAP):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.SHIP_PARAMETERS):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.LOGGED):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.PLAYER):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.PLAYER_SHIP):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.TO_GAME):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.LOCATION_SYSTEM):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.UPDATE_VALUE, 13):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.UPDATE_VALUE, 9):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.UPDATE_VALUE, 10):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.UPDATE_VALUE, 11):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.UPDATE_VALUE, 14):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.UPDATE_VALUE, 15):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.ACTIVE_WEPONS):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.ACTIVE_DEVICES):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.CLAN):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.UPDATE_VALUE, 3):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.SHIPS_POSITION):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.SHIPS_STASE):
            barray.append(pack)
        for pack in PacMan.processPackages(ServerRequest.HIDE_SHIP):
            barray.append(pack)

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
