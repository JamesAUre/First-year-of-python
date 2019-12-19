import timeit
import csv

class HashTable:
    def __init__(self, table_capacity=11, hash_base=1):
        """
        Creates an instance of the class HashTable

        :pre conditions: table capacity and hash base must be an integer
        :post conditions: it'll create an instance of the class HashTable with the values table capacity
        and hash base
        :worst time complexity: O(1)
        :best time complexity: O(1)
        :param table_capacity: the amount of empty elements you would like the hash table to contain
        :param hash_base: a number that will be used to hash values
        """
        self.table = [None] * table_capacity
        self.base = hash_base
        self.count = 0
        self.length = table_capacity

        self.collisions = 0
        self.probe_total = 0
        self.probe_max = 0
        self.rehash_count = 0

    def __getitem__(self, key):
        """
        Gets an item from the hashtable with the specified key (LINEAR PROBING)

        :pre conditions: key must be a string
        :post conditions: returns the value in the hash table that contains the key
        :worst time complexity: O(N+K) where N is the length of the hashtable and K is the length of
        key
        :best time complexity: O(K) where K is the length of key
        :param key: a string containing information for where to find the item on the hashtable
        :return: the item in the hashtable associated with the specified key, or KeyError if doesn't exist
        """
        location = self.hash(key)
        while self.table[location % self.length] is not None:
            if self.table[location % self.length][0] == key:
                return self.table[location % self.length][1]
            location += 1
        raise KeyError

    def __setitem__(self, key, item):
        """
        Sets an item from item into the hashtable with the specified key (LINEAR PROBING)

        :pre condition: key must be a string, item can be any value
        :post condition: hashtable will store the element [key, item] at specified key hash
        :worst time complexity: O(N+K) where N is the length of the hashtable and K is the length of key
        :best time complexity: O(K) where K is the length of key
        :param key: a string containing information for where to store the item on the hashtable
        :param item: contains the value that the user wants to store on the hashtable
        """
        if self.checkfull():
            self.rehash()
        index = self.hash(key)
        fixindex = index
        if self.__contains__(key):
            while self.table[index % self.length][0] != key:
                index += 1
        else:
            while self.table[index % self.length] is not None:
                index += 1
            self.count += 1

        if index != fixindex:
            if index - fixindex > self.probe_max:
                self.probe_max = index - fixindex
            self.probe_total += (index - fixindex)
            self.collisions += 1


        self.table[index % self.length] = [key, item]

    def __contains__(self, key):
        """
        Checks to see if a key exists in the hashtable (LINEAR PROBING)

        :pre condition: key must be a string
        :post condition: will have checked whether the key exists in the hashtable
        :worst time complexity: O(N+K) where N is the size of the hashtable and K is the length of key
        :best time complexity: O(K) and K is the length of the key
        :param key: a string containing information for where to look for the key and what key to look for
        :return: True if the key exists, False otherwise
        """
        location = self.hash(key)
        while self.table[location % self.length] is not None:
            if self.table[location % self.length][0] == key:
                return True
            location += 1
        return False

    def checkfull(self):
        """
        Checks whether the hashtable is full

        :worst time complexity: O(1)
        :best time complexity: O(1)
        :return: True if hashtable is full, False otherwise
        """
        if self.count == self.length:
            return True

        return False

    def hash(self, key):
        """
        Hashes the key so that it will contain a index for where to be stored

        :pre condition: key must be a string
        :worst time complexity: O(N) where N is the length of the string key
        :best time complexity: O(N) where N is the length of the string key
        :param key: a string containing the value to be hashed
        :return: the hashed value of key
        """
        hash = 0
        for i in range(len(key)):
            hash = (hash*self.base + ord(key[i])) % self.length
        return hash

    def rehash(self):
        """
        This function will be called when the list is full. It will resize the hashtable by a prime number
        at least twice the original size and hash every value from the old hashtable into the new one.

        :pre condition: the object contains a hash table to rehash
        :post condition: the object will contain a new hashtable of a size at least twice the original
        with correctly rehashed values.
        :worst time complexity:O(N*M) where N is the length of the current hashtable and M is the length
        of the keys
        :best time complexity: O(N*M) where N is the length of the current hashtable and M is the length
        of the keys
        """
        self.rehash_count += 1
        Primes = [3, 7, 11, 17, 23, 29, 37, 47, 59, 71, 89, 107, 131, 163, 197, 239, 293, 353, 431, 521, 631, 761,
                  919, 1103, 1327, 1597, 1931, 2333, 2801, 3371, 4049, 4861, 5839, 7013, 8419, 10103, 12143, 14591,
                  17519, 21023, 25229, 30313, 36353, 43627, 52361, 62851, 75521, 90523, 108631, 130363, 156437,
                  187751, 225307, 270371, 324449, 389357, 467237, 560689, 672827, 807403, 968897, 1162687, 1395263,
                  1674319, 2009191, 2411033, 2893249, 3471899, 4166287, 4999559, 5999471, 7199369]

        newlength = 0
        for i in range(len(Primes)):
            if Primes[i] > self.length * 2:
                newlength = Primes[i]
                break

        tempArray = [None] * self.length
        for i in range(self.length):
            tempArray[i] = self.table[i]

        self.table = [None] * newlength
        self.length = newlength
        self.count = 0

        for item in range(len(tempArray)):
            if tempArray[item] is not None:
                key, value = tempArray[item]
                self.__setitem__(key, value)

    def statistics(self):
        """
        Returns the values containing statistics of the hashtable

        :worst time complexity: O(1)
        :best time complexity: O(1)
        :return self.collisions: the number of times there was a collision when trying to insert a piece of data
        :return self.probe_total: the total length of all probes within the hashtables lifespan
        :return self.probe_max: the highest probe length that occured when inserting data into the hashtable
        :return self.rehash_count: the number of times the object had to resize and rehash all values in the table
        """
        return self.collisions, self.probe_total, self.probe_max, self.rehash_count


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


