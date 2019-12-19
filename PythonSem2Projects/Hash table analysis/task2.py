from task1 import HashTable
import timeit
import csv


def load_dictionary(hashtable, filename, timelimit=None):
    """
    Tries to put each line in the file 'filename' into the hashtable before the timelimit. If
    timelimit is reached it will stop adding to the hashtable and return a TimeoutError.

    :pre condition: hashtable is a HashTable object, filename is a string containing the name of a file
    to open and timelimit is an integer containing the maximum amount of time for the function to run.
    :post condition: hashtable will contain lines from the file filename till it ran out of time to hash them in.
    :worst time complexity: O(N*M+K) where where N is the number of lines in the file 'filename', M is the length
    of the hashtable and K is the length of the key (content)
    :best time complexity: O(N+K) where N is the number of lines in the file 'filename' and K is the length
    of the key (content)
    :param hashtable: an object of the HashTable class
    :param filename: contains the name of the file to read lines from
    :param timelimit: contains the maximum amount of time for the function to run for
    """
    starterTimer = timeit.default_timer()
    with open(filename) as file:
        for line, content in enumerate(file, 1):
            #starterTimer = timeit.default_timer()
            hashtable[content.replace("\n", "")] = 1
            #print(starterTimer, timelimit)
            if timelimit is not None:
                endtimer = timeit.default_timer() - starterTimer
                if endtimer > timelimit:
                    raise TimeoutError


def load_dictionary_time(hash_base, table_size, filename, max_time):
    """
    Times how long it takes for the load dictionary function to run and if it throws a TimeoutError
    it'll set the time as None. It then returns the amount of words in the hashtable and the time taken.

    :pre condition: hash_base must be an integer, table_size must be an integer, filename must be a string
    containing the name of the file being used, max_time is an integer containing the maximum amount of time for
    the function load dictionary to run.
    :post condition: will have hashed all lines from the file filename into the hashtable, and timed it.
    :worst time complexity: O(N*M+K) where where N is the number of lines in the file 'filename' and M is the length
    of the hashtable and K is the length of the key (content)
    :best time complexity: O(N+K) where N is the number of lines in the file 'filename' and K is the
    length of the keys
    :param hash_base: an integer containing the base of the hash table object
    :param table_size: an integer containing the size to set the hashtable object to
    :param filename: a string containing the name of the file to open
    :param max_time: an integer containing the maximum amount of time for the load_dictionary function to run for
    :return hashtable.count: The amount of words added to the hashtable object
    :return time: The time taken for the load_dictionary function to complete
    """

    hashtable = HashTable(table_size, hash_base)

    startTimer = timeit.default_timer()
    try:
        load_dictionary(hashtable, filename, max_time)
        endTimer = timeit.default_timer() - startTimer
        time = endTimer
    except TimeoutError:
        time = None

    print("seconds: ", time)
    return hashtable.count, time


def table_load_dictionary_time(max_time):
    """
    Stores all combinations between blist and sizelist and each file and stores all the data as rows in
    the output_task2.csv file

    :pre condition: max_time must be an integer, and there must be files available to read from
    :post condition: output_task2.csv will contain rows for each combination of data and the results produced
    from them.
    :worst time complexity:O(N*M+K) where N is the number of lines in each file, and M is the length of
    the hashtable and K is the length of the keys used
    :best time complexity: O(N+K) where N is the number of lines in each file and K is the length of the
    keys used
    :param max_time: the maximum amount of time each combination of data can run for before stopping.
    """
    blist = [1, 27183, 250726]
    filelist = ["english_large.txt", "english_small.txt", "french.txt"]
    sizelist = [250727, 402221, 1000081]
    with open('output_task2.csv', 'w', newline='') as f:
        thewriter = csv.writer(f, delimiter=',')
        for file in filelist:
            for b in blist:
                for size in sizelist:
                    print(file, b, size)
                    words, time = load_dictionary_time(b, size, file, max_time)

                    if time is None:
                        thewriter.writerow([file, b, size, words, max_time+10])
                    else:
                        thewriter.writerow([file, b, size, words, time])

table_load_dictionary_time(120)