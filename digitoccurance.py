n=(int)(input("Enter a  number"))
a=[]
for i in range(0,10):
    a.append(0)
while n>0:
    x = n%10
    a[x]+=1
    n=n//10
for i in range(0,10):
    print("%d occured %d times" %(i,a[i]))
