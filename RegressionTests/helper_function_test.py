from modules.Player import Player
from modules.Card import Card
from collections import Counter

def test_sumPlayerHand():
    player = Player([Card("K", "Hearts"), Card("9", "Hearts"), Card("A", "Hearts")], 0)
    assert Counter(player.sumHand()) == Counter([20, 30])