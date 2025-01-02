# write a program for reversing the string inside the list

l=["hii","hello","ramya","surya"]
s=[]
for i in l:
    j=i[::-1]
    s.append(j)
print(s)

# write a program to interchange the characters in a list

l=['Gfg', 'is', 'best', 'for', 'Geeks']
ls=[]
for i in l:
    res=i.replace('G','-').replace('e','G').replace('-','e')
    ls.append(res)
print(ls)