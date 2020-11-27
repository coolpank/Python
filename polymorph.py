class Animal:
    def speak(self):
        raise NotImplementedError("Subclass needs to implements this method")

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Fish(Animal):
    pass



c=Cat()
d= Dog()
f=Fish()
print(c.speak())
print(d.speak())
print(f.speak())