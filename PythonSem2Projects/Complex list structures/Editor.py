from task6 import Editor
from task2 import ListADT

def userprompt():
    userinput = ""
    userTokens = ListADT()
    userSesh = Editor()
    while userinput != "quit":
        while userTokens.is_empty() is False:
            userTokens.delete(0)
        userinput = input("Enter command: ")

        try:
            for i in range(len(userinput.split(" "))):
                userTokens.insert(i, userinput.split(" ")[i])

            if userTokens[0] == "read":
                userSesh.read_filename(userTokens[1])

            elif userTokens[0] == "print":
                if len(userTokens) == 1:
                    userSesh.print_num()

                elif len(userTokens) > 1:
                    userSesh.print_num(userTokens[1])

            elif userTokens[0] == "delete":
                if len(userTokens) == 1:
                    userSesh.delete_num()
                elif len(userTokens) > 1:
                    userSesh.delete_num(userTokens[1])

            elif userTokens[0] == "insert":
                insertList = ListADT(0)
                userinput = ""

                try:
                    userTokens[1] = int(userTokens[1])
                except ValueError:
                    raise IndexError

                while userinput != ".":
                    userinput = input("Enter line to insert into list: ")
                    insertList.append(userinput)

                insertList.delete(len(insertList)-1)

                userSesh.insert_num_strings(userTokens[1], insertList)

            elif userTokens[0] == "search":
                searchList = userSesh.search_string(userTokens[1])

                for i in range(len(searchList)):
                    #print("Line number ", searchList[i], ": ", end="")
                    userSesh.print_num(searchList[i])

            elif userTokens[0] == "undo":
                userSesh.undo()

            elif userTokens[0] != "quit":
                raise IndexError

        except IndexError:
            print("?")
    return

userprompt()