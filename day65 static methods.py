class Calculator:# Create a class named Calculator that:
    def __init__(self,num):# 1. Has a constructor accepting a number and stores it in an instance variable.
        self.num = num
    def add_to_num(self,n):# 2. Has an instance method add_to_num(n) that adds n to the stored number.
        self.num = self.num + n
    @staticmethod# 3. Has a static method calculate(a, b, operation) that performs addition or multiplication depending on the operation.
    def calculate(a,b,operation):
        if operation == "add":
            return a + b
        elif operation=='multiply':
            return a*b
        else:
            print("something went wrong")
# 4. The static method must not access or modify the instance variable.
# 5. Create two different objects with different initial numbers.
Calculator.calculate(3,4,"multiply")# Twist: Your static method must work even when no object has been created
ob1 = Calculator(22)
ob2 = Calculator(65)
ob1.add_to_num(5)
print("modified:",ob1.num) # 6. Modify only the first object's number using its instance method.
# 7. Call the static method using:
print(Calculator.calculate(5,3,"add"))#    - The class name.
print(ob1.calculate(5,3,"add"))#    - The first object.
print(ob2.calculate(5,3,"add"))#    - The second object.
# 8. Display the results and demonstrate that modifying one object's number doesn't modify the other.
