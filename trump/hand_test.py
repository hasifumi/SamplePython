import hand
import card
import unittest

class HandClassTestCase(unittest.TestCase):
    def setUp(self):
        self.h1 = hand.Hand()
        self.c1 = card.Card(1, 13)
        self.c2 = card.Card(2, 1)
        self.c3 = card.Card(3, 10)

    def tearDown(self):
        pass

    def testAddCard(self):
        self.h1.addCard(self.c1)
        self.h1.addCard(self.c2)
        self.h1.addCard(self.c3)
        self.assertEqual(self.h1.getNumberOfCards(), 3)

    def testLookCard(self):
        self.h1.addCard(self.c1)
        self.h1.addCard(self.c2)
        #self.assertEqual(self.h1.lookCard(2),
        c2 = self.h1.lookCard(1)
        print(c2.toString())

if __name__ == "__main__":
    unittest.main()
