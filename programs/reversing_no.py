n=int(input("Enter a number:"))
rev=0
while n:
    rev=rev*10+n%10
    n=n//10
    print(rev)