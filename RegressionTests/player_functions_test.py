from modules.Player import Player
from modules.Card import Card
from modules.Table import Table
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

def test_initGame():

    # Initializing test table
    table = Table()
    table.initGame()

    # Checking all players have two cards and all cards are different
    properInit = True
    cardsOnTable = set()
    seats = table.getSeats()
    for seat in seats:
        player = seats[seat]
        if len(player.getCards()) != 2:
            properInit = False
            break
        for card in player.getCards():
            if card in cardsOnTable:
                properInit = False
            cardsOnTable.add(card)

    # Final assertion
    assert properInit == True
            
# checkBlackjack() tests
def test_checkBlackjack_WhenGivenOneSumBlackjack_CorrectlyIdentifies():
    player = Player([Card("K", "Hearts"), Card("9", "Hearts"), Card("2", "Hearts")])
    assert player.checkBlackjack() == True
    
def test_checkBlackjack_WhenGivenMultiSumBlackjack_CorrectlyIdentifies():
    player = Player([Card("K", "Hearts"), Card("A", "Hearts")])
    assert player.checkBlackjack() == True

def test_checkBlackjack_WhenNoBlackjack_CorrectlyIdentifies():
    player = Player([Card("A", "Hearts"), Card("9", "Hearts")])
    assert player.checkBlackjack() == False

# checkBust() tests
def test_checkBust_WhenBust_CorrectlyIdentifies():
    player = Player([Card("K", "Hearts"), Card("K", "Hearts"), Card("K", "Hearts")])
    assert player.checkBust() == True

def test_checkBust_WhenNoBust_CorrectlyIdentifies():
    player = Player([Card("K", "Hearts"), Card("K", "Hearts")])
    assert player.checkBust() == False

# isPlaying tests
def test_isPlaying_WhenBlackjack_IsFalse():
    player = Player([Card("K", "Hearts"), Card("9", "Hearts"), Card("2", "Hearts")])
    player.checkBlackjack()
    assert player.isPlaying() == False

def test_isPlaying_WhenBust_IsFalse():
    player = Player([Card("K", "Hearts"), Card("9", "Hearts"), Card("3", "Hearts")])
    player.checkBust()
    assert player.isPlaying() == False






