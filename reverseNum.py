a = int(input("Enter a number"))
rev = 0;
while a > 0:
    rev = rev*10 + a % 10
    a = int(a/10)
print(rev)
