# Challenge: Student Marks Management
# Create a Python program using the following dictionary:
# Your program must satisfy all these requirements:
# Use map() to increase every student's marks by 5.
# Store the updated marks in a new dictionary, preserving student names.
# Use filter() to select students whose updated marks are greater than 50.
# Store the filtered students in another dictionary.
# Import and use reduce() to calculate the total of all updated marks.
# Print the original dictionary, updated dictionary, filtered dictionary and total marks.
# Rules:
# Use only concepts covered up to Day 53.
# Use lambda wherever appropriate.
# Don't modify the original dictionary.
# Don't use list/dictionary comprehensions.


def increment(x):
    return x + 5 


marks = {
    "Yash": 77,
    "Mohan": 22,
    "Rahul": 85,
    "Amit": 35,
    "Raj": 91,
    "Vijay": 48
}

mapped_marks = dict(map(lambda item:(item[0],(item[1]+5)),marks.items())) # to write this line without error i've spent more than half hour 😃🥹🙃🧐🧐🧐
print(mapped_marks)


















