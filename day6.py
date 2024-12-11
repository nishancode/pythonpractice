#for num in range(1, 11): #range(start, stop, step - by default=1) stop parameter is mandatory
#    print(num)
"""
for num in range(1, 11, 2): 
    print(num)

print("Nishan "*8)

#WAP to print even numbers from 1 to 20 where condition is kept inside for loop
for i in range(0, 21):
    if i%2==0:
        print(i)
"""
# WAP to print numbers as odd, even, or divisible by 5: 
"""
for num in range(1, 16):
    if num%2==0:
        print(f"Even number is {num}.")
    if num%2!=0:
        print(f"Odd Number is {num}.")
    if num%5==0:
        print(f"Divisible by 5 is {num}.")
"""
#Escape the Character 
print('This is Nishan\'s house', end=",")
print('It\'s a nice house')

a=10
b=15
a,b=b,a
print(f"This is a {a}")
print(f"This is a {b}")