import sys
from contextlib import contextmanager
import math
import unittest
from test_common import *
import task6

class TestTask6(TestCase):
  def test_addfile(self):
    with self.vis():
      freq = task6.Freq()
      freq.add_file('words_simple.txt')
      for word in ['this', 'dictionary', 'words']:
        self.assertEqual(freq.word_frequency[word], 1,
          "Incorrect frequency.")

    with self.vis():
      freq = task6.Freq()
      freq.add_file('words_dup.txt')
      for (word, count) in [('words', 3), ('and', 2)]:
        self.assertEqual(freq.word_frequency[word], count,
          "Incorrect frequency.")
     
    self.assertTrue(self.check_okay("addfile"))
    with self.assertRaises(FileNotFoundError, msg="Shouldn't run if file not found"):
      freq.add_file("rfdfsdklfslfsdkn.txt")

    freq = task6.Freq()
    freq.add_file('testFile3.txt')

    # test to see if can handle on my own files and words with grammar
    for (word, count) in [('this', 2), ("I'm", 1)]:
      self.assertEqual(freq.word_frequency[word], count,
                       "Incorrect frequency.")

    # test to see if maxval contains the count of the most frequent word
    self.assertEqual(freq.maxval, 2, msg="Max frequency should be 2")

    # test to see if correct error is raised when word not found
    with self.assertRaises(KeyError, msg="Shouldn't be able to find a non existant word"):
      x = freq.word_frequency["dfdsscvxcv"]

    # test to see if basic punctuation strips off word
    freq = task6.Freq()
    freq.add_file("punctuation.txt")

    self.assertEqual(freq.word_frequency["test"], 2, msg="Should strip basic punctuation")

  def test_rarity(self):
    with self.vis():
      freq = task6.Freq()
      freq.add_file('words_freq.txt')

      self.assertEqual(freq.rarity('a'), 0,
        "Incorrect rarity.")

    with self.vis():
      self.assertEqual(freq.rarity('fish'), 2,
        "Incorrect rarity.")

    self.assertTrue(self.check_okay("rarity"))

    # testing how it handles no word occurance
    self.assertEqual(freq.rarity("wubalubadubdub"), 3, "incorrect rarity")

    # testing how it handles incorrect data
    with self.assertRaises(TypeError, msg="cant put in integers"):
      freq.rarity(43)



if __name__ == '__main__':
  unittest.main()
