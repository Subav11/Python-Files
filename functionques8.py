 #create a function using following conditions
 #it should accept employee name and salary and display both
 #if the salary is missing in the function the assign the default value 10000 to salary
 #ben (9000) mike(15000) bob()

def salary(Employeename, Salary = 10000):
     print(Employeename, "Salary is", Salary)
salary("Ben", 9000)
salary("Mike", 15000) 
salary("Bob")   