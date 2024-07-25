from modules.Player import Player
from modules.Card import Card
from collections import Counter

def test_sumPlayerHand():

    # Single ace
    player = Player([Card('A', "Hearts")])
    assert player.sumHand() == {1, 11}

    # Two aces
    player = Player([Card('A', "Hearts"), Card('A', "Hearts")])
    assert player.sumHand() == {2, 12, 22}

    # Single ace, other cards
    player = Player([Card('A', "Hearts"), Card('4', "Hearts"), Card('6', "Hearts")])
    assert player.sumHand() == {11, 21}

    # Two aces, other cards
    player = Player([Card('K', "Hearts"), Card('9', "Hearts"), Card('A', "Hearts"), Card('A', "Hearts")])
    assert player.sumHand() == {21, 31, 41}