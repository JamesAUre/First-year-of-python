# function declaration with parameters
def bubblesort (the_list):

    # saving the amount of elements in 'the_list' into variable n as an int
    n = len(the_list)

    # initializing for loop for length of list - 1
    for a in range(n-1):

        # initializing double for loop for length of list - 1
        for i in range(n-1):

            # copying element in list being pointed to by second for loop into variable 'item'
            item = the_list[i]

            # copying element next in list being pointed to by second for loop into variable 'item_to_right'
            item_to_right = the_list[i+1]

            # comparing whether item is greater than item to right
            if item > item_to_right:

                # if yes then switch item with item to right
                the_list[i] = item_to_right
                the_list[i+1] = item