from tour import Tour

def knight():
    """The user interface function that creates an instance of the Tour class to modify the tour based
    on the users input

        :param          None
        :post           Uses the instance map1 to access the Tour class and its functions
        :complexity:    best case: O(1), worst case: O(n^3)"""
    map1 = Tour()
    while (True):
        try:
            userinput = int(input("[1] Position\n[2] Quit\n[3] Move\n[4] Undo\n"
                                "[5] Save\n[6] Load save\nInput: "))
        except ValueError:
            print("Error! You did not enter a proper integer")
            continue

        if userinput == 1:
            map1.show_tour()

        elif userinput == 2:
            return

        elif userinput == 3:
            validMove = False
            while validMove == False:
                try:
                    xinput = int(input("enter x "))
                    yinput = int(input("enter y "))
                except ValueError:
                    print("Error! You did not input a proper data type")
                    continue

                if map1.valid_move((xinput, yinput)) is True:
                    print('successful move')
                    map1.move_knight(xinput, yinput)
                    validMove = True
                else:
                    print('invalid move')

        elif userinput == 4:
            map1.undo()

        elif userinput == 5:
            saveData = map1.copy()
            #print(saveData.the_array)

        elif userinput == 6:
            try:
                map1.set(saveData)
            except UnboundLocalError:
                print("No save data!")
    return

knight()
