#take two input values then print them swapped
from tempfile import tempdir


x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
temp = x
x = y 
y = temp 
print("first value is :",x)
print("second value is :",y)