import math
def real_roots(a,b,c):
    a = float(input("Enter a value: "))
    b = float(input("Enter b value: "))
    c = float(input("Enter c value: "))

    d = (b**2) - (4*a*c)

    if d < 0:
        print("no real solution")

    elif d == 0:
        answer1 = (-b + math.sqrt(d)) / (2 * a)
        print("1 root: ", answer1)

    else:
        answer2 = (-b-math.sqrt(d))/(2*a)
        answer3 = (-b+math.sqrt(d))/(2*a)
        print("two roots: ", answer2, " ", answer3)

real_roots()