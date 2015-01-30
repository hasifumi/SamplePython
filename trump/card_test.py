import card
import unittest

class CardClassTestCase(unittest.TestCase):

    def setUp(self):
        self.c1 = card.Card(1, 13)

    def tearDown(self):
        pass

    def testToStringMethod(self):
        self.assertEqual(self.c1.toString(), "SK")

    def testGetNumberMethod(self):
        self.assertEqual(self.c1.getNumber(), 13)

    def testGetSuitMethod(self):
        self.assertEqual(self.c1.getSuit(), 1)

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

