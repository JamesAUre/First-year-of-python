from unsorted_list import List

class Tour:
    board_rows = 8
    board_cols = 8
    board_size = board_rows * board_cols
    
    def __init__(self):
        """Creates an empty object of the class (a constructor). Sets the starting position
        and how many moves the tour needs to take in order to complete every tile on the board

        @:param         None
        @:post          an empty list of the size of the board with (1,1) as the first element
        @:complexity    best and worst case: O(n) where n is the size of the list because it has to set
        the elements in the list class."""

        # You may wish to add additional attributes to the object.
        self.moves = List(Tour.board_size)
        self.moves.add_last( (1, 1) ) # Set a starting position

    def move_knight(self, row, col):
        """moves the position of the knight on the board and stores its new location on the list

        @:param         row - the row of the board position
                        column - the column of the board position
        @:post          the same list in self.moves but with the new tuple added to the end
        @:complexity    best and worst case: 0(1)"""
        assert self.moves.length() < Tour.board_size
        self.moves.add_last( (row, col) )

    def show_tour(self):
        """Prints the position of the knight and all the previous tiles it visited on an ascii table

        @:param         None
        @:post          a print statement on the console displaying in an ASCII table the tiles that are unvisited,
        visited and contain the knight
        @:complexity    best/worst case: O(n^3) where n is the size of a row / column of the board
                        """
        for r in range(1, Tour.board_rows+1):
            for c in range(1, Tour.board_cols+1):
                pos = self.moves.index( (r, c) )
                cell_char = '| '
                if pos is not None:
                    if pos == self.moves.length()-1:
                        cell_char = '|♘'
                    else:
                        cell_char = '|*'
                print(cell_char, end='')
            print(' ')

    def next_moves(self):
        """Checks the tile the knight is on and all previously visited tiles and
        gives a list of all possible tiles the knight can potentially move to in 1 turn

        @:param         None
        @:return        An object of potential tiles the knight can move to
        @:post          A new object 'outputMoves' part of the list class, length of object is equal to
                        the number of possible moves.
        @:complexity    best and worst case: O(n^3), where n is the number of board rows,
                        board columns and length of the tour

        """
        outputMoves = List(8)
        for i in range(1, Tour.board_rows+1):
            for j in range(1, Tour.board_cols+1):
                #scanning element vs last element

                if self.moves.index((i , j)) == self.moves.length()-1:

                    if self.moves.index((i-2,j+1)) is None and i > 2 and j < self.board_cols:
                        outputMoves.add_last((i-2, j+1))
                    if self.moves.index((i-1, j+2)) is None and i > 1 and j < self.board_cols-1:
                        outputMoves.add_last((i-1, j+2))

                    if self.moves.index((i+2, j-1)) is None and i < self.board_rows-1 and j > 1:
                        outputMoves.add_last((i+2, j-1))
                    if self.moves.index((i+1, j-2)) is None and i < self.board_rows and j > 2:
                        outputMoves.add_last((i+1, j-2))

                    if self.moves.index((i-2, j-1)) is None and i > 2 and j > 1:
                        outputMoves.add_last((i-2, j-1))
                    if self.moves.index((i-1, j-2)) is None and i > 1 and j > 2:
                        outputMoves.add_last((i-1, j-2))

                    if self.moves.index((i+2, j+1)) is None and i < self.board_rows-1 and j < self.board_cols:
                        outputMoves.add_last((i+2, j+1))
                    if self.moves.index((i+1, j+2)) is None and i < self.board_rows and j < self.board_cols-1:
                        outputMoves.add_last((i+1, j+2))

        #print(outputMoves.the_array)
        return outputMoves

    def valid_move(self, move):
        """Compares the users choice of the next knight position and checks whether it's part of the object list
        outputMoves

        @:param         move - The players chosen position to move the knight to
        @:return        True - If the element exists in 'possibleMoves' created from the next_moves() function
                        False - If the element does't exist in 'possibleMoves' created form the next_moves() function
        @:pre           Must be a tuple of integers
        @:post          Empties the possibleMoves object
        @:complexity    best and worst case: O(n) where n is the length of the object list 'possibleMoves'"""

        "NEED TO CHECK FOR COORDINATE OFFSETS TOO"

        #if there is no element stored in list with that coordinate
        possibleMoves = self.next_moves()
        while possibleMoves.is_empty() is False:
            checkmove = possibleMoves.get_item(possibleMoves.length()-1)

            possibleMoves.delete_item(checkmove)
            if checkmove == move:
                return True
        return False

    def undo(self):
        """Undoes the latest move the user made with the knight

        @:param         None
        @:post          The list of the knight tour has its last element removed but all other elements are the same
        @:complexity    best and worst case: O(n) because the delete_items function has to traverse through the
                        list until it finds the element it's looking for"""

        try:
            assert self.moves.length() > 1
            self.moves.delete_item(self.moves.get_item(self.moves.length() - 1))

        except AssertionError:
            print("You must have atleast one of your moves")

    def copy(self):
        """Creates a save for the current state of the game in a return

        @:param         None
        @:return        An object 'saveList' containing saved data
        @:post          A new object 'saveList' is created of size rows*columns of the board, contains all
                        Moves the player made
        @:complexity    best and worst case: O(n) where n is the length of the tour object"""
        saveList = List(Tour.board_cols*Tour.board_rows)
        for i in range(self.moves.length()):
             saveList.add_last(self.moves.get_item(i))

        #saveList.the_array
        #print(saveList.the_array)
        return saveList

    def set(self,saveListObj):
        """Uses the save data from copy() as the new game state

        @:param         saveListObj - has the save data that will be made the state of the game
        @:post          Data from the savedListObj is now in the tour object making it the current state of
                        the game
        @:complexity    best and worst case: O(n) because it has to traverse through every element in saveListObj
        """
        # print(saveListObj)
        #while self.moves.is_empty() is False:
        #    self.undo()

        self.moves.reset()
        for i in range(saveListObj.length()):
            self.moves.add_last(saveListObj.get_item(i))

