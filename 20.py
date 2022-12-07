s=0
f=1
for i in range(1,101):
    f=f*i
n=f
st=str(n)
l=len(st)
for i in range(0,l):
    a=st[i]
    b=int(a)
    s+=b
print(s)
