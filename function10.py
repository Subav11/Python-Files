a = 5   #globally
def example():
    global a
    a = 10 #locally as it is defined in function
    print(a)

print(a)
example()