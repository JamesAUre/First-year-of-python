import sys
from contextlib import contextmanager
import math
import unittest
from test_common import *
import task1
import task2

class TimedOutExn_(Exception):
  pass

class TestTask2(TestCase):
  def test_load(self):
    with self.vis():
      table = task1.HashTable()
      task2.load_dictionary(table, "words_simple.txt", 10)
      self.assertEqual(count_nonempty_buckets(table), 6)

    with self.vis():
      table = task1.HashTable()
      task2.load_dictionary(table, "words_empty.txt", 10)
      self.assertEqual(count_nonempty_buckets(table), 11, "Failed to handle empty line or whitespace.")

    self.assertTrue(self.check_okay("load_dictionary"))


    myTable = task1.HashTable()
    # test to see if it can load my own file
    task2.load_dictionary(myTable, "testFile3.txt", 10)

    # test to see if no duplicate data stored
    self.assertEqual(count_nonempty_buckets(myTable), 12, "If key is the same, should overwrite")

    # new file contains unique words, this should be added onto the hashtable
    task2.load_dictionary(myTable, "anotherTestFile.txt", 10)
    self.assertEqual(count_nonempty_buckets(myTable), 15, "If loaded again, should not overwrite")

    # should throw an error if cant find file
    with self.assertRaises(FileNotFoundError, msg="Shouldn't be able to read non existant files"):
      task2.load_dictionary(myTable, "thisshouldntexist.txt", 10)


  def test_load_timeout(self):
    with self.vis("load without max_time"):
      table = task1.HashTable()
      task2.load_dictionary(table, "words_simple.txt")

    with self.vis("failed to apply timeout"):
      table = task1.HashTable(100000, 1)
      with self.assertRaises(Exception, msg = "reading too many words should time out."):
        try:
          self.with_deadline(3, task2.load_dictionary, (table, "english_small.txt", 1))
        except TimedOutExn_:
          pass

    self.assertTrue(self.check_okay("load_dictionary timeout"))
    myTable = task1.HashTable(7, 1)

    # should not crash even if rehashing table
    task2.load_dictionary(myTable, "testFile3.txt", 10)

    # should not be able to read words with a time of 0 (tests limits of timer)
    with self.assertRaises(Exception, msg = "Reading words on a timer of 0 shouldn't work"):
      task2.load_dictionary(myTable, "testFile3.txt", 0)

  def test_load_time(self):
    with self.vis("reporting words"):
      (words, time) = self.with_deadline(1, task2.load_dictionary_time, (31, 100, "words_simple.txt", 10))
      self.assertEqual(words, 6)

    self.assertTrue(self.check_okay("load_dictionary time"))


if __name__ == '__main__':
  unittest.main()
