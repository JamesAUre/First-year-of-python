import math
import unittest
from test_common import *
import task2

class TestTask2(unittest.TestCase):
  def test_insert(self):
    x = task2.ListADT(10)
    
    ## This should not fail.
    append(x, [1 for i in range(1000)])
    
    ## If the ListADT has renamed the underlying array, or used some other
    ## representation, we can't realy test whether resizing is handled correctly.
    if not hasattr(x, "the_array"):
      raise AttributeError("could not identify underlying array for the ListADT.")

    y = task2.ListADT(10)

    # If we gave a smaller constant, should have become 40.
    self.assertEqual(len(y.the_array), 40, "Allocated array below threshold.")

    # ... and with rounding
    y = task2.ListADT(44)
    for i in range(45):
      y.insert(i, i)
    self.assertEqual(len(y.the_array), 84, "Incorrect grow.") # math.ceil(44 * 1.9)

    # Check shrinking
    for i in range(25):
      y.delete(len(y)-1)
    self.assertTrue(len(y.the_array) == 42, "Incorrect shrink.")

# TESTING EXTENSION FUNCTIONALITY
  def test_extend(self):
    extendlist = task2.ListADT(40)

    # To make sure it extends appropriately, make sure it starts at the correct size to extend from
    self.assertEqual(len(extendlist.the_array), 40, "Incorrect starting size")
    for i in range(40):
      extendlist.insert(i, i)

    # Once it reaches max capacity, should extend by 1.9* its original max size
    self.assertEqual(len(extendlist.the_array), 77, "Incorrect extending size")

    # Length of the list should be 40 once it extends (as this is its original max capacity)
    self.assertEqual(len(extendlist), 40, "Incorrect list size")

    extendlist.insert(3,1)

    # Max size should remain the same even after an element is inserted, only extends when full
    self.assertEqual(len(extendlist.the_array), 77, "Incorrect extending size")

    # Making sure the list actually extended while the max size remained the same
    self.assertNotEqual(len(extendlist), 40, "Incorrect list size")

# TESTING SHRINK FUNCTIONALITY
  def test_shrink(self):
    shrinklist = task2.ListADT(51)
    shrinklist.insert(0,0)

    # Should not shrink unless you take an element away from the list
    self.assertEqual(len(shrinklist.the_array), 51, "Incorrect shrink size")

    for i in range(1, 51):
      shrinklist.insert(i, i)

    # Should not shrink if length of list is not less than 1/4 of the size of its capacity
    shrinklist.delete(3)
    self.assertEqual(len(shrinklist.the_array), 97, "Incorrect shrink size")

    for i in range(49, 20, -1):
      shrinklist.delete(i)

    # Should shrink if the length of the list is less than 1/4 of its capacity (by half the size)
    self.assertEqual(len(shrinklist.the_array), 48, "Incorrect shrink size")

    for i in range(20, 10, -1):
      shrinklist.delete(i)

    # Should never shrink below a max size of 40
    self.assertEqual(len(shrinklist.the_array), 40, "Incorrect shrink size")

if __name__ == '__main__':
  unittest.main()
