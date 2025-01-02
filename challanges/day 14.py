#checking 3 consecutive numbers
'''
l=list(map(int,input().split()))
res=[]
for i in range(0,len(l)):
    if i>0:
        if l[i-1]==l[i] and l[i]==l[i+1]:
            res.append(l[i])
print(','.join(map(str,res)))
'''
#nested to flatten dictonary
'''
import pandas as pd
nested_dict = {'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]}
df=pd.json_normalize(nested_dict)
print(df.to_dict(orient='records'))
''' 