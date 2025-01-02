"""
 return the no of occurances of each element in list
"""

from collections import Counter

lst=[1,2,2,1,4,1,5,8,5]
for x,y in dict(Counter(lst)).items():
    print(f"{x}:{y}")

"""
write all ones first and remaining elements next [0,1,3,0,1,2,0,1,2,3,4,1,6,3]
"""

lst=[0,1,3,0,1,2,0,1,2,3,4,1,6,3]
n_lst=[]
for x in lst:
    if x == 1:
        n_lst.append(x)
        lst.remove(x)
print(n_lst+lst)


"""
counting no.of lower and upper case letters in a string
"""
inp=input('emter string: ')
lc,uc=0,0
for x in inp:
    if x.islower():
        lc+=1
    else:
        uc+=1
print(f"lower count is {lc}\nupper count is {uc}")


"""
Count occurrences of an specific element in a list
"""
lst=[1,2,2,1,4,1,5,8,5]
target=1
count=0
for x in lst:
    if target==x:
        count+=1
print(f"{target} occured {count} times")


"""
check email is vaild or invaild
"""
import re
ptr=r'^[a-zA-Z]+[0-9]+@gmail.com$'
inp=input('enter email id: ')
matched=re.match(ptr,inp)
if matched:
    print('valid')
else:
    print('invalid')


"""
validate an Ip address
"""
import re
p=r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
inp="my ip address is 1.2.3.4"
match=re.search(p,inp)
if match:
    print('valid')
else:
    print('invalid')