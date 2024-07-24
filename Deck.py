import random
from Card import Card

# Class to describe a 52-card deck
class Deck:
    def __init__(self):
        self.suites = ["H", "D", "S", "C"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.rankValueKey = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, 
                             "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": (1, 11)}
        self.Cards = []
        for rank in self.ranks:
            for suite in self.suites:
                self.Cards.append(Card(rank, suite))
    
    # To string method
    def __str__(self) -> str:
        deck = ""
        for card in self.Cards:
            deck += f"{str(card)}\n" 
        return deck
        
    # Randomly shuffles the `Cards`
    def deckShuffle(self):
        random.shuffle(self.Cards)

    # Removes and returns the first card in `Cards`
    def topCard(self):
        return self.Cards.pop(0)

    # Returns the number of cards in `Cards`
    def numCards(self):
        return len(self.Cards)
    
    # Checks if deck is empty
    def isEmpty(self):
        return self.numCards() == 0
                
