arr=[1,2,3,1,3,1,3,2,4,5]
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)