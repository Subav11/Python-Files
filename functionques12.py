#create a function that will display how many items in the list have names more than 5 characters
#names = ["Atul", "Subham", "Anurag", "Rahul", "Dev", "Roy"]

def name(names):
    character = 0
    for i in names:
        if len(i)>5:
         character += 1    
names = ["Atul", "Subham", "Anurag", "Rahul", "Dev", "Roy"] 
character = name(names)
print(character)        
