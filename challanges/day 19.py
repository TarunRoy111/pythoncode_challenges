'''
16)Program for Finding the IP address in an file using regular expression 
'''
"""
import re

def find_ip(inp, pattern):
    lst = re.findall(pattern, inp)
    print(lst[0])
if __name__ == '__main__':
    inp = input()
    pattern = r'\b(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\b'
    find_ip(inp, pattern)
"""





'''
17)Program to Print missing random odd number between all odd number between 1 to 50
output1:45
output2:27
'''
"""
import random
def find_missing_num(start,end):
    random_number=random.randint(start,end)
    if random_number%2!=0:
        print(random_number)
    else:
        find_missing_num(start,end)
find_missing_num(1,50)
"""

