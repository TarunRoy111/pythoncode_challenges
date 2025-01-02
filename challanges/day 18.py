
'''
14)open a file and check how many words of “Windows” and “windows” is there
output:2
'''
"""
def no_Words(filepath):
    with open(filepath,'r') as file:
        content=file.read()
        c=content.count("Windows") + content.count("windows")
        return c
if __name__=='__main__':
    filepath='/home/trinadharao-3695/general_text_file.txt'
    print(no_Words(filepath))
"""




'''
15) Find the largest substring in a string. String = "abcdabmnmnqrsabcdefg"
output:abcdabmnmnqrsabcdefg
'''
"""
s='abcdabmnmnqrsabcdefg'
largest=''
for i in range(len(s)):
    new_str=s[i:]
    if len(largest)<len(new_str):
        largest=new_str
print(largest)
"""