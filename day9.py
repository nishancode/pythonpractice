"""
def rect(l, b):
    return l*b
l=int(input("Enter Length of Rectange : "))
b=int(input("Enter Breadth of Rectange : "))
area=rect(l, b)
print(area)
"""
def add(*args):
    return sum(args)
print(add(4,5,6,7,8))
print(add(4,5))