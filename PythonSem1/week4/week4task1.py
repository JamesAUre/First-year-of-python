import sys
import codecs

file = open("haiku.txt","w+")
file.write("Five,;seven;then;five,	Syllables;mark;a;Haiku,	Reading;files;is;fun")
mystring = ""
for line in file:
    mystring += line

file.close()
print (mystring)