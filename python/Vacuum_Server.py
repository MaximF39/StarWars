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
        # read_packages = ReadPackages(self.id)
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

    def send(self):
        time.sleep(1)

    def get_entry_pack(self):
        PacMan = PackagesManager(self.id, self.Game)

        PacMan.processPackages(ServerRequest.VERSION)  # VERSION
        PacMan.processPackages(ServerRequest.ONLINE)  # ONLINE
        PacMan.processPackages(ServerRequest.TOP_LIST)  # TOP_LIST
        PacMan.processPackages(ServerRequest.TOP_CLANS_LIST)  # TOP_CLANS_LIST
        PacMan.processPackages(ServerRequest.TOP_RATING_LIST)  # TOP_RATING_LIST
        PacMan.processPackages(ServerRequest.WEAPONS_PARAMETERS)  # WEAPONS_PARAMETERS
        PacMan.processPackages(ServerRequest.AMMOS_PARAMETERS)  # AMMOS_PARAMETERS
        PacMan.processPackages(ServerRequest.RESOURCE_PARAMETERS)  # RESOURCE_PARAMETERS
        PacMan.processPackages(ServerRequest.ENGINES_PARAMETERS)  # ENGINES_PARAMETERS
        PacMan.processPackages(ServerRequest.DEVICE_PARAMETERS)  # DEVICE_PARAMETERS
        PacMan.processPackages(ServerRequest.DROID_PARAMETERS)  # DROID_PARAMETERS
        PacMan.processPackages(ServerRequest.MAP)  # MAP
        PacMan.processPackages(ServerRequest.SHIP_PARAMETERS)  # SHIP_PARAMETERS
        PacMan.processPackages(ServerRequest.LOGGED)  # LOGGED
        PacMan.processPackages(ServerRequest.PLAYER)  # PLAYER
        PacMan.processPackages(ServerRequest.PLAYER_SHIP)  # PLAYER_SHIP
        PacMan.processPackages(ServerRequest.TO_GAME)  # TO_GAME
        PacMan.processPackages(ServerRequest.LOCATION_SYSTEM)  # LOCATION_SYSTEM
        PacMan.processPackages(ServerRequest.UPDATE_VALUE, 13)  # UPDATE_VALUE
        PacMan.processPackages(ServerRequest.UPDATE_VALUE, 9)  # UPDATE_VALUE
        PacMan.processPackages(ServerRequest.UPDATE_VALUE, 10)  # UPDATE_VALUE
        PacMan.processPackages(ServerRequest.UPDATE_VALUE, 11)  # UPDATE_VALUE
        PacMan.processPackages(ServerRequest.UPDATE_VALUE, 14)  # UPDATE_VALUE
        PacMan.processPackages(ServerRequest.UPDATE_VALUE, 15)  # UPDATE_VALUE
        PacMan.processPackages(ServerRequest.ACTIVE_WEPONS)  # ACTIVE_WEPONS
        PacMan.processPackages(ServerRequest.ACTIVE_DEVICES)  # ACTIVE_DEVICES
        PacMan.processPackages(ServerRequest.CLAN)  # CLAN
        PacMan.processPackages(ServerRequest.UPDATE_VALUE, 3) # s
        PacMan.processPackages(ServerRequest.SHIPS_POSITION)  # SHIPS_POSITION
        PacMan.processPackages(ServerRequest.SHIPS_STASE)  # SHIPS_POSITION
        PacMan.processPackages(ServerRequest.HIDE_SHIP) # s

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
