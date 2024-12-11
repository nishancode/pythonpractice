#IF ELSE practice
#Write a program to check whether a number is even or odd.
"""
num=int(input("Enter your number : "))
if num<0:
    print(f"The number {num} is negative.")
elif num==0:
    print(f"The number {num} is zero.")
elif num%2==0:
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")
"""
#Write a program to find the largest of three numbers entered by the user.
"""
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
num3=int(input("Enter your third number: "))
if num1>num2:
    if num1>num3:
        print(f"The number {num1} is the largest number.")
    else:
        print(f"The number {num3} is the largest number.")
elif num2>num1:
    if num2>num3:
        print(f"The number {num2} is the largest number.")
    else:
        print(f"The number {num3} is the largest number.")
else:
    print(f"The number {num3} is the largest number.")
"""
#Create a program that checks if a given year is a leap year.
"""
days=int(input("Enter total days of year : "))
if days==366:
    print("This is a leap year.")
else:
    print("This is not a leap year.")
"""
#For Loop Questions:
#Write a program to print all numbers from 1 to 50.
"""
for i in range(1, 51):
    print(i)
"""
#Print the multiplication table of a given number
"""
num1=int(input("Enter number for multiplication : "))
for b in range(1, 11):
    multiplication=num1*b
    print(f"{num1}*{b}={multiplication}")
"""
#Write a program to calculate the sum of all numbers from 1 to n (where n is entered by the user).
"""
nnum =int(input("Enter number to sum from 1 : "))
nnum=nnum+1
sum=0
for n in range(1, nnum):
    sum=sum+n
print(sum)
"""
#Write a program to find the factorial of a given number.
"""
numfact=int(input("Enter number for factorial : "))
fact=1
for fl in range(numfact, 0, -1):
    fact=fact*fl
print(fact)
"""
