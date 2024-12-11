# Check number with elif
"""
num = int(input('Enter number to check: '))
if num>0:
    print(f'The number {num} is positive.')
elif num<0:
    print(f'The number {num} is negative.')
else:
    print('The number is zero.')
"""
#Check division
marks = int(input('Enter your marks to check division: '))
if marks>=90:
    print("Excellent.")
elif marks>=80:
    print("Great")
elif marks>=60:
    print("First Division")
elif marks>=50:
    print("Second Division")
elif marks>=45:
    print("Pass")
else:
    print("Fail")