import sys
from contextlib import contextmanager
import math
import unittest
from test_common import *
import task1

class TestTask1(TestCase):
  def test_init(self):
    with self.vis("empty init"):
      x = task1.HashTable()
    with self.vis("init with size and base"):
      z = task1.HashTable(800, 2398)
      
    assert self.check_okay("init")
    
  def test_hash(self):

    x = task1.HashTable(1024, 17)
    for (key, expect) in [("", 0),
                          ("abcdef", 389),
                          ("defabc", 309)]:
        with self.vis():
          self.assertEqual(x.hash(key), expect, msg=f"Unexpected hash with base 17 and key {key}.")

    assert self.check_okay("hash")

    # checks to see if it rejects key integers
    with self.assertRaises(TypeError, msg="can't hash integers"):
      x.hash(100)

    # checks to see if hashing formula is correct
    self.assertFalse("((" == "P", msg="Hashes should not add to same value")
    self.assertEqual(x.hash("(("), 720, msg="multiple digits should evaluate to correct value")
    self.assertEqual(x.hash("P"), 80, msg="values should be from correct ASCII table value")

  # The tests for __contains__ and __getitem__ use __setitem__, so we don't make any assumptions
  # about the underlying array representation. Remember to define your own tests for __setitem__
  # (and rehash)
  def test_contains(self):
    x = task1.HashTable(1024, 1)

    with self.vis():
      self.assertFalse("abcdef" in x, "False positive in __contains__ for empty table.")

    with self.vis("unexpected failure in setitem"):
      x["abcdef"] = 18
      x["definitely a string"] = None
      x["abdcef"] = "abcdef"

    for key in ["abcdef", "definitely a string", "abdcef"]:
      with self.vis():
        self.assertTrue(key in x, "False negative in __contains__ for key {}".format(key))

    assert self.check_okay("contains")

    testTable = task1.HashTable()

    # test to see if can check whether hash contains correct value
    testTable["james"] = 5
    self.assertEqual(testTable["james"], 5, msg="Contains failure")

    # checks to see if inserting will increment counter by 1
    self.assertEqual(testTable.count, 1, msg="Not inserting elements correctly")

    # test to see if it can retrieve replaced element
    testTable["james"] = 7
    self.assertEqual(testTable["james"], 7, msg="Failure to replace")
    self.assertEqual(testTable.count, 1, msg="Not inserting elements correctly")

    # test to see if contains can correctly find keys
    self.assertTrue("james" in testTable, msg="Contains is incorrect")
    self.assertFalse("jamess" in testTable, msg="Contains is incorrect")

    # test to see if contains can correctly find keys when updated
    testTable["jamess"] = 4
    self.assertTrue("jamess" in testTable, msg="Contains is incorrect")

    # test to see if count will further update
    self.assertFalse(testTable.count == 1, msg="Should change count when element inserted")

  def test_getitem(self):
    x = task1.HashTable(1024, 1)

    with self.vis():
      with self.assertRaises(KeyError, msg="x[key] should raise KeyError for missing key."):
        elt = x["abcdef"]
      
    with self.vis("unexpected failure in setitem"):
      x["abcdef"] = 18
      x["definitely a string"] = None

    with self.vis():
      self.assertEqual(x["abcdef"], 18, msg = "Read after store failed.")
    x["abdcef"] = 22

    assert self.check_okay("getitem")

    testTable = task1.HashTable()
    # "!" = 33, 33/11=0
    testTable["!"] = 328

    # test to see if it can get correct value with specified key
    self.assertEqual(testTable["!"], 328, msg="Not retrieving hash values correctly")

    # test to see if unique keys with same hash remainder wont interfere with eachother
    with self.assertRaises(KeyError, msg="Different keys with same remainder shouldnt return same value"):
      # "7" = 55, 55/11=0
      test = testTable["7"]

    testTable["7"] = 232

    # test to see if it can retrieve the correct value even if remainders are same
    self.assertEqual(testTable["7"], 232, msg="Not retrieving updated values on hash table")


  def test_rehash(self):
    assert self.check_okay("rehash")
    testTable = task1.HashTable(2)
    # checks to see if initial hashtable size is correct
    self.assertEqual(testTable.length, 2, msg="Incorrect initialized hashtable size")
    testTable["test"] = 0

    # test to see if rehash calls correctly
    self.assertFalse(testTable.length == 7, msg= "should not extend until full")
    testTable["test2"] = 0
    testTable["fff"] = 0

    # test to see if rehashes when full
    self.assertEqual(testTable.length, 7, msg="Failure rehashing when inserting into full table")

if __name__ == '__main__':
  unittest.main()
