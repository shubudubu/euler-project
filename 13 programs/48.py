s=0
x=0
st=""
for i in range(1,1001):
    s+=i**i
st=str(s)
l=len(st)
std=st[l-1:l-10-1:-1]
stdr=std[::-1]
print(stdr)
