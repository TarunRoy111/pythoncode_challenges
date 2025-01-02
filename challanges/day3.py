"""
Remove special symbols / punctuation from a string
"""

"""
s=input('enter strig: ')
k=""
for i in s:
    if i.isalnum():
        k+=i
print(k)
"""





"""
swap key and values in dictionary
"""
"""
d={1:'one',2:'two',3:'three',4:'four'}
s_d={}
for k,v in d.items():
    s_d[v]=k
print(s_d)
"""




"""
convert the nested list to flatten list by using list comprehension
"""

"""
def flattening(l):
    return [item for sublist in l for item in (flattening(sublist) if isinstance(sublist, list) else [sublist])]

l = [1, [2, 3], 4, [5, 6, 7]]
print(flattening(l))
"""




"""
prints the line numbers where the specific word appears in file
"""
"""
word=input('enter target word: ')
with open("sample.txt",'r') as file:
    statements_list=file.readlines()
    for line in statements_list:
        if word in line:
            print(statements_list.index(line)+1)
"""