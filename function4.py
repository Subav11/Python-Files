def name(firstName, lastName):
    print("My name is", firstName, lastName)
name("Subham", "Yadav")    
name("Anurag", "Dhull") 


def name(*args):
    print(args[0])
name("Subham", "Yadav", 19, "Agra")
#it will print in tupple form as a collection


