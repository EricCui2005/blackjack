# Class to describe a single playing card
class Card:
    def __init__(self, rank: int, suite: str):

        # Denotes card value and suite
        self.rank = rank
        self.suite = suite

    # To string method
    def __str__(self) -> str:
        return f"[{self.rank} of {self.suite}]"

    # Accessor methods
    def get_rank(self):
        return self.rank 
    def get_suite(self):
        return self.suite