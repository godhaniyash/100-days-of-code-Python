# Create a Python program for an Employee Management System that:
# - Creates an Employee class.
# - Uses a class variable to store the company name.
# - Uses a class variable to count the total number of employees.
# - Uses a constructor to initialize each employee's name and raise amount.
# - Automatically increases the employee count whenever a new employee is created.
# - Creates at least three employee objects with different names.
# - Displays each employee's name, raise amount and company name.
# - Changes the raise amount of only one employee.
# - Changes the company name using the class name.
# - Creates an instance variable with the same name as the class variable for one employee.
# - Displays the company name for all employees to demonstrate the difference between instance and class variables.
# - Displays the total number of employees.
class Employee:
    comp_name = "Apple"
    noofemp = 0
    def __init__(self,name,raiseamount):
        self.name = name 
        self.raise_amount = raiseamount
        self.noofemp = self.noofemp + 1

em1 = Employee("Nitesh",3)
em2 = Employee("yash",300000)
em3 = Employee("mohan",420)
print(em1.name())
print(em1.comp_name())
print(em1.raise_amount())
print(em2.name())
print(em2.comp_name())
print(em2.raise_amount())
print(em3.name())
print(em3.comp_name())
print(em3.raise_amount())
# theme of vs code:github dark default
