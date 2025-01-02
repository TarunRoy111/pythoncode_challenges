# program to get n (non-negative integer) copies of the first 2 characters of a given string return n copies of the whole string if the length is less than 2.

s=input("enter:")
n=int(input("enter:"))
if len(s)<2:
    print("Copies:",s*n)
else:
    print("Copies:",s[:2]*n)

# program to test whether a passed letter is a vowel or not. 

v='a','e','i','o','u','A','E','I','O','U'
s=input("enter:")
if any(char in v for char in s):
    print("Yes")
else:
    print("No")