from socket import socket
from . import PackageCreator, ClientRequest, ServerRequest
from . import PackageDecoder

server = socket()
users = []


def ConnectNewUser():
    while True:
        conn, addr = server.accept()
        users.append(conn)
        print("new user been connected!")

def StartServer():
    server.bind(('localhost', 10000))
    server.listen(1)
    print("Server is started")
    while True:
        for i in range(len(users)):
            decoder = PackageDecoder()
            decoder.data = users[i].recv(16)
            PackageNumber = decoder.read_int()
            if PackageNumber == ClientRequest.FLASH_CONNECT_REQUEST:
                SendPackage(FlashPlayerConnect(), i)
                users.remove(i)
            HZvalue = decoder.read_int()
            HZvalueTwo = decoder.read_int()
            PackageLen = decoder.read_int()
            PackageBytes = users[i].recv(PackageLen)
            DecodePackage(PackageNumber, PackageBytes, i)


def SendPackage(package, userIndex):
    users[userIndex].send(package)


def DecodePackage(packNum, packBytes, id):
    if packNum == ClientRequest.LOGIN:
        DecodeLogin(packBytes)
        SendPackage(CompilOnline(), id)
        SendPackage(CompilVersion(), id)
        pass
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
    return creator.getPackage()


def read_f():
    with open('test.txt', 'r') as f:
        res = f.read()
        return res


def FlashPlayerConnect():
    return PackageCreator().converter(read_f())

def main():
    StartServer()
