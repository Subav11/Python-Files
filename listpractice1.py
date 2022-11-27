colors = ["Red", "Blue", "Red", "Black", 22] #list
cars = ["Tata", "Nano", "Alto"] #list
players =("Dhoni", "Messi", "Dravid") #tuple
for x in cars:
    print(x)
#colors[2] = "Green"   #lists are mutuable and tuples are not
#print(colors[1:4])
#colors[0:2] = "Orange", "White"
#colors.insert(2,"Indigo") #adding any element after the specified index
#colors.append("BMW") #adding any element to the last index
#colors.extend(cars)
#colors.extend(players) #also tuples can be extended with list
#colors.remove("Red")
#colors.pop(1) #pop removes element from a specified index
#del colors[0]
colors.clear() #clear the whole list
print(colors)