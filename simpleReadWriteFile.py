f=open("aditya.txt","w")
for i in range(1,21):
    f.write("%d\n"%(i))
f.close()
f=open("aditya.txt","r")
sum=0
for i in range(1,21):
    l1=f.readline()
    sum+=(int)(l1)
print("sum is %d and average is %.2f" %(sum,sum/20))
f.close()