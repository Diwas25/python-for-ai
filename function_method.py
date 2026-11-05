"""

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("Bark!!!")

jerry = Dog(name='Jerry')

jerry.name
jerry.bark()
"""

"""
def multiply(x,y):
    return "Multi ",x*y


x = multiply(3,12)

print(x)
"""

"""
def print_even(num):
    count = 0
    for i in range(1,num+1):
        if(i%2==0):
            count += 1
            print("Even : ",i)
    return count        

x = print_even(20)

print(x)
"""
def add(*numbers):
    total = 0
    for i in numbers:
        total += i
    
    return total

print(add(2,6,43,23,11))