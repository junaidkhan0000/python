a, b=map(int,input("Enter two numbers separated by a space: ").split())
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print(f"gcd={a}")
