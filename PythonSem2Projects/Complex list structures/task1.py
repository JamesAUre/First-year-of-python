class ListADT:

    def __init__(self, size = 40):
        """
        A constructor of the ListADT class, initializes each instantiation of the class (creates the objects)

        :pre condition: the current object must contain a list attribute and 'size' must be a positive integer
        :post condition: will create an object
        :Big O worst case time complexity: O(1)
        :Big O best case time complexity: O(1)
        :param: size (initial size of the list)
        """
        self.length = 0
        try:
            self.the_array = [None] * size
        except TypeError:
            raise TypeError("The list size must be an integer")
            # raise TypeError("The list size must be an integer")
        self.max_size = size


    def __str__(self):
        """
        Turns the elements of the current list object into one string where each element is on a different line

        :pre condition: the current object must contain a list attribute
        :post condition: creates a string 'stringList' and stores all elements of the current list object in it.
        :Big O worst case time complexity: O(N) where N is the length of the current object
        :Big O best case time complexity: O(N) where N is the length of the current object
        :return: stringList (the string containing each element of the list object)
        """
        stringList = ""
        for i in range(0, self.length):
            if self.the_array[i] == None:
                stringList = stringList + ""
            else:
                stringList += str(self.the_array[i]) + "\n"
        return stringList

    def __len__(self):
        """
        Calculates the length of the current list object (number of elements)

        :pre condition: the current object must contain a list attribute
        :post condition: retrieves the length attribute associated with the current object its in
        :Big O worst case time complexity: O(1)
        :Big O best case time complexity: O(1)
        :return: self.length (the length of the current objects list)
        """
        return self.length

    def __getitem__(self, index):
        """
        Looks at the index given and goes through the list to find the element at the given index

        :pre condition: the current object must contain a list attribute and index must be an integer between -len(self)
                        to len(self)-1
        :post condition: Retrieves the element in the list at the given index
        :Big O worst case time complexity: O(1)
        :Big O best case time complexity: O(1)
        :param: index (the position of the element in the list that will be retrieved)
        :return: self.the_array[index] - the content of the element in the position of index
        """
        try:
            if index < len(self) and index >= -1 * len(self):
                index = self.calculate_index(index)
                return self.the_array[index]
            else:
                raise IndexError

        except IndexError:
            raise IndexError("Index not in list")

    def __setitem__(self, index, item):
        """
        Writes the input 'item' into the list at element number 'index'. Data previously in the list will be overwritten.

        :pre condition: the current object must contain a list attribute, index must be an integer between -len(self)
                        to len(self)-1, item must be a variable
        :post condition:item will be overwritten at the given index
        :Big O worst case time complexity: O(1)
        :Big O best case time complexity: O(1)
        :param: index (the position of the element in the list that will be retrieved)
        :param: item (the item you wish the enter into the element at position 'index' on the list object)
        """
        try:
            if index < len(self) and index >= -1 * len(self):
                index = self.calculate_index(index)
                self.the_array[index] = item
            else:
                raise IndexError

        except IndexError:
            raise IndexError("Index not in list")

    def __eq__(self, other):
        """
        Checks if the list of the current object is equal to the list 'other' (all elements are the same, lengths
        of the lists are equal and the type of the lists are the same)

        :pre condition: the current object must contain a list attribute, input 'other' must be a list
        :post condition: The state of both lists will remain unchanged, this function is pure.
        :Big O worst time complexity: O(N) where N is the length of the list in the current object
        :Big O best time complexity: O(N) where N is the length of the list in the current object
        :param: other (the list which the current object is being compared to)
        :return: True if the lists are equal and False otherwise
        """
        if type(self) == type(other):
            for i in range(self.length):
                if self.the_array[i] != other[i]:
                    return False
            if self.length != len(other):
                return False
            return True
        return False

    def __contains__(self, item):
        """
        Checks if the the current object list contains an item within one of its elements
        the item must be equal to the element, e.g. not part of the element or vice versa.

        :pre condition: the current object must contain a list attribute, item must be a variable
        :post condition: The state of the list will remain unchanged, the function is pure
        :Big O worst time complexity: O(N) where N is the length of the list in the current object
        :Big O best time complexity: O(N) where N is the length of the list in the current object
        :param: item (the item you wish the enter into the element at position 'index' on the list object)
        :return: True if the list contains the data in 'item' and False otherwise
        """
        for i in range(self.length):
            if item == self.the_array[i]:
                return True
        return False

    def calculate_index(self, index):
        """
        Finds the index initially inputted and converts the inputted index to a value
        that the object can use as a list index

        :pre condition: the current object must contain a list attribute, index must be an integer
        :post condition: it will give an index value the current objects list can use
        :Big O worst time complexity: O(1)
        :Big O best time complexity: O(1)
        :param: index (the inputted index that needs to be converted)
        :return: index (the index that the current object list will use), 0 if the length of the list object is 0
        """
        if self.length == 0:
            return 0
        else:
            index = (index % self.length)
            return index

    def is_empty(self):
        """
        Checks to see whether there are no elements in the current objects list

        :pre condition: the current object must contain a list attribute
        :post condition: the function is pure and will only return a boolean value
        :Big O worst time complexity: O(1)
        :Big O best time complexity: O(1)
        :return: True if the list is empty (length of the list is 0) and False otherwise
        """
        return self.length == 0

    def insert(self, index, item):
        """
        Puts the input 'item' into the objects list at the index of 'index' and shifts everything to the right of the
        index by 1 before inserting the item into the empty cell in the list.

        :pre condition: the current object must contain a list attribute, index must be an integer between -len(self)-1
        and len(self) and item must be a variable
        :post condition: the objects list will increase by 1 and have inserted the element 'item' into the list at
        location 'index' in the parameters
        :Big O worst time complexity: O(N) where N is the number of elements in the list object to the right of location
        index
        :Big O best time complexity: O(N) where N is the number of elements in the list object to the right of location
        index
        :param: index (the location of the list where the element will be inserted to)
        :param: item (the item you wish the enter into the element at position 'index' on the list object)
        """
        try:
            if self.is_full() is False and index <= self.length and index >= -1 * self.length - 1:
                self.length += 1
                index = self.calculate_index(index)
                for i in range(self.length - 2, index - 1, -1):
                    self.the_array[i + 1] = self.the_array[i]
                self.the_array[index] = item

            elif self.is_full() is False:
                raise IndexError("Index not in list")

            elif self.is_full() is True:
                raise Exception("List is full")

        except TypeError:
            raise TypeError("Index and item must be integers")

    def delete(self, index):
        """
        Deletes an item in the lists object in location 'index' and shifts all elements to the right of the index by 1
        to the left to fill the empty space.

        :pre condition: the current object must contain a list attribute, index must be an integer between -len(self)
        to len(self)-1
        :post condition: the objects list will decrease by 1 and delete the element currently at location 'index' and
        fill in the gap by shifting all elements to the right of it by 1 to the left.
        :Big O worst time complexity: O(N) where N is the number of elements between index and the last element in the
        list.
        :Big O best time complexity: O(N) where N is the number of elements between index and the last element in the
        list.
        :param: index (the location of the element in the list that will be deleted)
        """
        try:
            if index < len(self) and index >= -1 * len(self):

                index = self.calculate_index(index)
            else:
                raise IndexError("Index not in list")

            for i in range(index, self.length - 1):
                self.the_array[i] = self.the_array[i + 1]

            self.the_array[self.length - 1] = None
            self.length -= 1

        except TypeError:
            raise TypeError("Index must be an integer")

    def is_full(self):
        """
        Checks whether the objects list is full or not

        :pre condition: the current object must contain a list attribute
        :post condition: the function is pure and will only return a boolean value
        :Big O worst time complexity: O(1)
        :Big O best time complexity: O(1)
        :return: True if the number of elements in the list has reached its maximum capacity, False otherwise.
        """
        return self.length == self.max_size

    def append(self, item):
        """
        Adds the item inputted onto the end of the objects list

        :pre condition: the current object must contain a list attribute, item must be a variable
        :post condition: the elements in the list currently will remain unchanged however if the list is not full
        the last element will contain the item, otherwise the list will remain unchanged
        :Big O worst time complexity: O(1)
        :Big O best time complexity: O(1)
        :param: item (the item you wish to append to the end of the objects list)
        """
        print('test')
        if not self.is_full():
            self.the_array[self.length] = item
            self.length += 1
        else:
            raise Exception('List is full')

    def unsafe_set_array(self, array, length):
        """
        Retrieves an array and a length and hard sets the array structure of the objects list to 'array'
        and the objects list length to 'length'.

        :pre condition: the current object must contain a list attribute, array must be an array and length must
        be an integer.
        :post condition:
        :Big O worst time complexity: O(1)
        :Big O best time complexity: O(1)
        :param array:
        :param length:
        :return:

        UNSAFE: only to be used during testing to facilitate it!! DO NOT USE FOR ANYTHING ELSE
        """
        if 'test' not in __name__:
            raise Exception('Not runnable')

        self.the_array = array
        self.length = length