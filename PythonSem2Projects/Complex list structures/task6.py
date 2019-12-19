from task3 import read_text_file
from task2 import ListADT
from task2 import ListADT as StackADT

class Editor:
    def __init__(self):
        """
        A constructor of the Editor class, initializes each instantiation of the class

        :post condition: an instance of the class Editor will be created
        :Big O worst time complexity: O(1)
        :Big O best time complexity: O(1)
        """
        self.text_lines = ListADT(0)
        self.stack = StackADT(0)

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

        while(self.stack.is_empty() is False):
            self.stack.pop()

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
                #
                self.stack.append(['D', line_num, self.text_lines[line_num]])
                self.text_lines.delete(line_num)

            elif line_num > 0:
                line_num -= 1
                #
                self.stack.append(['D', line_num, self.text_lines[line_num]])
                self.text_lines.delete(line_num)

            else:
                raise IndexError

        else:
            self.stack.append(['C'])
            while self.text_lines.is_empty() is False:
                self.stack[len(self.stack)-1].append(self.text_lines[0])
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

        linelength = len(lines)
        if line_num < 0:
            self.stack.append(['I', line_num, linelength])

            for i in range(linelength):
                self.text_lines.insert(line_num - i, lines[linelength-i-1])
            # self.stackADT.append(self.text_lines)
        elif line_num > 0:
            line_num -= 1
            self.stack.append(['I', line_num, linelength])
            for i in range(linelength):
                self.text_lines.insert(line_num + i, lines[i])
            # self.stackADT.append(self.text_lines)
        else:
            raise IndexError


    def search_string(self, query):
        """
        Searches for whether the string 'query' occurs within any elements of the ListADT self.text_lines, the function
        then stores all the line numbers where query appeared and returns these line numbers as a ListADT.

        :pre condition: query must be a string
        :post condition: a list must be returned, the ListADT self.text_lines should remain unchanged
        :Big O worst time complexity: O(N*K) where N is the total number of characters across all elements
        in ListADT self.text_lines and K is the length of the search query
        :Big O best time complexity: O(N) where N is the total number of characters across all elements
        in ListADT self.text_lines
        :param: query (this will be the string that is searched for in each element of ListADT self.text_lines)
        :return: linesFound (a list containing all the lines which 'query' appears in)
        """
        if query == "":
            raise IndexError
        linesFound = ListADT()

        # loops through each ELEMENT of text_lines
        for i in range(len(self.text_lines)):
            linelength = len(self.text_lines[i])

            # loops through each CHARACTER of the element
            for j in range(len(self.text_lines[i])):
                if query[0] == self.text_lines[i][j] and len(query) <= linelength:
                    flag = True
                    for k in range(1, len(query)):
                        if query[k] != self.text_lines[i][j + k]:
                            flag = False
                    if flag is True:
                        linesFound.append(i + 1)
                        break
                linelength -= 1

        return linesFound


    def undo(self):
        """
        Uses the stack stackADT to see what the last operation done by the user was and uses the information
        provided on the stack to reverse the users operation.

        :post condition: self.text_lines will contain the list from before the last operation done by the user
        :Big O worst time complexity: O(N*M*K) - where N is the maximum capacity of the text_lines list, M
        is the number of elements between index and the last element in the list and K is the number of elements in the
        stack which need to be deleted in self.text_lines
        :Big O best time complexity: O(1) if stack is empty

        """

        if self.stack.is_empty():
            raise IndexError

        # FOR DELETING 1 ELEMENT
        if self.stack[len(self.stack)-1][0] == 'D':
            self.text_lines.insert(self.stack[len(self.stack)-1][1], self.stack[len(self.stack)-1][2])

        # FOR DELETING ALL ELEMENTS
        elif self.stack[len(self.stack) - 1][0] == 'C':
            for i in range (1, len(self.stack[len(self.stack) - 1])):
                self.text_lines.append(self.stack[len(self.stack) - 1][i])

        # FOR INSERTING ELEMENTS
        elif self.stack[len(self.stack) - 1][0] == 'I':
            for i in range(self.stack[len(self.stack) - 1][2]):
                self.text_lines.delete(self.stack[len(self.stack) - 1][1])
        self.stack.pop()

            # self.stack.delete(len(self.stack) - 1)


