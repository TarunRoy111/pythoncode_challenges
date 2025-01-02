#------------------------------- Day-1  --------------------------------
"""    
1) Find the First Non-Repeated Character in a String
"""
"""
def check(strr):
    for i in strr:
        if strr.count(i)<2:
            print(f"'{i}' is first non repeating char in given string")
            break
s=input('enter string: ')
check(s)
"""

"""
2) 2.Write a Python program that finds and prints the longest line in file
"""
"""
with open("sample.txt", "r") as file:
    lines=file.readlines()
    max_len=0
    line_no=0
    for line in lines:
        if max_len<len(line):
            max_len=len(line)
            line_no=lines.index(line)+1
    print(f"longest line is {line_no}")
"""

"""
3) 1. Longest substring
"""
"""
def longest_substring(s1,s2):
    allowed_char=set(s2)
    max_sub=""
    curr_sub=""
    for char in s1:
        if char in allowed_char:
            curr_sub+=char
        else:
            if len(curr_sub)>len(max_sub):
                max_sub=curr_sub
            curr_sub=""
    if len(curr_sub)>len(max_sub):
        max_sub=curr_sub
    return max_sub

# Test
string1 = "abcdeabcdabcbbac"
string2 = "abc"
result = longest_substring(string1, string2)
print(f"The longest substring of '{string1}' that can be formed using characters from '{string2}' is: '{result}'")

"""

"""
4) 2.Generate a random password
"""
"""
import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special = '!@#$%^&*'

length = 6
all_characters = lower + upper + numbers + special

password = ''.join(random.choice(all_characters) for _ in range(length))
print(password)
"""


"""
5)sort dict by keys
"""

d={1:'one',5:'five',3:'three',2:'two',4:'four'}
n_d=sorted(d.items(),key=lambda item:item[1])
print(dict(n_d))