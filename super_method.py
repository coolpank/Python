class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species = "cat")
        self.breed = breed
        self.toy = toy


blue = Cat("Blue", "Ginger", "String")
print(blue)


