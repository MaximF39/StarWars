import socket
import

ip = '127.0.0.1'
port = 1234

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
    # socket.TCP
)

server.bind(
    (ip, port)
)

server.listen()

users = []


def send_all(data):
    for user in users:
        user.send(data)


def listen_user(user):
    while True:
        data = user.recv(2048)
        print(data.decode())
        send_all(data)


def start_server():
    while True:
        user_socket, address = server.accept()
        print('hello', address)
        users.append(user_socket)


if __name__ == '__main__':
    start_server()
