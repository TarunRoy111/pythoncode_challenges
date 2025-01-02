'''
3) program to how can you generate random numbers in Python
output:
Enter How many random number you want: 5
89
58
5
73
48
'''

"""
import random
def generate_randomNums(n):
    for _ in range(n):
        print(random.randint(1,100))
if __name__=='__main__':
    n=int(input("Enter How many random number you want: "))
    generate_randomNums(n)
"""


'''
4) Palindrome program 
input1: madam
output1: madam is palindroime
input2: sir
output2: sir is not a palindrome
input3: madaM
output3: madaM is not a palindrome
'''
"""
def check_palindorme(word):
    if word==word[::-1]:
        print(f"{word} is palindrome")
    else:
        print(f"{word} is not a palindrome")
if __name__=='__main__':
    word=input('Enter word: ')
    check_palindorme(word)
"""

