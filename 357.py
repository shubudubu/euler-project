s,so=0,0
for i in range(1,1000000001):
    p=0
    s=0
    for j in range(1,i+1):
        if i%j==0:
            p+=1
            a=int(j+i/j)
            x=0
            for k in range(1,a+1):
                if a%k==0:
                    x+=1
            if x==2:
                s+=1
    if p==s:
        so+=i
print(so)

