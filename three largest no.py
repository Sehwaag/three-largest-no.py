l=[1,23,12,9,30,2,50]
for i in range(len(l)):
    for j in range(len(l)):
        if(l[i]>l[j]):
            temp=l[j]
            l[j]=l[i]
            l[i]=temp
print(l[0:3])