def test_move_knight():
    testKnight = Tour()

    testKnight.move_knight(3,3)
    assert testKnight.moves.the_array[0] == (1, 1)
    assert testKnight.moves.the_array[1] == (3,3)
    assert testKnight.moves.the_array[5] == None
    assert testKnight.moves.the_array[2] == None
    testKnight.move_knight(3,4)
    assert testKnight.moves.the_array[2] == (3,4)
    assert testKnight.moves.the_array[1] != None

def test_valid_moves():
    testMoves = Tour()
    assert testMoves.valid_move((2,3))
    assert not testMoves.valid_move((4,4))
    testMoves.move_knight(6,6)
    assert testMoves.valid_move((5,4))
    assert testMoves.valid_move((4,5))
    assert testMoves.valid_move((7,4))
    assert not testMoves.valid_move((4,4))
    assert not testMoves.valid_move((5,6))

def test_undo():
    testUndo = Tour()
    testUndo.move_knight(2,2)
    testUndo.move_knight(3,5)
    testUndo.move_knight(7,5)
    testUndo.undo()
    testUndo.undo()
    testUndo.move_knight(6,4)

    assert testUndo.moves.the_array[1] == (2, 2)
    assert testUndo.moves.the_array[2] == (6, 4)
    assert testUndo.moves.the_array[3] == (7, 5)
    assert testUndo.moves.the_array[4] == None
    assert testUndo.moves.the_array[0] == (1, 1)
    assert testUndo.moves.the_array[15] == None
    assert testUndo.moves.the_array[3] != (7, 6)

def test_copy():
    testCopy = Tour()
    assert testCopy.copy().the_array[0] == (1,1)
    assert testCopy.copy().the_array[1] == None
    testCopy.move_knight(3,3)
    assert testCopy.copy().the_array[1] == (3,3)
    assert testCopy.copy().the_array[0] == (1, 1)
    assert testCopy.copy().the_array[7] == None

def test_set():
    testSet = Tour()
    testSet2 = Tour()
    testSet2.move_knight(6,6)
    testSet2.move_knight(5,3)

    setVar = testSet2.copy()

    testSet.set(setVar)

    assert testSet.moves.the_array[0] == (1, 1)
    assert testSet.moves.the_array[1] == (6, 6)
    assert testSet.moves.the_array[2] == (5, 3)
    assert testSet.moves.the_array[2] != (3, 6)
    assert testSet.moves.the_array[5] == None
    assert testSet.moves.the_array[1] != None
    assert testSet.moves.the_array[0] != (6, 6)


if __name__ == '__main__':
    test_move_knight()
    test_valid_moves()
    test_undo()
    test_copy()
    test_set()
    print("all tests passed")

    #the_tour = Tour()

    #the_tour.move_knight(2, 3)
    #the_tour.move_knight(4, 2)
    #the_tour.show_tour()
