import socket, threading
class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAddress = clientAddress
        self.clientIP = clientAddress[0]
        print("Connection from: ", self.clientAddress, flush=True)

    def start(self):
        print("Connection from: ", self.clientIP, flush=True)
        msg = ""
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg == "1":
                self.csocket.send(bytes("Creating game", "UTF-8"))
                self.newGame()
            elif msg == "2":
                self.csocket.send(bytes("Loading game", "UTF-8"))
                self.loadGame()
            elif msg == "quit":
                print(f"User {self.clientIP} disconnected", flush=True)
                break
            else:
                self.csocket.send(bytes("Input not recognized", "UTF-8"))

    def newGame(self):
        print(clientAddress, " created a game.", flush=True)
        msg = ""
        self.csocket.send(bytes("Let's go!", "UTF-8"))
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg=="quit":
                break
            print("From client: ", msg, flush=True)
            self.csocket.send(bytes(msg, "UTF-8"))

    def loadGame(self):
        print(clientAddress, " loaded a game.", flush=True)
        msg = ""
        self.csocket.send(bytes("Let's go!", "UTF-8"))
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg=="quit":
                break
            print("From client: ", msg, flush=True)
            self.csocket.send(bytes(msg, "UTF-8"))

LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    print("Starting thread for: ", clientAddress)
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()



    # def game_loop(self):
    #     print("Connection from: ", clientAddress, flush=True)
    #     msg = ""
    #     while True:
    #         data = self.csocket.recv(2048)
    #         msg = data.decode()
    #         if msg=="quit":
    #             break
    #         print("From client: ", msg, flush=True)
    #         self.csocket.send(bytes(msg, "UTF-8"))
