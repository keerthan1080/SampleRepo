x=[5,3,8,6,7,2]
for i in range(len(x)):
    for j in range(len(x)):
        if j<len(x)+1:
            if x[i]<x[j]: #reverse Soring if x[i]>x[j]
                temp=x[j]
                x[j]=x[i]
                x[i]=temp
print(*x)
