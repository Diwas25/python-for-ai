class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
            return f"{self.name} is sleeping"

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

dog_1 = Dog("Tom")
dog_2 = Dog("Jerry")

print(dog_1.eat())
print(dog_1.sleep())
print(dog_1.bark())

print(dog_2.eat())
print(dog_2.sleep())
print(dog_2.bark())