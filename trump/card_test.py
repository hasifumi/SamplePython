import card
import unittest

class CardClassTestCase(unittest.TestCase):

    def setUp(self):
        self.c1 = card.Card(1, 13)

    def tearDown(self):
        pass

    def testGetNumberMethod(self):
        self.assertEqual(self.c1.getNumber(), 13)

    def testGetSuitMethod(self):
        self.assertEqual(self.c1.getSuit(), 1)

    def testToStringMethod1(self):
        self.assertEqual(card.Card(1,1).toString(), "SA")

    def testToStringMethod2(self):
        self.assertEqual(card.Card(2,2).toString(), "D2")

    def testToStringMethod3(self):
        self.assertEqual(card.Card(3,10).toString(), "CT")

    def testToStringMethod4(self):
        self.assertEqual(card.Card(4,11).toString(), "HJ")

    def testToStringMethod5(self):
        self.assertEqual(card.Card(1,12).toString(), "SQ")

    def testToStringMethod6(self):
        self.assertEqual(card.Card(1,13).toString(), "SK")

class JorkerClassTestCase(unittest.TestCase):

    def setUp(self):
        self.j1 = card.Jorker()

    def tearDown(self):
        pass

    def testToStringMethod(self):
        self.assertEqual(self.j1.toString(), "JK")

    def testSetNumberMethod(self):
        self.j1.setNumber(10)
        self.assertEqual(self.j1.getNumber(), 10)

    def testSetSuiteMethod(self):
        self.j1.setSuit(1)
        self.assertEqual(self.j1.getSuit(), 1)


if __name__ == "__main__":
    unittest.main()

