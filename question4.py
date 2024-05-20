#write a program to find the sum of digits of a given number'
num = int(input("enter the number"))
copy = num
sum = 0
while(copy!=0):
    sum +=int(copy%10)
    copy/=10
print(f"the sum of digit of {num} is: ",sum)
