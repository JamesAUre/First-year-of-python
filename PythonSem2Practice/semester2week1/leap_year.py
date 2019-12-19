"""
This function  detects whether the given year is a leap year
:precondition:      leap_year is an integer
:complexity best:   O(1)
:complexity worse:  O(1)
:exceptions:
"""

year = int(input('Enter year: '))
leap_year = False

if year %4 != 0:
    leap_year = False
elif year % 100 != 0:
    leap_year = True
elif year % 400 != 0:
    leap_year = False
else:
    leap_year = True

if leap_year:
    string = ""
else:
    string = " not"
# a simpler form would be: string = "" if leap_year  else " not"

print(year, "is" + string, "a leap year")
