'''
Program to Print factorial using recursion
input:5
output:factorial of 5 is 120
'''
"""
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
if __name__=='__main__':
    n=int(input('enter a number to find it\'s factorial: '))
    print(f"factorial of {n} is {fact(n)}")
"""


'''
 Counting number of char 'A' in a file
input:A
output:count of A is 1
'''
"""
def char_count(file_path,char):
    with open(file_path,'r') as file:
        content=file.read()
        c=content.count(char)
        return c
char=input('enter character to find: ')
file_path='/home/trinadharao-3695/general_text_file.txt'
print(f"count of {char} is {char_count(file_path,char)}")
"""