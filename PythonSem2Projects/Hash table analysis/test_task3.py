import sys
from contextlib import contextmanager
import math
import unittest
from test_common import *
import task3

class TestTask3(TestCase):
  def test_statistics(self):
    table = task3.HashTable(1024, 1)

    with self.vis("testing statistics"):
      for key in ["abcdef", "defabc"]:
        table[key] = 1
      stats = table.statistics()
      self.assertEqual(stats, (1, 1, 1, 0), "incorrect statistics")

    with self.vis():
      for key in ["acbedf"]:
        table[key] = 1
      stats = table.statistics()
      self.assertEqual(stats, (2, 3, 2, 0), "incorrect statistics")

    # making my own hash table
    newTable = task3.HashTable(1,6)

    # testing how stats change for list of words
    for words in ["ddds","fdfdsfs", "aaa", "aa", "aaa"]:

      newTable[words] = 1

    # checking if statistics are as expected
    newstats = newTable.statistics()
    self.assertEqual(newstats, (4, 6, 2, 2), "incorrect stats")

    # adding duplicate data
    newTable["aaa"] = 1
    newstats = newTable.statistics()
    self.assertFalse(newstats != (4, 6, 2, 2), "stats don't altar for duplicates")

    # adding non duplicate data after
    newTable["a"] = 1
    newstats = newTable.statistics()
    self.assertFalse(newstats == (4, 6, 2, 2), "stats will change for non duplicates")
    self.assertTrue(self.check_okay("statistics"))

  def test_load_statistics(self):
    with self.vis("reporting words"):
      (w, _, _, _, _, _) = self.with_deadline(1, task3.load_dictionary_statistics, (1, 1024, "words_perm.txt", 10))
      self.assertEqual(w, 5, "incorrect word count")

    self.assertTrue(self.check_okay("load_statistics"))

if __name__ == '__main__':
  unittest.main()
