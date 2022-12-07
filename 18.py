#     3
#    74
#   246
#  8593
# 
# 3+7+4+9=23
a=[]
p=0
x=[3,7,4,2,4,6,8,5,9,3]

l=len(x)
for i in range(1,l):
    l-=i
    if l==0:
        m=i
        break
for i in range(0,m):
    b=[]
    for j in range(0,i+1):
        b.append(x[p])
        p+=1
        
    a.append(b)
y=0
s=a[0][0]
for i in range(1,m):
    if a[i][y]<a[i][y+1]:
        s+=a[i][y+1]
        y+=1
    else:
        s+=a[i][y]
print(s)



