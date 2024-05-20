#write a program to find the factorial of a nummber
num = int(input("Enter the number: "))
fact = 1  
for i in range(1, num + 1):
    fact *= i 
print(f"The Factorial of {num} is ",fact)
