s=0
n=int(input("1st  January of year?"))
ch=int(input("1.Monday,2.Tuesday,3.Wednesday,4.Thursday,5.Friday,6.Saturday,7.Sunday"))
if (n%4==0 or n%400) and n%100!=0:
    ch+=366%7
else:
    ch+=365%7
n+=1
for i in range(n,2000+1):
    for j in range(1,12+1):
        if j==4 or j==6 or j==9 or j==11:
            ch+=30%7
        elif j==2:
            if n%4==0:
                ch+=29%7
            else:
                ch+=28%7
        else:
            ch+=31%7
        if ch%7==0:
            s+=1
print(s)
























































































































        
