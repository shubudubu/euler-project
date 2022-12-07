s=0
for i in range(1,10001):
    s1,s2=0,0
    for j in range(1,i):
        if i%j==0:
            s1=s1+j
    for j in range(1,s1):
        if s1%j==0:
            s2=s2+j
    if s2==i and s1!=i:
        s=s+i
print(s)
