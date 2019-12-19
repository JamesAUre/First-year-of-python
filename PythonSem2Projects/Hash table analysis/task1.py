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

    def __getitem__(self, key):
        """
        Gets an item from the hashtable with the specified key (LINEAR PROBING)

        :pre conditions: key must be a string
        :post conditions: returns the value in the hash table that contains the key
        :worst time complexity: O(N+M) where N is the length of the hashtable and M is
        the length of the key
        :best time complexity: O(M) where M is the length of the key
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
        :worst time complexity: O(N+M) where N is the length of the hashtable and M is the length
        of the key
        :best time complexity: O(M) where M is the length of the key
        :param key: a string containing information for where to store the item on the hashtable
        :param item: contains the value that the user wants to store on the hashtable
        """
        # keyHash = self.hash(key)
        if self.checkfull():
            self.rehash()
        index = self.hash(key)
        if self.__contains__(key):
            while self.table[index % self.length][0] != key:
                index += 1
        else:
            while self.table[index % self.length] is not None:
                index += 1

            self.count += 1
        self.table[index % self.length] = [key, item]

    def __contains__(self, key):
        """
        Checks to see if a key exists in the hashtable (LINEAR PROBING)

        :pre condition: key must be a string
        :post condition: will have checked whether the key exists in the hashtable
        :worst time complexity: O(N+M) where N is the size of the hashtable and M is the length of
        the key
        :best time complexity: O(M) where M is the length of the key
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
        :worst time complexity:O(N*K) where N is the length of the current hashtable and K is the length
        of the keys
        :best time complexity: O(N*K) where N is the length of the current hashtable and K is the length
        of the keys
        """
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
