# calculate the sum of three given numbers. If the values are equal, return three times their sum. 

a=int(input("Enter:"))
b=int(input("enter:"))
c=int(input("enter:"))
if a==b==c:
    print((a+b+c)*3)
else:
    print("sum is:",a+b+c)


# program that returns a string that is n (non-negative integer) copies of a given string. 

s=input("enter:")
n=int(input("enter:"))
if n!=0:
    print("Text:",s*n)