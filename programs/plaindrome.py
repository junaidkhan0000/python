def is_palindrome(number):
    num_str=str(number)
    return num_str == num_str[::-1]
n=int(input("Enter a number:"))
if is_palindrome(n):
    print(f"It is a palindrome")
else:
    print(f"It is not a palindrome")