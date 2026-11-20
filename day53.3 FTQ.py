from functools import reduce 
# Challenge: Number Processor
# Create a Python program using this list:
numbers = [2, 5, 8, 10, 3, 6]
print(f"list:{numbers}")

# ALL FUNCTIONS HERE
def sq(x):
    return x*x
def grtr(value):
    return value > 20
# def sum(x,y):
#     return x+y
# Requirements:
# 1. Use map() to calculate the square of every number.
squared = list(map(sq,numbers))
print(f"Squared:{squared}")

# 2. Use filter() to select numbers greater than 20 from the squared results.
filtered = list(filter(grtr,squared))
print(f"Filtered:{filtered}")

# 3. Use reduce() to calculate the sum of all squared numbers.
reduced = reduce(lambda x,y:x+y,squared)
print(f"Reduced:{reduced}")
# 4. Import reduce from functools.
# 5. Print all three results.k