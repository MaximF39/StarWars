LOCALHOST = "127.0.0.1"
PORT = 15077
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
server.listen(10)
print("Server started \nWaiting for client request..")
while True:
    clientsock, clientAddress = server.accept()