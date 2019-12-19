import math
import unittest
from test_common import *
import task2
import task4

class TestTask4(unittest.TestCase):
  def test_read(self):
    ed = task4.Editor()
    ed.read_filename('TestFile.txt')
    self.assertTrue(equal_lines(ed, test_content), msg =  "File not correctly read.")

  def test_print(self):
    pass

  def test_delete(self):
    ed = task4.Editor()
    ed.read_filename('TestFile.txt')
    ed.delete_num("1")
    self.assertTrue(equal_lines(ed, test_content[1:]), msg =  "Failed to delete first line.")
   
    for index in ["-5"]:
      with self.assertRaises(IndexError, msg = "Deleting out-of-bounds lines should fail."):
        ed.read_filename('TestFile.txt')
        ed.delete_num(index)

    for index in ["potato"]:
      with self.assertRaises(IndexError, msg = "Should only delete from a numbered line"):
        ed.read_filename('TestFile.txt')
        ed.delete_num(index)

    for index in ["0"]:
      with self.assertRaises(IndexError, msg="Cannot delete at line 0"):
        ed.read_filename('TestFile.txt')
        ed.delete_num(index)

    ed.read_filename('TestFile.txt')
    ed.delete_num("-1")
    test_list = ['This is a test file\n', 'It is a file that is used for testing.\n', 'It has several lines.\n', None,
                  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                  None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                  None, None]

    self.assertEqual(ed.text_lines.the_array, test_list, "Failed to delete last line.")
    self.assertEqual(len(ed.text_lines), 3, "Failed to resize list after user deletion")

  def test_insert(self):
    ed = task4.Editor()
    ed.insert_num_strings("1", ToListADT(task2.ListADT, [test_content[0]]))
    self.assertTrue(equal_lines(ed, [test_content[0]]), msg =  "Failed to insert single line.")

    ed = task4.Editor()
    ed.insert_num_strings("-1", ToListADT(task2.ListADT, [test_content[2], test_content[3]]))
    self.assertTrue(equal_lines(ed, [test_content[2], test_content[3]]), msg =  "Incorrect handling of negative insertion")

    with self.assertRaises(IndexError, msg="List should raise Index Error when out of range"):
      ed = task4.Editor()
      ed.insert_num_strings("1000", ToListADT(task2.ListADT, [test_content[2], test_content[3]]))

    for index in ["0"]:
      with self.assertRaises(IndexError, msg="Cannot insert at line 0"):
        ed.insert_num_strings(index,"test")

if __name__ == '__main__':
  unittest.main()