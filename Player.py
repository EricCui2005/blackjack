from Card import Card
from typing import List
import random

# Describes a single player (including a dealer)
class Player:
    def __init__(self, cards: List[Card] = [], cash: int = 0):
        self.cards = cards
        self.cash = cash
    
    def __str__(self) -> str:
        cards = ""
        for card in self.cards:
            cards += f"{str(card)} "
        return f"| Cash: {self.cash} Cards: {cards} |"

    # Accessor for player's cards
    def getCards(self):
        return self.cards
    
    # Add a new card to the player's hand
    def newCard(self, card: Card):
        self.cards.append(card)
    
    # Function to randomly decide to hit or not
    def randomHit():
        return random.choice([True, False])
    
    # Function to (considering the ace rule) return all possible summings of a player's hand
    def sumHand(self):
        sums = []
        self.sumRec(self.cards, 0, sums)
        return sums       
        
    # Recursive summing method
    def sumRec(self, cards: List[Card], curSum, sums):

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
