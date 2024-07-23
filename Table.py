from Deck import Deck
from Player import Player

# Class to describe a table of blackjack
class Table:
    def __init__(self, numPlayers: int, playerWins: int, dealerWins: int):
        self.gameDeck = Deck()
        self.numPlayers = numPlayers
        self.players = []
        self.playerWins = 0
        self.dealerWins = 0

    # Initializes the game
    def initGame(self):
        self.gameDeck.deckShuffle()
        for i in range(self.numPlayers):
            card = self.gameDeck
            self.players.append(Player([self.gameDeck.topCard()]))
        
        