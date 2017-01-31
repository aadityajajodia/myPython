a=["aditya","siddhart"]
count=[]
for i in range (0,123):
    count.append(0)
for i in range(0,2):
    for j in a[i]:
        count[ord(j)]+=1
for i in range(97,123):
    if(count[i]!=0):
        print("%s %d"%(chr(i),count[i]))