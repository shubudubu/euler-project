n=2**1000
su=0
st=str(n)
l=len(st)
for i in range(0,l):
    s=st[i]
    d=int(s)
    su+=d
print(su)
