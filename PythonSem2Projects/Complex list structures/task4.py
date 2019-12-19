from task3 import read_text_file
from task2 import ListADT


class Editor:
    def __init__(self):
        """
        A constructor of the Editor class, initializes each instantiation of the class

        :post condition: an instance of the class Editor will be created
        :Big O worst time complexity: O(1)
        :Big O best time complexity: O(1)
        """
        self.text_lines = ListADT(0)


    def read_filename(self, file_name):
        """
        This function will call the read_text_file(file_name) function and store each line of the file with the file
        name inputted into the ListADT self.text_lines

        :pre condition: 'file_name' is a string
        :post condition: the current instance of text_lines will contain an element for each line in the file
        :Big O worst time complexity: O(N) where N is the number of lines in the file name inputted
        :Big O best time complexity: O(N) where N is the number of lines in the file name inputted
        :param: file_name (the name of the file that will be used)
        """
        try:
            self.text_lines = read_text_file(file_name)
        except FileNotFoundError:
            raise IndexError

    def print_num(self, line_num=""):
        """
        Prints the element at the index 'line_num'-1 in the current instances self.text_lines
        if a line is not specified in 'line_num', print all the elements in self.text_lines instead

        :pre condition: line_num can either be a number or have no value
        :post condition: prints a statement on the console
        :Big O worst time complexity: O(N) where N is the length of the length of the ListADT self.text_lines
        :Big O best time complexity: O(1) if the line_num to read from is specified
        :param: line_num (this will indicate which element to read from or whether to read the entire list)
        """
        if line_num != "":
            try:
                line_num = int(line_num) - 1
            except ValueError:
                raise IndexError
            print(self.text_lines[line_num])

        if line_num == "":
            print(str(self.text_lines))


    def delete_num(self, line_num=""):
        """
        Deletes the element in the ListADT self.text_lines at index line_num - 1 if line_num is positive and at
        line_num if line_num is negative. Cannot delete at line_num = 0. If no line_num value is specified, it will
        delete all the elements of the ListADT self.text_lines

        :pre condition: line_num can either be a number or have no value
        :post condition: self.text_lines will delete the element at a specified index or all if no index specified
        :Big O worst time complexity: O(K*N*M) where N is the maximum capacity of the ListADT self.text_lines, M
        is the number of elements between index and the last element in the ListADT and K is the length of the ListADT
        :Big O best time complexity: O(N*M) where N is the maximum capacity of the ListADT self.text_lines and M
        is the number of elements between index and the last element in the ListADT.
        :param: line_num (this will indicate which element to delete or whether to delete every element)
        """

        if line_num != "":
            try:
                line_num = int(line_num)

            except ValueError:
                raise IndexError

            if line_num < 0:
                self.text_lines.delete(line_num)
            elif line_num > 0:
                line_num -= 1
                self.text_lines.delete(line_num)
            else:
                raise IndexError

        else:
            while self.text_lines.is_empty() is False:
                self.text_lines.delete(0)

    def insert_num_strings(self, line_num, lines):
        """
        Inserts a list 'lines' from the index 'line_num'-1 if line_nums is positive and at line_nums if line_nums is
        negative in the ListADT self.text_lines. Cannot insert at line_num = 0.

        :pre condition: line_num can either be a number or hold no value, lines must be a list
        :post condition: will insert 'lines' at 'line_num' within the ListADT self.text_lines
        :Big O worst time complexity: O(N*M) where N is the number of elements to the right of the element 'line_num'
        in self.text_lines ListADT and M is the number of elements in the ListADT 'lines'.
        :Big O best time complexity: O(N*M) where N is the number of elements to the right of the element 'line_num'
        in self.text_lines ListADT and M is the number of elements in the ListADT 'lines'.
        :param: line_num (this will indicate which element to insert from)
        :param: lines (this will contain the list which will be inserted from line_num in self.text_lines)
        """
        try:
            line_num = int(line_num)
        except ValueError:
            raise IndexError

        if line_num < 0:
            for i in range(len(lines)):
                self.text_lines.insert(line_num - i, lines[len(lines)-i-1])

        elif line_num > 0:
            line_num -= 1
            for i in range(len(lines)):
                self.text_lines.insert(line_num + i, lines[i])
        else:
            raise IndexError

    def search_string(self, query):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError

