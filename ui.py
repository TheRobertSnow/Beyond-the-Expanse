class App:
    def __init__(self):
        self.menuText = """
===========================================================================================
    ____                       __   __  __            ______
   / __ )___  ____  ____  ____/ /  / /_/ /_  ___     / ____/  ______  ____ _____  ________
  / __  / _ \\/ __ \\/ __ \\/ __  /  / __/ __ \\/ _ \\   / __/ | |/_/ __ \\/ __ `/ __ \\/ ___/ _ \\
 / /_/ /  __/ /_/ / / / / /_/ /  / /_/ / / /  __/  / /____>  </ /_/ / /_/ / / / (__  )  __/
/_____/\\___/\\____/_/ /_/\\__,_/   \\__/_/ /_/\\___/  /_____/_/|_/ .___/\\__,_/_/ /_/____/\\___/
                                                            /_/
===========================================================================================
"""
        self.mainMenu = """
    1.  Start new game
    2.  Load save
    3.  Quit
"""
        self.main_menu()

    def main_menu(self):
        mainMenuDict = {'1': newGame, '2': loadSave, '3'}
        print(self.menuText)
        while True:
            print(self.mainMenu)
            userInput = input()
            if userInput not in mainMenuDict:
                print("Unknown input...")
            else:
                break
    def newGame(self):
        print("Created new game")

    def loadGame(self):
        print("Loaded save")
