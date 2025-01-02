'''
Write a program to print frequency of a number in python
'''
l=[1,2,3,4,2,5,3,4,5,1,2,3,4]
d={}
for i in l:
    if i in d:
        d[i]+=1 
    else:
        d[i]=1 
for k,v in d.items():
    print(k,":",v)


'''
Program to Print missing random odd number between all odd number between 1 to 50
'''
num=[1,3,2,4,5,6,7,9,34,13,56,50]
for i in range(51):
    if i%2!=0 and i not in num:
        print(i,end=" ")
        