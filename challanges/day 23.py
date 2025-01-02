# Program for prime number using functions
def fun(n):
    flag = 0
    for i in range(2, n):
        if n % i == 0:
            flag = 1
    if n == 0 or n == 1 or flag == 1:
        print("Not a prime")
    else:
        print("Prime")

n = int(input("enter: "))
fun(n)

# Find the common prefix from a list of strings and print, if no common prefix found print “No prefix”
# Ex: ["test", "testing", "tease"] here prefix is "te"

l = ['test', 'ttsting', 'tease']
for i in l:
    p = i[:2]
    if p == "te":
        print(p)
    else:
        print("no")