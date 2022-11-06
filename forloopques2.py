#number must be divisible by 5
#if the number is greater than 150, then skip it and move to next number
#if the number is greater than 500, stop the loop
numbers = int[12,75,150,180,145]
for i in numbers:
    if i>150:
        continue
print(i)