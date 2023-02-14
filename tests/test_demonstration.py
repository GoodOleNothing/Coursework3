import unittest
import demonstration

class Testdemonstration(unittest.TestCase):

    def test_looking_for_last_five_executed(self):
        self.assertEqual(demonstration.looking_for_last_five_executed([{'state':'EXECUTED'}]), [{'state': 'EXECUTED'}])

