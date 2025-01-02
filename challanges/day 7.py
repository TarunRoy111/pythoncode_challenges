""""mapping list into dictionary"""

keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']
print(dict(zip(keys,values)))

"""counting three consecutive common numbers in a list"""
l=[4, 5, 5, 5, 3, 8]
for x in l:
    if l.count(x)==3:
        print(x)
        break

