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
        :worst time complexity: O(N+K) where N is the length of the hashtable and K is the length of key
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
        # keyHash = self.hash(key)
        if self.check_rehash():
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
        :worst time complexity: O(N+K) where N is the size of the hashtable and K is the length of key
        :best time complexity: O(K) where K is the length of key
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

    def check_rehash(self):
        if self.count > (self.length / 2):
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
        of keys
        :best time complexity: O(N*K) where N is the length of the current hashtable and K is the length
        of keys
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

class Freq:
    def __init__(self):
        """
        Creates an instance of the class Freq

        :post conditions: creates an instance of the class Freq with attributes word frequency being a
        object of Hash Table, max val containing the maximum frequency a word appeared. And rarity tally
        attributes such as common, uncommon, rare and errors.
        :worst time complexity: O(1)
        :best time complexity: O(1)
        """
        self.word_frequency = HashTable(1000081, 250726)
        self.maxval = 0
        self.common = 0
        self.uncommon = 0
        self.rare = 0
        self.errors = 0

    def add_file(self, filename):
        """
        Loads a file into the word frequency HashTable then stores its frequency as its value,
        if the frequency of the word is the largest in the hash table, it will be stored on self.maxval

        :precondition: filename must be a string
        :postcondition: self.word_frequency will store words from the file, self.maxval will store the
        most frequent word count
        :worst case time complexity: O(N*K) where N is the number of words in a file and K is the length
        of words
        :best case time complexity: O(N*K) where N is the number of words in a file and K is the length
        of words
        :param filename: a string containing the file to read from
        """
        with open(filename, encoding='utf8') as file:
            for line in file:
                for word in line.split():
                    word = ''.join(c for c in word if c not in ':;"().')
                    try:
                        self.word_frequency[word] += 1

                    except KeyError:
                        self.word_frequency[word] = 1

                    if self.word_frequency[word] > self.maxval:
                        self.maxval = self.word_frequency[word]

    def rarity(self, word):
        """
        Returns how rare a word is in its self.word_frequency HashTable
        -COMMON - 0: when frequency is greater or equal to 1% compared to most frequent
        -UNCOMMON - 1: when frequency is greater 0.1% compared to most frequent
        -RARE - 2: when frequency is less than 0.1% compared to most frequent
        -ERROR - 3: when word does not exist in word_frequency

        :precondition: word must be a string
        :worst time complexity: O(N+K) where N is the number of elements in word frequency and
        K is the length of word
        :best time complexity: O(K) where K is the length of word
        :param word: a string containing a word to find the rarity of
        :return: a rarity score of 0-3
        """
        try:

            rarity = self.word_frequency[word] / self.maxval
            if rarity >= 1 / 100:
                return 0
            elif rarity >= 1 / 1000:
                return 1
            elif rarity < 1 / 1000:
                return 2
        except KeyError:
            return 3

    def evaluate_frequency(self, other_filename):
        """
        Checks the ratio of word rarity in the other file based on the rarity values generated
        from previous files.

        :pre condition: other_filename is a string
        :worst time complexity: O(N*K*M) where N is the number of words in other_filename, K is the length
         of each word and M is the length of the newHashtable
        :best time complexity: O(N*K) where N is the number of words in other_filename and K is the length
        of each word
        :param other_filename: a string containing the name of the file to read from
        :return: self.common, the percentage of words in the file that are common
        self.uncommon, the percentage of words in the file that are uncommon,
        self.rare, the percentage of words in the file that are rare,
        self.error, the percentage of words in the file that do not exist
        """
        #self.add_file(other_filename)
        newHashtable = HashTable(1000081, 250726)
        with open(other_filename, encoding='utf8') as file:
            for line in file:
                for word in line.split():
                    word = ''.join(c for c in word if c not in ':;"().')
                    if word not in newHashtable:
                        if self.rarity(word) == 0:
                            self.common += 1
                            newHashtable[word] = 0
                        if self.rarity(word) == 1:
                            self.uncommon += 1
                            newHashtable[word] = 1

                        if self.rarity(word) == 2:
                            self.rare += 1
                            newHashtable[word] = 2

                        elif self.rarity(word) == 3:
                            self.errors += 1
                            newHashtable[word] = 3

        total = self.common + self.uncommon + self.rare + self.errors
        self.common = (self.common / total) * 100
        self.uncommon = (self.uncommon / total) * 100
        self.rare = (self.rare / total) * 100
        self.errors = (self.errors / total) * 100

        return self.common, self.uncommon, self.rare, self.errors


firstWords = Freq()
firstWords.add_file("1342-0.txt")
firstWords.add_file("2600-0.txt")
firstWords.add_file("98-0.txt")
print(firstWords.evaluate_frequency("84-0.txt"))
