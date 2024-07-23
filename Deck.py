import random
from Card import Card

# Class to describe a 52-card deck
class Deck:
    def __init__(self):
        self.suites = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'A']
        self.Cards = []
        for rank in self.ranks:
            for suite in self.suites:
                self.Cards.append(Card(rank, suite))
        
    # Randomly shuffles the `Cards`
    def deckShuffle(self):
        self.Cards = random.shuffle(self.Cards)

    # Removes and returns the first card in `Cards`
    def topCard(self):
        return self.Cards.pop(0)

    # Returns the number of cards in `Cards`
    def numCards(self):
        return len(self.Cards)
                
