x,y,z=0,1,0
while True:
    x=0
    for i in range(1,y+1):
        if y%i==0:
            x+=1
    if x==2:
        z+=1
    if z==10001:
        print(y)
        break
    y+=1
    
        
