def print_menu():
    print("\nMenu:")
    print("1. append")
    print("2. pop")
    print("3. count")
    print("4. reverse")
    print("5. print")
    print("6. quit")

def reverse(my_list):
    length = len(my_list)
    for i in range(length//2):
        temp = my_list[i]
        my_list[i] = my_list[length -i-1]
        my_list[length -i-1]=temp

my_list = []
quit = False
input_line = None

def pop(my_list):
    lenlist = len(my_list)
    newlist = []
    #print(my_list[lenlist])
    for i in range(lenlist-1):
        newlist.append(my_list[i])

    return newlist

def counting(my_list, countfor):
    counter = 0
    for i in range(len(my_list)):
        if my_list[i] == countfor:
            counter+=1
    return counter

while not quit:
    print_menu()
    command = int(input("\nEnter command: "))

    if command == 1:
        item = input("Item? ")
        my_list.append(item)
    elif command == 2:
        my_list = pop(my_list)
        print(my_list)
    elif command == 3:
        countinput = input("Count for which item? ")
        print(counting(my_list, countinput))
    elif command == 4:
        reverse(my_list)
    elif command == 5:
        print(my_list)
    elif command == 6:
        quit = True