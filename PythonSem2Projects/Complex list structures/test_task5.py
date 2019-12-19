import math
import unittest
from test_common import *
import task5

class TestTask5(unittest.TestCase):
  def test_search(self):
    ed = task5.Editor()
    ed.read_filename('TestFile.txt')
    
    queries = [ ("is a", [1, 2]), # Multi-word
                ("is", [1, 2]), # Multiple occurrences
                ("potato", []), # No word occurrence
                ("testinging", []), # Should not occur
                ("lines", [3, 4])] # Multi-word

    for query, lines in queries:
      ed_lines = ed.search_string(query)
      self.assertTrue(sorted(ToList(ed_lines)) == lines, msg =  "Incorrect result for search query {0}".format(query))

    ed.read_filename('small.txt')

    queries = [("this", [2]),  # Should be case sensitive
               ("element 3", [3]),  # Should handle numbers in strings
               ("cred", []),  # Should stop reading query once it finds an index doesnt align
               ("James\nthis", []),  # Should not read past each line
               ("Wow! Big cool!", [4])]  # Should be able to read entire lines

    for query, lines in queries:
      ed_lines = ed.search_string(query)
      self.assertTrue(sorted(ToList(ed_lines)) == lines, msg="Incorrect result for search query {0}".format(query))

if __name__ == '__main__':
  unittest.main()
