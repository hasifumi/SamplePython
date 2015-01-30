import card
import random

class Hand:
    def __init__(self):
        self.hand = []

    def addCard(self, card):
        self.hand.append(card)
        print(len(self.hand))

    def lookCard(self, position):
        if 0 <= position and position < len(self.hand):
            return self.hand[position]
        else:
            return None

    def pickCard(self, position):
        if 0 <= position and position < len(self.hand):
            return self.hand.pop(position)
        else:
            return None

    def shuffle(self):
        #debug
        #self.toString()
        for i in range(len(self.hand)*2):
            pos = random.randrange(0, len(self.hand))
            pickedCard = self.hand.pop(pos)
            self.hand.insert(pos, pickedCard)
        #debug
        #self.toString()

    def getNumberOfCards(self):
        return len(self.hand)

    #def toString(self):
    #    wkStr = ""
    #    for i in self.hand
    #        wkStr = wkStr + i.toString() + " "
    #    return wkStr

