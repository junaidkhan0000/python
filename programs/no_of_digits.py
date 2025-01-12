n=int(input("Enter a number:"))
c=0
while n:
    n//=10
    c+=1
    print("number of digits",c)
