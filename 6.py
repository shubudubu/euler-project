q,s=0,0
for i in range(1,100+1):
    s+=i**2
    q+=i
p=q**2
d=p-s
print("difference between the sum of the squares of the first one hundred natural numbers and the square of the sum=",d)    
