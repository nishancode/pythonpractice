#If statement can be use without elif or else
"""
roll=5
if roll>2:
    print("If statement Printed.")
print("If statement not printed.")

is_active=True
if is_active:
    print("Hello Python.")
"""
# AND, OR , NOT
# AND: When both two conditions are true, result is true otherwise false.
# OR: If any on conditions is true, then result is true.
# NOT: It make true to false and vice versa.
#AND (and should be on small letter)
"""
age=45
grade=19
# WAP where age must be less than 30 and grade must be greater than 15 to enter purple haze

if age<30 and grade>15:
    print("You can enter.")
else:
    print("Your requirement doesn't match to enter.")

#OR (should be on small letters)
age=45
grade=19
# WAP > where age must be less than 30 and grade must be greater than 15 to enter purple haze
if age<30 or grade>15:
    print("You can enter.")
else:
    print("Your requirement doesn't match to enter.")

#not
# In boolean true is 'True' and false is 'False'. should be caps first letter
is_active=False
if not is_active:
    print("Hello Python.")
"""

#age should be greater than or equal to 18 and should not have any criminal record
age=int(input("Please enter your age: "))
is_criminal_record=False
if age>=18 and not is_criminal_record:
    print("You are eligible.")
else:
    print("You are not eligible.")