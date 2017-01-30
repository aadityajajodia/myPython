x=0
for i in range(1, 11):
    for j in range(1, 11):
        x=0
        for k in range(0,j):
            x=x+i;
        print('%dx%d=%d\t' % (j, i, x), end="")
    print("")
