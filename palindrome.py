x=(int)(input("Enter a number"))
n=x
rev=0
while x>0:
    rev=rev*10+x%10
    x//=10
if(rev==n):
    print("palindrome")
else:
    print("not palindrome")