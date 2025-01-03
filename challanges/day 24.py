# write a program to generate random number and appending to the list
import random
n=int(input("Enter the elements:"))
l=[]
for i in range(n):
    l.append(random.randint(0,n))
print(l)

# write a program to find the largest string between two strings
s1="Hello"
s2="Hii"
largest=""
if len(s1)<len(s2):
    largest=s2 
else:
    largest=s1 
print(largest)
