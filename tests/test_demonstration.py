import unittest #с пайтест пока не сработался, пробую unittest
import demonstration
from main import executed

class Testdemonstration(unittest.TestCase):

    def test_looking_for_executed(self):
        self.assertEqual(demonstration.looking_for_executed([{'state': 'EXECUTED'}]), [])
        self.assertEqual(demonstration.collect_and_present_data(executed), None)

