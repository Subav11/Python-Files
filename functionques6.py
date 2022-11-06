#create a function that will take two arguments, name and age and print their values
def name(name , age):
 print(name, age)    
name("Subham", 19)


#create a function in such a way that we can pass any number of arguments to this and it should display each argument's value
def names(*args):
    for i in args:
        print(i)
names("Subham", "Anurag", "Atul", "Lakshay")
