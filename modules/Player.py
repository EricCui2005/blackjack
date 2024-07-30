from modules.Card import Card
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

    # Accessors
    def getCards(self):
        return self.cards
    def isBusted(self):
        return self.bust
    def hasBlackjack(self):
        return self.blackjack
    
    # Add a new card to the player's hand
    def newCard(self, card: Card):
        self.cards.append(card)
    
    # Function to randomly decide to hit or not
    def randomHit():
        return random.choice([True, False])
    
    # Function to (considering the ace rule) return all possible summings of a player's hand
    def sumHand(self):
        sums = set()
        self.sumRec(self.cards, 0, sums)
        return sums       
        
    # Recursive summing method
    def sumRec(self, cards: List[Card], curSum, sums):

        # Card list is empty
        if not cards:
            sums.add(curSum)
            return
        
        # Recursive logic
        card = cards.pop()
        if card.get_rank() == 'A':
            self.sumRec(cards, curSum + 1, sums)
            self.sumRec(cards, curSum + 11, sums)
            cards.append(card)
        else:
            self.sumRec(cards, curSum + card.rankValueKey[card.get_rank()], sums)
            cards.append(card)
        return
    
    # Function to check whether the player has a blackjack
    def checkBlackjack(self):
        sums = self.sumHand()
        for sum in sums:
            if sum == 21:
                return True
        return False
    
    # Function to check whether the player busted
    def checkBust(self):
        sums = self.sumHand()
        if all(sum > 21 for sum in sums):
            return True
        return False