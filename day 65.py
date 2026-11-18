# Static Methods in Python

class Math():
    def __init__(self,num):
        self.num = num
    def addtonum(self,n):
        self.num = self.num + n
    @staticmethod
    def add(x,y):
        return x+y

a = Math(5)
print(a.num)
a.addtonum(5)
print(a.num)
print(a.add(6,7))  # I hope you understood what i wanted to present
print(Math.add(6,7))# I hope you understood what i wanted to present
