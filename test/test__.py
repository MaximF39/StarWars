from socket import socket

server = socket()
server.bind(("localhost", 10000))
server.close()