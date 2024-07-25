# Class to describe a single playing card
class Card:
    def __init__(self, rank: str, suite: str):

        # Denotes card value and suite
        self.rank = rank
        self.suite = suite
        self.rankValueKey = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, 
                             "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": (1, 11)}

    # To string method
    def __str__(self) -> str:
        return f"[{self.rank} of {self.suite}]"

    # Accessor methods
    def get_rank(self):
        return self.rank 
    def get_suite(self):
        return self.suite