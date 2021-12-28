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
        my_thread = threading.Thread(target=self.send)
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
        my_thread = threading.Thread(target=self.get_id, args=(decoder.data,))
        my_thread.start()

    def get_id(self, data):
        d = PackageDecoder()
        d.data = data
        self.id = int(d.read_utf()) # id
        self.Game.connect_user(self.id, self.conn)
        print('get', self.id)
        print(d.read_utf()) # don't use
        print(d.read_utf()) # AuthKey
        print(d.read_utf()) # domain
        self.create_player(self.id)
        print('create pack')
        self.pack = self.get_entry_pack

    def create_player(self, id_):
        self.Game.create_player(self.id)


    def get(self):
        self.entry()
        # read_packages = ReadPackages(self.id)
        while True:
            decoder = PackageDecoder()
            decoder.data = self.conn.recv(16)
            PackageNumberGet = decoder.read_int()
            decoder.read_int() # секунды
            decoder.read_int() # Не известная хрень
            lenBytes = decoder.read_int()
            decoder.data = self.conn.recv(lenBytes)
            my_thread = threading.Thread(target=self.get_package, args=(PackageNumberGet, decoder.data))
            my_thread.start()

    def get_package(self, pack_number, data):
        ReadPackages(self.Game, self.id, pack_number, data)

    def send(self):
        time.sleep(1)
        self.conn.send(self.pack)

    @property
    def get_entry_pack(self):
        Entry_Pac = EntryPac(self.id, self.Game)
        PacMan = PackagesManager(self.id, self.Game)

        b = bytearray()
        Player = getattr(self.Game, f'Player_{self.id}')
        def add_bytes(bytes_pack):
            for i in bytes_pack:
                b.append(i)
        add_bytes(Entry_Pac.processPackages(ServerRequest.VERSION))  # VERSION
        add_bytes(Entry_Pac.processPackages(ServerRequest.ONLINE))  # ONLINE
        add_bytes(Entry_Pac.processPackages(ServerRequest.TOP_LIST))  # TOP_LIST
        add_bytes(Entry_Pac.processPackages(ServerRequest.TOP_CLANS_LIST))  # TOP_CLANS_LIST
        add_bytes(Entry_Pac.processPackages(ServerRequest.TOP_RATING_LIST))  # TOP_RATING_LIST
        add_bytes(Entry_Pac.processPackages(ServerRequest.WEAPONS_PARAMETERS))  # WEAPONS_PARAMETERS
        add_bytes(Entry_Pac.processPackages(ServerRequest.AMMOS_PARAMETERS))  # AMMOS_PARAMETERS
        add_bytes(Entry_Pac.processPackages(ServerRequest.RESOURCE_PARAMETERS))  # RESOURCE_PARAMETERS
        add_bytes(Entry_Pac.processPackages(ServerRequest.ENGINES_PARAMETERS))  # ENGINES_PARAMETERS
        add_bytes(Entry_Pac.processPackages(ServerRequest.DEVICE_PARAMETERS))  # DEVICE_PARAMETERS
        add_bytes(Entry_Pac.processPackages(ServerRequest.DROID_PARAMETERS))  # DROID_PARAMETERS
        add_bytes(Entry_Pac.processPackages(ServerRequest.MAP))  # MAP
        add_bytes(Entry_Pac.processPackages(ServerRequest.SHIP_PARAMETERS))  # SHIP_PARAMETERS
        add_bytes(Entry_Pac.processPackages(ServerRequest.LOGGED))  # LOGGED
        add_bytes(Entry_Pac.processPackages(ServerRequest.PLAYER))  # PLAYER
        add_bytes(Entry_Pac.processPackages(ServerRequest.PLAYER_SHIP))  # PLAYER_SHIP
        add_bytes(Entry_Pac.processPackages(ServerRequest.TO_GAME))  # TO_GAME
        add_bytes(Entry_Pac.processPackages(ServerRequest.LOCATION_SYSTEM))  # LOCATION_SYSTEM
        add_bytes(Entry_Pac.processPackages(ServerRequest.UPDATE_VALUE, 13, Player.bonus))  # UPDATE_VALUE
        add_bytes(Entry_Pac.processPackages(ServerRequest.UPDATE_VALUE, 9, Player.cash))  # UPDATE_VALUE
        add_bytes(Entry_Pac.processPackages(ServerRequest.UPDATE_VALUE, 10, Player.ControlUsed))  # UPDATE_VALUE
        add_bytes(Entry_Pac.processPackages(ServerRequest.UPDATE_VALUE, 11, Player.ControlLeft))  # UPDATE_VALUE
        add_bytes(Entry_Pac.processPackages(ServerRequest.UPDATE_VALUE, 14, 15))  # UPDATE_VALUE
        add_bytes(Entry_Pac.processPackages(ServerRequest.UPDATE_VALUE, 15, 25))  # UPDATE_VALUE
        add_bytes(Entry_Pac.processPackages(ServerRequest.ACTIVE_WEPONS))  # ACTIVE_WEPONS
        add_bytes(Entry_Pac.processPackages(ServerRequest.ACTIVE_DEVICES))  # ACTIVE_DEVICES
        add_bytes(Entry_Pac.processPackages(ServerRequest.CLAN))  # CLAN
        add_bytes(Entry_Pac.processPackages(ServerRequest.UPDATE_VALUE, 3, Player.point))
        add_bytes(Entry_Pac.processPackages(ServerRequest.SHIPS_POSITION))  # SHIPS_POSITION
        add_bytes(Entry_Pac.processPackages(ServerRequest.SHIPS_STASE))  # SHIPS_POSITION
        add_bytes(Entry_Pac.processPackages(ServerRequest.HIDE_SHIP))
        from .Packages.__ReadPackagesServer.main import main
        main(b)
        return b

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
