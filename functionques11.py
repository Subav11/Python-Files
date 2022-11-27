def count(listofNum):
    even = 0
    odd = 0
    for i in listofNum:
        if i % 2 == 0:
            even = even + 1
        else:
            odd += 1
    return even, odd    
    
listofNum = [32, 21, 64, 100, 13]
even,odd = count(listofNum) 
print(even)
print(odd)