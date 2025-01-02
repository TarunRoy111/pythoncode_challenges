#string convertion from 11:s0:h4:f3:g8:jk to 11s0:h4f3:g8jk
inp=input('enter string : ')
new_s=inp.replace(':',"")
k=len(new_s)//3
print(f"{new_s[:k]}:{new_s[k:2*k]}:{new_s[2*k:]}")


#sum of two non consequtive nums results 20 in a list

lst=list(map(int,input().split(",")))
ls1=[]
ls2=[]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==20:
            ls1.append(lst[i])
            ls2.append(lst[j])
print(list(set(zip(ls1,ls2))))
