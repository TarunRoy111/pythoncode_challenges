"""counting no.of letters in a file"""
with open('general_text_file.txt','r') as file:
    content=file.read()
    print(f"the no of words in this file is {len(content.split())}")


"""Remove special symbols / punctuation from a string"""

inp=input("enter a string: ")
for x in inp:
    if x.isalnum():
        print(x,end="")