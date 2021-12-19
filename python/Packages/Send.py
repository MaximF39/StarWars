from python.Packages import PackagesManager, ReadPackages
from python.Static.ServerRequest import ServerRequest


def StartServer():
    print("Server is started")
    i = 0
    # while True:
    #     for i in range(len(users)):
            # decoder = PackageDecoder()
            # decoder.data = users[i].recv(16)
            # PackageNumberGet: int = decoder.read_int()
            # NaN = decoder.read_int()
            # NaN = decoder.read_int()
            # lenBytes = decoder.read_int()
            # packages = read_packes.main(PackageNumberGet, users[i].recv(lenBytes))
            # print(PackageNumberGet, packages)
    send = PackagesManager()
    SendPackage(send.processPackages(ServerRequest.VERSION), i)
    SendPackage(send.processPackages(ServerRequest.ONLINE), i)
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
    # SendPackage(send.processPackages(ServerRequest.FLASH_CONNECT_REQUEST), i)  #
    send2()

all_bytes = bytearray()

def SendPackage(package, userIndex):
    for i in package:
        all_bytes.append(i)

def send2():
    r = ReadPackages(all_bytes)

