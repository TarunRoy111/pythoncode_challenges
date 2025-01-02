"""
Remove duplicate words in string(unique string)
"""
s='rajaramohan'
# print("".join(list(set(list(s)))))
ns=''
for x in s:
    if x not in ns:
        ns+=x
print(ns)


"""
check whether two strings are anagrams or not
"""
def anagram(s1,s2):
    if len(s1)!=len(s2):return False
    for x in s1:
        if x in s2: 
            s2=s2.replace('x',"",1)
        else: 
            return False
    return True
s1='listen'
s2='silent'
if anagram(s1,s2):
    print('anagram')
else: 
    print('not anagram')
# if sorted(s1)==sorted(s2): print('anagram')
# else: print('not anagram')




"""
check whether the input is integer or not using try except
"""
n=10
# if isinstance(n,int):
#     print('yes')
# else:print('no')
try:
    int(n)
    print('yes')
except ValueError:
    print('no')



"""
check whether the string is pangrams or not 
"""
alp="abcdefghijklmnopqrstuvwxyz"
s1=set(alp)
inp=input('enter string: ').lower()
s2=set(inp)
if s1.issubset(s2):
    print('panagram')
else:print('not panagram')