def palindrome(word):
    word = word.lower()
    reversedstring = word[::-1]
    if reversedstring == word:
        return True
    else:
        return False

def GetWordsInFile( filename ):
    File = open(filename,"r")

    Words = []
    for line in File:
        WordsInLine = line.split(" ")
        for Word in WordsInLine:
            Word = Word.replace("\n", "")
            Words.append( Word )

    File.close()
    return Words


WordsFromFile = GetWordsInFile("palindromic.txt")

for Word in WordsFromFile:
    print(palindrome(Word))
