from modules.Table import Table

class GameController:

    def __init__(self) -> None:
        self.table = None
    
    # Method for a single player to play a command-line based game
    def terminalGame(self):

        # Initializing the game
        self.table = Table(1, 0, 0)
        table = self.table
        table.initGame()
        dealer = table.getDealer()
        player = table.getPlayer(0)
        print("Take a seat at the table!")

        while(not table.getDeck().isEmpty()):

            # Inputting bet
            input("Enter bet: ")

            # Displaying current cards
            cardsString = ""
            for card in player.getCards():
                cardsString += str(card)
            print(f"Cards: {cardsString}")

            # Hit or stay
            choice = input("Hit (1) or Stay (2): ")









    