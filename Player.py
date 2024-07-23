from Card import Card
from typing import List

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

    # Add a new card to the player's hand
    def newCard(self, card: Card):
        self.cards.append(card)
