def flipstring (word):
    #reversedstring = word[::-1]
    for i in range(0,len(word)//2):
        word[i] = word[len-1]

    return word

def palindrome(word):
    if flipstring(word) == word:
        return 1
    else:
        return 0

def vowelcheck(word):
    vowels = ['a','e','i','o','u']

    vowelcount = 0

    for i in range (0,len(vowels)):
        vowelcount += word.count(vowels[i])

    if (vowelcount) > len(word)//2:
        return 1
    else:
        return 0

def longestword():
    return

userlist = [['ooooo','tttt','tacocat','word'],[],[]]
userlist.lower()

userinput = input("enter word: ")
for i in userlist[]:
    if palindrome(userinput) == 1 and vowelcheck(userinput) == 1:
        print ("yes")
    else: print ("no")