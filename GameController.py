from Table import Table

class GameController:

    def __init__(self) -> None:
        self.table = None
    
    # Method for a single player to play a command-line based game
    def terminalGame(self):

        # Initializing the game
        self.table = Table(1, 0, 0)
        table = self.table
        table.initGame()
        print("Take a seat at the table!")

        while(not table.getDeck().isEmpty):





    