def load_dictionary_statistics(hash_base, table_size, filename, max_time):
    """
    Times how long it takes for the load dictionary function to run and if it throws a TimeoutError
    it'll set the time as None. It then returns the amount of words in the hashtable and the time taken.

    :pre condition: hash_base must be an integer, table_size must be an integer, filename must be a string
    containing the name of the file being used, max_time is an integer containing the maximum amount of time for
    the function load dictionary to run.
    :post condition: will have hashed all lines from the file filename into the hashtable, and timed it.
    :worst time complexity: O(N*M+K) where where N is the number of lines in the file 'filename', M is the length
    of the hashtable and K is the length of the keys used
    :best time complexity: O(N+K) where N is the number of lines in the file 'filename' and K is the length
    of the keys used
    :param hash_base: an integer containing the base of the hash table object
    :param table_size: an integer containing the size to set the hashtable object to
    :param filename: a string containing the name of the file to open
    :param max_time: an integer containing the maximum amount of time for the load_dictionary function to run for
    :return hashtable.count: The amount of words added to the hashtable object
    :return time: The time taken for the load_dictionary function to complete
    :return collisions: The number of times there was a collision when inserting a piece of data.
    :return total_probe: The total length of all probes when inserting into the hash table.
    :return max_probe: The highest length of all probe chains.
    :return rehashcount: The number of times the rehash function was called.
    """
    hashtable = HashTable(table_size, hash_base)

    startTimer = timeit.default_timer()
    try:
        load_dictionary(hashtable, filename, max_time)
        endTimer = timeit.default_timer() - startTimer
        time = endTimer
    except TimeoutError:
        time = None

    collisions, total_probe, max_probe, rehashcount = hashtable.statistics()
    return hashtable.count, time, collisions, total_probe, max_probe, rehashcount

def table_load_dictionary_statistics(max_time):
    """
    Stores all combinations between blist and sizelist and each file and stores all the data as rows in
    the output_task3.csv file

    :pre condition: max_time must be an integer, and there must be files available to read from
    :post condition: output_task3.csv will contain rows for each combination of data and the results produced
    from them.
    :worst time complexity:O(N*M+K) where N is the number of lines in each file, M is the length of
    the hashtable and K is the length of keys used
    :best time complexity: O(N+K) where N is the number of lines in each file and K is the length of
    the keys used
    :param max_time: the maximum amount of time each combination of data can run for before stopping.
    """
    blist = [1, 27183, 250726]
    filelist = ["english_large.txt", "english_small.txt", "french.txt"]
    sizelist = [250727, 402221, 1000081]
    with open('output_task3.csv', 'w', newline='') as f:
        thewriter = csv.writer(f, delimiter=',')
        for file in filelist:
            for b in blist:
                for size in sizelist:
                    print(file, b, size)
                    words, time, collisions, probe_total, probe_max, rehash = load_dictionary_statistics(b, size, file, max_time)
                    print(time)

                    if time is None:
                        thewriter.writerow([file, b, size, words, max_time + 10, collisions, probe_total, probe_max, rehash])
                    else:
                        thewriter.writerow([file, b, size, words, time, collisions, probe_total, probe_max, rehash])

table_load_dictionary_statistics(120)
