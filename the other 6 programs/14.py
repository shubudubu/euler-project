max=0
for i in range(1,1000001):
    x=1
    y=i
    while True:
        if i%2==0:
            i=int(i/2)
        else:
            i=i*3+1
        x+=1
        if i==1:
            break
    if max<x:
        max=x
        lc=y
print(max,lc)
