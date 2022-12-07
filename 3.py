n=600851475143
x=0
for i in range(n,0,-1):
    if n%i==0:
        x=0
        for j in range(1,i+1):
            if i%j==0:
                x+=1
        if x==2:
            break
print(i)
