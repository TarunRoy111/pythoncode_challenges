"""remove duplicates in list """
"""
lst=[1,5,5,3,4,4,2,2,6]
res_lst=[x for i,x in enumerate(lst) if x not in lst[:i]]
print(res_lst)
"""

""" sort dictonary by values"""
"""
d={'one':1,'four':4,'two':2,'seven':7}
s_d=sorted(d.items(),key=lambda x:x[1])
print(dict(s_d))
"""

"""remove odd characters in a list"""
"""
lst=input.split()
new=[lst[x] for x in range(0,len(lst),2)]
print(new)
"""

"""addition on elements in a list using recursion"""
"""
def add(lst):
    if not lst:
        return 0
    else:
        return lst[0]+add(lst[1:])

lst=[1,2,3,4,5]
print(add(lst))
"""