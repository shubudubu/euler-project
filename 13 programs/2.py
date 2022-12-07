a=1
b=2
q=0
if a%2==0:
    q+=a
if b%2==0:
    q+=b
while True:
    c=a+b
    if c>4000000:
        break
    a=b
    b=c
    if c%2==0:
        q+=c
print("sum of even valued terms among the first 4 million fibonacci numbers=",q)


    
    
