class Person:
    def __init__(self, name, rollNo):
        self.name = name  #self.name m name instance h
        self.rollNo = rollNo

    def printOutput(self):
        print("The name is:", self.name, "and roll no. is:", self.rollNo)
person1 = Person("Ramendra", "50") 
person2 = Person("Subham", "69")   
person1.printOutput()
person2.printOutput()  
print(id(person1))
print(id(person2))      