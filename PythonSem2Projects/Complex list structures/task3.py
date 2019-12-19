from task2 import ListADT


def read_text_file(fileName):
    """
    Reads the string from a text file line by line and inputs each line of strings into its own element in an
    object of the ListADT class.

    :pre condition: fileName is a string
    :post condition: fileList is an object of ListADT containing a list
    :Big O worst time complexity: O(N) where N is the number of lines in the file 'fileName'
    :Big O best time complexity: O(N) where N is the number of lines in the file 'fileName'
    :param: fileName (the name of the file that will be used)
    :return: fileList (an object of ListADT that contains a list with an element of each line in the file)
    """

    fileList = ListADT()
    with open(fileName) as file:
        for line, content in enumerate(file, 1):
            fileList.insert(line-1, content)

    return fileList

OMGITSALIST = read_text_file('small.txt')