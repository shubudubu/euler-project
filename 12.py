n=1
while True:
    k=0
    for i in range(1,n+1):
        k+=i
    x=0
    for j in range(1,k+1):
        if k%j==0:
            x+=1
    if x>500:
        print(str(k)+","+str(n))
        break
    n+=1
