max=0
for i in range(999,100,-1):
    for j in range(i,0,-1):
        k=i*j
        p=str(k)
        q=p[::-1]
        if p==q and max<k:
            max=k
print("largest possible palindrome product of 2 three digit numbers=",max)
    
