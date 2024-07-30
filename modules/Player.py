from modules.Card import Card
from typing import List
import random

# Describes a single player (including a dealer)
class Player:
    def __init__(self, cards: List[Card] = [], cash: int = 0, name: str = "Player"):
        self.cards = cards
        self.cash = cash
        self.playing = True
        self.roundWin = False
        self.name = name
    
    def __str__(self) -> str:
        cards = ""
        for card in self.cards:
            cards += f"{str(card)} "
        return f"| Cash: {self.cash} Cards: {cards} |"

    # Accessors
    def getCards(self):
        return self.cards
    def isPlaying(self):
        return self.playing
    def getRoundWin(self):
        return self.roundWin
    def getName(self):
        return self.name
    
    def setRoundWin(self, status):
        self.roundWin = status
    
    # Function to signal the player will stay
    def stay(self):
        self.playing = False
    
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
                self.playing = False
                self.roundWin = True
                return True
        return False
    
    # Function to check whether the player busted
    def checkBust(self):
        sums = self.sumHand()
        if all(sum > 21 for sum in sums):
            self.playing = False
            return True
        return False