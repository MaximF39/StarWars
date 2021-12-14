import socket

ip = '127.0.0.1'
port = 1234

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((ip, port))
def start():
    while True:
        client.send(input().encode())
        data = client.recv(2048) # size byte

if __name__ == '__main__':
    start()






