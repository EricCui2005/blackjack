from modules.Deck import Deck
from modules.Card import Card
from modules.Player import Player
from typing import List
from typing import Dict

# Class to describe a table of blackjack
class Table:
    def __init__(self, numPlayers: int = 3, playerWins: int = 0, dealerWins: int = 0):
        self.gameDeck = Deck()
        self.dealer = Player()
        self.numPlayers = numPlayers
        self.players: List[Player] = []
        self.playerWins = 0
        self.dealerWins = 0
    
    # To string method
    def __str__(self) -> str:
        table = str(self.gameDeck)
        for seat in self.seats:
            table += f"{str(self.seats[seat])}\n" 
        return table
    
    # Accessors
    def getDeck(self):
        return self.gameDeck
    def getPlayer(self, seat: int):
        return self.players[seat]
    def getDealer(self):
        return self.dealer
    def getPlayers(self):
        return self.players
            
    # Function to check for a blackjack
    def checkBlackJack(self, value):
        return value == 21

    # Initializes the game
    def initGame(self):

        # Adding players to table
        for i in range(self.numPlayers):
            self.players.append(Player([], 500))
        
        # Shuffling and dealing 2 cards to each player (including the dealer)
        self.gameDeck.deckShuffle()
        self.initRound()

    # Initializes the card dealing of a round   
    def initRound(self):
        for i in range(2):
            for player in self.players:
                player.newCard(self.gameDeck.topCard())
            self.dealer.newCard(self.gameDeck.topCard())
    
        

            
        
        