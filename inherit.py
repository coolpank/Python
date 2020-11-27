class Animal:
    cool = True
    def make_sound(self, sound):
        print(f"This animal says {sound}")

class Cat(Animal):
    pass

a = Cat()
a.make_sound("Meow")

# print(isinstance(a, Animal)) 