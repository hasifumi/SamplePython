# -*- coding: UTF-8 -*-

class Card():
    SUIT_SPADE = 1
    SUIT_DIAMOND = 2
    SUIT_CLUB = 3
    SUIT_HEART = 4
    SUIT_NUM = 4
    CARD_NUM = 13

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def getNumber(self):
        return self.number

    def getSuit(self):
        return self.suit

    def toString(self):
        rtn = ""

        if self.suit == Card.SUIT_SPADE:
            rtn = "S"
        elif self.suit == Card.SUIT_DIAMOND:
            rtn = "D"
        elif self.suit == Card.SUIT_CLUB:
            rtn = "C"
        elif self.suit == Card.SUIT_HEART:
            rtn = "H"

        if self.number == 1:
            rtn += "A"
        elif self.number == 10:
            rtn += "T"
        elif self.number == 11:
            rtn += "J"
        elif self.number == 12:
            rtn += "Q"
        elif self.number == 13:
            rtn += "K"
        else:
            rtn += str(self.number)

        return rtn

class Jorker(Card):
    def __init__(self):
        Card.__init__(self, 0, 0)

    def setSuit(self, suit):
        self.suit = suit

    def setNumber(self, number):
        self.number = number

    def toString(self):
        return "JK"
