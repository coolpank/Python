class Aquatic:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of sea"

class Amblulatory:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of land"

class Penguin(Amblulatory, Aquatic):
    def __init__(self,name):
        super().__init__(name = name)


jimmy = Penguin("Jimmy")
print(jimmy.swim())
print(jimmy.walk())
print(jimmy.greet())
print(Penguin.__mro__)
print(Penguin.mro())
help(Penguin)