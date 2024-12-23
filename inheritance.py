# class to inherit attribute nd methods from another class

class Animal:
    def __init__(self,name):
        self.name = name
        self.alive = True
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")
    
     #inheriting
class Dog(Animal):
    def speak(self):
        print("Bhav")
    pass

class Cat(Animal):
    pass

class Monkey(Animal):
    pass

dog = Dog("Honey")
cat = Cat("Whiskey")
monkey = Monkey("Mon")

print(dog.name)
print(dog.alive)

dog.eat()
dog.sleep()
dog.speak()

cat.eat()