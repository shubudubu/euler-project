s=0
for i in range(1,2000001):
    x=0
    for j in range(i,0,-1):
        if i%j==0:
            x+=1
    if x==2:
        s+=i
print(s)
