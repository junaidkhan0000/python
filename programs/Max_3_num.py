a, b, c=map(int,input().split())
if(a>b and a<c) or (a<b and a>c):
    print("A is 2nd Max")
elif (b>c and b<a) or (b<c and b>a):
    print("B is 2nd Max")
elif (c>a and c<b) or (c<a and a>b):
    print("C is 2nd Max")
else:
    print("You entered two same numbers")


