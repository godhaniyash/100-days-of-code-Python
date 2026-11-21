# FTQ – Day 61: Inheritance in Python

# Create a Python program for an employee management system.
# Requirements
# 1. Create a class Employee with:
# - Employee name
# - Employee ID
# - A method showDetails() that displays employee details.
# 2. Create a class Programmer that inherits Employee.
# 3. Add a method showLanguage() inside Programmer that displays the default programming language as Python.

# 4. Create at least two objects:
# - One object of Employee.
# - One object of Programmer.
# 5. Demonstrate that:
# - Both objects can access showDetails().
# - Only the Programmer object can access showLanguage().
# 6. Display all relevant details
class Employee:
    name = "rohan das"
    emp_id = 420
    def showDetails(self):
        print(f"{self.name} has employee id:{self.emp_id}")

class Programmer(Employee):
    def showLanguage(self):
        print("Default language is Python")

a = Employee()
b = Programmer()
a.showDetails()
b.showDetails()
b.showLanguage()