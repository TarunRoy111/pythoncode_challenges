#write a program for replacing the string using sub string

import re
a="I have 2 apples and 3 bananas."
x=re.sub(r"I have","She has",a)
print(x)


#write a program to check if the string starts from the particular word or not 

import re 
a="The milk is in white"
txt=r'\AThe'
x=re.findall(txt,a)
if x:
    print(x,"\nMatch")
else:
    print("No")
