for i in range(1,1000):
    for j in range(1,1000):
        for k in range(1,1000):
            if i+j+k==1000 and (i**2+j**2==k**2) and i<j<k:
                p=i*j*k
                a=i
                b=j
                c=k
                break
print(p)
print(a,b,c)
