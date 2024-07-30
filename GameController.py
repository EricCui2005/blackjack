from modules.Table import Table

class GameController:

    def __init__(self) -> None:
        self.table = None
    
    # Method for a single player to play a command-line based game
    def terminalGame(self):

        # Initializing the game
        self.table = Table(2, 0, 0)
        table = self.table
        deck = table.getDeck()
        table.initGame()
        dealer = table.getDealer()
        player = table.getPlayer(0)
        print("Take a seat at the table!")

        # We play until the deck is empty
        while(not table.getDeck().isEmpty()):

            table.initRound()

            # Defaulting to no active players. Flag will be set in the following loops
            table.setActivePlayersStatus(False)

            for player in table.getPlayers():
                
                # Cards only offered to players that are still in play
                if player.isPlaying():
                    print(f"\n{player.getName()}")
                    # Round still contains active players
                    table.setActivePlayersStatus(True)

                    # Displaying current cards
                    cardsString = ""
                    for card in player.getCards():
                        cardsString += str(card)
                    print(f"Cards: {cardsString}")

                    # Hit or stay
                    choice = int(input("Hit (1) or Stay (2): "))
                    
                    # Choice action
                    match choice:
                        case 1:
                            player.newCard(deck.topCard())
                            player.checkBlackjack()
                            player.checkBust()
                        case 2:
                            player.stay()
            
            if table.getActivePlayersStatus() == False:
                players = table.getPlayers()

                # All players win if the dealer busts
                if dealer.checkBust():
                    for player in players:
                        player.setRoundWin(True)
                
                # All players lose if the dealer gets a blackjack, excluding players with blackjacks
                elif dealer.checkBlackjack():
                    for player in players:
                        if player.getRoundWin():
                            print(f"{player.getName()} pushes")
                        else:
                            print(f"{player.getName} loses")
                
                # Case where dealer neither busts nor has a blackjack
                else:

                    # Getting the highest dealer hand sum that does not bust
                    dealerSums = dealer.sumHand()
                    filteredDealerSums = [dealerSum for dealerSum in dealerSums if dealerSum < 21]
                    dealerHighSum = max(filteredDealerSums)

                    for player in table.getPlayers():

                        # Getting the highest player hand sum that does not bust
                        playerSums = player.sumHand()
                        filteredPlayerSums = [playerSum for playerSum in playerSums if playerSum < 21]
                        playerHighSum = max(filteredPlayerSums)

                        if playerHighSum < dealerHighSum:
                            print(f"{player.getName()} loses")
                        elif playerHighSum > dealerHighSum:
                            print(f"{player.getName()} wins")
                        else:
                            print(f"{player.getName()} pushes")

                    









    