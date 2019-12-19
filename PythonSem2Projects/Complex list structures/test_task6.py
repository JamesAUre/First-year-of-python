import math
import unittest
from test_common import *
import task2
import task6


class TestTask6(unittest.TestCase):
  def test_undo(self):
    ed = task6.Editor()
    
    extra_lines = [ "These are some extra lines.", "They are will be added to the string." ]

    ed.read_filename('TestFile.txt')

    ed.delete_num("")
    ed.insert_num_strings("1", ToListADT(task2.ListADT, extra_lines))

    ed.undo()
    self.assertTrue(equal_lines(ed, []))
    ed.undo()
    self.assertTrue(equal_lines(ed, test_content))
    with self.assertRaises(Exception, msg = "Undoing past the beginning of history should have failed."):
      ed.undo()

    ed.delete_num()
    ed.insert_num_strings("1", ["test", "test1"])
    ed.insert_num_strings("2", ["1", "2", "3"]) # do 3 commands
    ed.undo() # try undo without any parameter given (overloading)
    self.assertTrue(equal_lines(ed, ["test", "test1"])) # 1 undo means pop 1 off stack adt
    ed.delete_num("2")  # user operation
    ed.insert_num_strings("1", ["begone", "after undo"]) # user operation
    ed.undo() # should undo previous insert operation
    self.assertTrue(equal_lines(ed, ["test"])) # will continue to work even after undoing beforehand
    ed.undo()
    self.assertTrue(equal_lines(ed, ["test", "test1"])) # should work even after 2nd consecutive undo

    ed.read_filename('small.txt')
    with self.assertRaises(Exception, msg="Shouldn't be able to undo after reading another file."):
      ed.undo()
if __name__ == '__main__':
  unittest.main()
