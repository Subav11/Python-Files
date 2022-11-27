def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
def power(num1,num2):
    return num1**num2   

num1 = int(input("Enter the first number:"))     
num2 = int(input("Enter the second number:"))

print("Select the operator")
print("for Addition: +")
print("for subtraction: -")
print("for multiplication: *")
print("for division: /")
print("for power: **")

choose = input("Select the operator:")
if choose == "+":
    print(add(num1,num2))
elif choose == "-":
    print(subtact(num1,num2))    
elif choose == "*":
    print(multiply(num1,num2))  
elif choose == "/":
    print(division(num1,num2))      
elif choose == "**":
    print(power(num1,num2)) 
else:
    print("nothing")       

               

