import math
import random

def converter():
    f = float(input("Enter degrees Fahrenheit: "))
    c = (f-32)*5/9
    print(c)

def root():
    x = float(input("Enter the number x: "))
    y = int(input("Enter the number y:"))
    a = math.e**(math.log(x)/y)
    print(a)

def coinflip():
    prob = float(input("Enter probability of heads: "))
    if random.random() < prob:
        print("heads")
    else: print("tails")

def namelength():
    name = input("Enter your name: ")
    vowelcount = 0
    count = 0
    for x in name:
        count = count + 1
        if (x =='a' or x =='e' or x =='i' or x =='o' or x =='u'):
            vowelcount = vowelcount + 1

    print("length of name: ", count)
    print("number of vowels: ", vowelcount)


def threesidecoin():
    threecoinprob = int(random.randint(0,2))
    print(threecoinprob)
    if threecoinprob==1:
        print("1")
    elif threecoinprob==2:
        print("2")
    else:
        print("3")


def velocity():
    g = 6.67408 * (10**-11)
    m = 5.972 * (10**24)
    r = 6.371 * (10**6)
    m0 = 0.1

    v = float(math.sqrt((2/m0)*(-(-g*m*m0)/r)))
    print(v)

inp = int(input("enter number: "))

if inp == 1:
    converter()

if inp == 2:
    root()

if inp == 3:
    coinflip()

if inp == 4:
    namelength()

if inp == 5:
    threesidecoin()

if inp == 6:
    velocity()