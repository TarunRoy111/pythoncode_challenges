# counting keys in a dict

d1={1:'one',2:'two'}
d2={3:'three',4:'four',5:'five'}
d3={6:'six'}
d={'d1':d1,'d2':d2,'d3':d3}
print(d)
count=0
for v in d.values():
    for k in d.keys():
        count+=1
print(count)

# renaming keys in dictionary

d1={"name":"Ramya","Age":21,"Loc":"Vsp"}
d1["Location"]=d1.pop("Loc")
print(d1)