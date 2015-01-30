import hand
import card
import unittest

class HandClassTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAddCard(self):
        h1 = hand.Hand()
        c1 = card.Card(1, 13)
        h1.addCard(card)
        print(h1.toString())

if __name__ == "__main__":
    unittest.main()
