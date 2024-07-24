from Deck import Deck
from Card import Card
from Player import Player
from typing import List

# Class to describe a table of blackjack
class Table:
    def __init__(self, numSeats: int = 3, playerWins: int = 0, dealerWins: int = 0):
        self.gameDeck = Deck()
        self.dealer = Player()
        self.numSeats = numSeats
        self.seats = {0: None, 1: None, 2: None}
        self.playerWins = 0
        self.dealerWins = 0
    
    # To string method
    def __str__(self) -> str:
        table = str(self.gameDeck)
        for seat in self.seats:
            table += f"{str(self.seats[seat])}\n" 
        return table
    
    # Accessor for the game deck
    def getDeck(self):
        return self.gameDeck
    
    # Method to get possible sums for a player's cards
    def sumPlayerCards(self, player: Player):
        sums = []
        self.sumRec(player.getCards(), 0, sums)
        return sums
        
    # Recursive summing method
    def sumRec(self, cards: List[Card], curSum, sums: List[int]):

        # Card list is empty
        if not cards:
            sums.append(curSum)
            return
        
        # Recursive logic
        card = cards.pop()
        if card.get_rank == "A":
            self.sumRec(self, cards, curSum + 1, sums)
            self.sumRec(self, cards, curSum + 11, sums)
        else:
            self.sumRec(self, cards, curSum + card.rankValueKey[card.get_rank])

        return
            



            



    
    # Function to check for a blackjack
    def checkBlackJack(self, value):
        return value == 21

    # Initializes the game
    def initGame(self):

        # Adding players to table
        for i in range(self.numSeats):
            self.seats[i] = Player([], 500)
        
        # Shuffling and dealing 2 cards to each player (including the dealer)
        self.gameDeck.deckShuffle()
        for i in range(2):
            for seat in self.seats:
                player = self.seats[seat]
                if player:
                    player.newCard(self.gameDeck.topCard())
            self.dealer.newCard(self.gameDeck.topCard())
        

            
        
        