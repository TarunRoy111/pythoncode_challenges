"""mismatched indexes

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
for i in range(len(l1)):
    if l1[i]!=l2[i]:
        print(f"index {i} not matched")"""

"""
Program - Open a file with Email IDs , replace the mail ids with gmail with hotmail
"""
"""
def replacing(filepath):
    with open(filepath,'r') as file:
        content=file.read()
        updated=content.replace('gmail.com','hotmail.com')
    with open(filepath,'w') as file:
        file.write(updated)
filepath='/home/trinadharao-3695/emailSample.txt'
replacing(filepath)
"""