import math
import unittest
from test_common import *
import task1


class TestTask1(unittest.TestCase):
    # Check that initialisation doesn't fail
    def test_init(self):
        y = task1.ListADT(10)

        self.assertEqual(y.length, 0, msg="Length of empty list should be 0")

        # Checks to see whether it'll only accept integer values as original list size
        with self.assertRaises(TypeError, msg="List cannot have the size of a non-integer value"):
            f=task1.ListADT(4.3)

    def test_str(self):
        # Check str for non-empty lists
        x = task1.ListADT(10)
        append(x, [1, 2, 3])
        self.assertEqual(str(x).strip('\n'), '1\n2\n3')

        append(x,[4,4,4])

        # Checks to see if appending multiple times will successfully add onto the original str list
        self.assertNotEqual(str(x).strip('\n'), '1\n2\n3\n4\n5\n6')
        self.assertEqual(str(x).strip('\n'), '1\n2\n3\n4\n4\n4')

    def test_len(self):
        # Test length of an empty list
        x = task1.ListADT(20)
        self.assertEqual(len(x), 0, msg="Length of empty list should be 0")
        # And for a non-empty one
        x.insert(0, 2)
        self.assertEqual(len(x), 1, msg="Length should be 1")

        # Testing negative indices on list size
        x.insert(-1, 3)
        self.assertNotEqual(len(x), 4, msg="Length should not be 4")
        self.assertEqual(len(x), 2, msg="Length should be 2")

    def test_get(self):
        x = task1.ListADT(10)
        append(x, [0, 1, 2, 3, 4])

        # Check both positive and negative indices
        for index, value in [(1, 1), (-2, 3)]:
            self.assertEqual(x[index], value, msg="Incorrect _getitem_.")

        # Checks to see if index error is raised when out of range
        with self.assertRaises(IndexError, msg="Should have raised an index error"):
            x[-11]
        with self.assertRaises(IndexError, msg="Should have raised an index error"):
            x[-6]
        with self.assertRaises(IndexError, msg="Should have raised an index error"):
            x[6]

    def test_set(self):
        x1 = task1.ListADT(10)
        append(x1, [1, 2, 3])
        # Testing assignment (and implicitly _getitem_)
        x1[0] = 8
        self.assertTrue(equal(x1, [8, 2, 3]), msg="Incorrect assignment at index 0")

        # Checks to see whether it throws IndexError for out of range sets
        with self.assertRaises(IndexError, msg="Should have raised an index error"):
            x1[3] = 4

        with self.assertRaises(IndexError, msg="Should have raised an index error"):
            x1[-4] = 4

    def test_eq(self):
        x1 = task1.ListADT(10)
        x2 = task1.ListADT(20)
        # Check equality for lists of different size
        self.assertTrue(x1 == x2, msg="Lists with different capacity should still be equal.")
        # Check that equality tests for List type.
        append(x1, [1, 2, 3])
        self.assertFalse(x1 == [1, 2, 3], msg="Equality test doesn't check type.")
        append(x2, [1, 2, 3])

        # Checks to see whether objects of the same ListADT class with the same list are equal
        self.assertTrue(x1 == x2, msg="Different objects of ListADT with same elements should be equal")

        # Checks to see whether objects of the same ListADT class with different lists are not equal
        append(x2, [1])
        self.assertFalse(x1==x2, msg="Different objects of ListADT should not be equal if elements are different")

    def test_insert(self):
        x = task1.ListADT(10)
        # Check insertion at beginning
        x.insert(0, 1)
        self.assertTrue(equal(x, [1]), msg="Insertion in empty list failed")
        # And at end.
        x.insert(1, 2)
        self.assertTrue(equal(x, [1, 2]), msg="Insertion at end failed")

        # Check insertion out-of-bounds
        with self.assertRaises(IndexError, msg="Inserting out of bounds should fail"):
            x.insert(6, 8)

        with self.assertRaises(Exception, msg="Inserting above capacity should raise an exception."):
            append(x, [1 for i in range(20)])

        # Checks to see whether inserting on a negative index gives correct result
        for i in range(10):
            x.delete(0)
        x.insert(0, 1)
        x.insert(-1, 3)
        self.assertTrue(equal(x, [1, 3]), msg="Reverse index insertion failed")

        # Checks to see whether inserting on a negative index limits gives correct result
        x.insert(-2, 4)
        self.assertTrue(equal(x, [1, 4, 3]), msg="Reverse index insertion failed")

        # Checks to see whether inserting on a non integer index throws a TypeError
        #with self.assertRaises(TypeError, msg="Should throw a TypeError"):
        #    x.insert("potato", "peaches")

    def test_delete(self):
        x = task1.ListADT(10)
        append(x, [0, 1, 2, 3, 4, 5])
        # Test deletion from the middle.
        x.delete(2)
        self.assertTrue(equal(x, [0, 1, 3, 4, 5]), msg="Delete from middle failed")
        # And from a negative index.
        x.delete(-4)
        self.assertTrue(equal(x, [0, 3, 4, 5]), msg="Negative deletion failed")

        # Checks to see whether it throws an IndexError for deleting an out of range element
        with self.assertRaises(IndexError, msg="Should throw an IndexError"):
            x.delete(9)

        # Checks to see whether it throws a TypeError for deleting at a non integer index
        with self.assertRaises(TypeError, msg="Deleting string indexes throw a TypeError"):
            x.delete("4")


if __name__ == '__main__':
    unittest.main()
