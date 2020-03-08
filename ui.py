import menus, settings
import socket

class App:
    def __init__(self):
        # print(self.generateTextWindow(menus.MAIN_MENU))
        self.server = settings.SERVER
        self.port = settings.PORT
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.server, self.port))
        self.client.sendall(bytes("This is from Client",'UTF-8'))
        self.main_menu()

    def game_loop(self):
        while True:
            in_data =  self.client.recv(1024)
            print("From Server :" ,in_data.decode())
            out_data = input()
            self.client.sendall(bytes(out_data,'UTF-8'))
            if out_data=='quit':
                break

    def main_menu(self):
        while True:
            in_data =  self.client.recv(1024)
            print("From Server :" ,in_data.decode())
            if in_data.decode()=="Creating game" or in_data.decode() == "Loading game":
                self.game_loop()
            print(self.generateTextWindow(menus.MAIN_MENU))
            out_data = input()
            self.client.sendall(bytes(out_data,'UTF-8'))
            if out_data=='quit':
                break
        self.client.close()

    def generateTextWindow(self, data):
        dataList = data.split("\n")
        returnStr = ""
        maxLen = 0
        for line in dataList:
            if len(line) > maxLen:
                maxLen = len(line)

        returnStr += "+" + ("-" * (maxLen+2)) + "+\n"
        for i in range(0, len(dataList)):
            mystr = dataList[i]
            while len(mystr) < maxLen:
                mystr += " "
            returnStr += "| " + mystr + " |\n"
        returnStr += "+" + ("-" * (maxLen+2)) + "+\n"
        return returnStr
