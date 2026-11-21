x = [1, 2, 3]
print(dir(x))
print()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 30)
print(dir(p))
print(p.__dict__)
help(p)
help(str)