# printing calendar of specific month

import calendar
y=int(input("enter year:"))
m=int(input("Enter month:"))
print(calendar.month(y,m))

# remove characters from a string from 0 to n and return a new string.

str1 = "PYnative"
n=int(input("Enter:"))
y=str1[:n]
x=str1[n:]
print(x)
print(y)