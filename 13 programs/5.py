a=1
while True:
    x=0
    for i in range(1,21):
        if a%i==0:
            x+=1
    if x==20:
        break
    a+=1
print(a)
