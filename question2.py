# find if the given number is a palindrome or not?
n = input("enter the string ")
if(n == n[::-1]):
    print("palindrome")
else:
    print("Not a palindrome")
