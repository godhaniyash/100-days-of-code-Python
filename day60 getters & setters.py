# Create a constructor that accepts a student's marks.
# Store the marks in an attribute named _marks.
# Create a getter using @property that returns twice the actual marks.
# Create a setter using the appropriate setter decorator.
# The setter must update _marks by dividing the received value by 2.
# Create an object of the class.
# Display the getter's returned value.
# Change the value using the setter.
# Display the updated getter value and the actual _marks
class Student:
    def __init__(self,marks):
        self._marks = marks
    @property
    def twice_marks(self):
        return 2 * self._marks
    @twice_marks.setter
    def twice_marks(self,new_marks):
        self._marks = new_marks / 2
    
s1 = Student(20)
print(s1.twice_marks)
print(s1._marks)
s1.twice_marks = 500
print(s1._marks)