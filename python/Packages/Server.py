from python.Static.ServerRequest import ServerRequest
# from python.Static.ClientRequest import ClientRequest
import threading
from socket import socket
from PackageCreator import PackageCreator
from PackageDecoder import PackageDecoder
from ReadPackages import ReadPackages
from PackagesManager import PackagesManager

server = socket()
serverThread = threading.Thread()
users = []


def ConnectNewUser():
    while True:
        conn, addr = server.accept()
        users.append(conn)
        print("new user been connected!")


def decode_pack():
    pass


def StartServer():
    server.bind(('localhost', 10000))
    server.listen(1)
    serverThread = threading.Thread(target=ConnectNewUser)
    serverThread.start()
    print("Server is started")
    read_packes = ReadPackages()
    while True:
        for i in range(len(users)):
            decoder = PackageDecoder()
            decoder.data = users[i].recv(16)
            PackageNumberGet: int = decoder.read_int()
            NaN = decoder.read_int()
            NaN = decoder.read_int()
            lenBytes = decoder.read_int()
            packages = read_packes.main(PackageNumberGet, users[i].recv(lenBytes))
            print(PackageNumberGet, packages)
            send = PackagesManager()
            # SendPackage(send.processPackages(ServerRequest.FLASH_CONNECT_REQUEST), i)  #
            SendPackage(send.processPackages(ServerRequest.VERSION), i)
            SendPackage(send.processPackages(ServerRequest.ONLINE, 200), i)
            SendPackage(send.processPackages(ServerRequest.TOP_LIST), i)
            SendPackage(send.processPackages(ServerRequest.TOP_CLANS_LIST), i)
            SendPackage(send.processPackages(ServerRequest.TOP_RATING_LIST), i) #
            SendPackage(send.processPackages(ServerRequest.WEAPONS_PARAMETERS), i)
            SendPackage(send.processPackages(ServerRequest.AMMOS_PARAMETERS), i) #
            SendPackage(send.processPackages(ServerRequest.RESOURCE_PARAMETERS), i) #
            SendPackage(send.processPackages(ServerRequest.ENGINES_PARAMETERS), i) #
            SendPackage(send.processPackages(ServerRequest.DEVICE_PARAMETERS), i) #
            SendPackage(send.processPackages(ServerRequest.DROID_PARAMETERS), i) #
            SendPackage(send.processPackages(ServerRequest.MAP), i) #
            SendPackage(send.processPackages(ServerRequest.SHIP_PARAMETERS), i)
            SendPackage(send.processPackages(ServerRequest.LOGGED), i) #
            SendPackage(send.processPackages(ServerRequest.PLAYER), i)  #
            SendPackage(send.processPackages(ServerRequest.TO_GAME), i)  #
            # SendPackage(send.processPackages(ServerRequest.FLASH_CONNECT_REQUEST), i)  #
            SendPackage(send.processPackages(ServerRequest.LOCATION_SYSTEM), i)
            print('end')


def SendPackage(package, userIndex):
    print(*list(package))
    users[userIndex].send(package)


def DecodePackage(packNum, packBytes, id):
    print(packNum)
    if packNum == ClientRequest.LOGIN:
        DecodeLogin(packBytes)
        SendPackage(CompilOnline(), id)
        SendPackage(CompilVersion(), id)
    else:
        print("unknow package", packNum)


def DecodeLogin(pack):
    decoder = PackageDecoder()
    decoder.data = pack
    print('Decode login')
    print(decoder.read_utf(), decoder.read_utf(), decoder.read_utf(), decoder.read_utf())


def CompilOnline():
    creator = PackageCreator()
    creator.PackageNumber = ServerRequest.ONLINE
    creator.write_int(1)
    creator.write_int(len(users))
    return creator.get_package()


def CompilVersion():
    creator = PackageCreator()
    creator.PackageNumber = ServerRequest.VERSION
    creator.write_utf("Hello, im your ass hehe")
    return creator.get_package()


StartServer()
