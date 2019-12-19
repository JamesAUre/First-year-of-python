def binary(number):
    """
    :param number: the decimal number the user wants to convert bases
    :return output the base 2 version of the decimal value 'number'
    :precondition: input must be an integer
    :postcondition: a string of digits 1 and 0 outputted into the console
    :complexity: best case O(Log n), worst case O(Log n) where n is the value of number
    """
    if number > 1:
        binary(number//2)
    print(number%2, end = "")

def hexadecimal(number):
    """
        :param number: the decimal number the user wants to convert bases
        :return output the base 16 version of the decimal value 'number'
        :precondition: input must be an integer
        :postcondition: a string of digits 0-9 and A,B,C,D,E,F outputted into the console
        :complexity: best case O(Log n), worst case O(Log n) where n is the value of number
        """
    if number > 15:
        hexadecimal(number//16)
    if number % 16 == 15:
        print('F', end = "")
    elif number % 16== 14:
        print('E', end = "")
    elif number % 16 == 13:
        print('D', end = "")
    elif number % 16 == 12:
        print('C', end = "")
    elif number % 16 == 11:
        print('B', end = "")
    elif number % 16 == 10:
        print('A', end = "")
    else: print(number%16, end = "")
hexadecimal(497)