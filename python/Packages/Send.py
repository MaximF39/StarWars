from . import ServerRequest
from . import ReadPackages
from . import PackagesManager

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
    # SendPackage(send.processPackages(ServerRequest.ONLINE, 200), i)
    # SendPackage(send.processPackages(ServerRequest.TOP_LIST), i)
    # SendPackage(send.processPackages(ServerRequest.TOP_CLANS_LIST), i)
    # SendPackage(send.processPackages(ServerRequest.TOP_RATING_LIST), i) #
    # SendPackage(send.processPackages(ServerRequest.WEAPONS_PARAMETERS), i)
    # SendPackage(send.processPackages(ServerRequest.AMMOS_PARAMETERS), i) #
    # SendPackage(send.processPackages(ServerRequest.RESOURCE_PARAMETERS), i) #
    # SendPackage(send.processPackages(ServerRequest.ENGINES_PARAMETERS), i) #
    # SendPackage(send.processPackages(ServerRequest.DEVICE_PARAMETERS), i) #
    # SendPackage(send.processPackages(ServerRequest.DROID_PARAMETERS), i) #
    # SendPackage(send.processPackages(ServerRequest.MAP), i) #
    # SendPackage(send.processPackages(ServerRequest.SHIP_PARAMETERS), i)
    # SendPackage(send.processPackages(ServerRequest.LOGGED), i) #
    # SendPackage(send.processPackages(ServerRequest.PLAYER), i)  #
    # SendPackage(send.processPackages(ServerRequest.TO_GAME), i)  #
    # SendPackage(send.processPackages(ServerRequest.FLASH_CONNECT_REQUEST), i)  #
    # SendPackage(send.processPackages(ServerRequest.LOCATION_SYSTEM), i)
    print('end')


def SendPackage(package, userIndex):
    print(package)
    # r = ReadPackages(package)

