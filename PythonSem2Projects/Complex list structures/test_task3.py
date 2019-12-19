import math
import unittest
from test_common import *
import task3

class TestTask3(unittest.TestCase):
  def test_read_file(self):
    test_lines = task3.read_text_file('TestFile.txt')
    self.assertEqual([ l.strip('\n') for l in ToList(test_lines) ], test_content, msg = "File not correctly read.")

    # Test if it can read and save each line of my text file onto a ListADT object successfully
    test_myOwn = task3.read_text_file('small.txt')
    self.assertEqual([ l.strip('\n') for l in ToList(test_myOwn)], test_myFile, msg = "File not correctly read.")
if __name__ == '__main__':
  unittest.main()
