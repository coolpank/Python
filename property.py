# We define getter with '@property'
# we define getter and setter here
class User:
    def __init__(self, first, last, age):
        self._first = first
        self._last = last
        if age > 0:
            self._age = age
        else:
            self._age = 0

    def full_name(self):
        print(f"{self._first} {self._last} is {self._age}")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 0:
            self._age = age
        else:
            self._age = 0

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, first):
        self._first = first


u1 = User("pankaj", "Kumar", 30)
u1.full_name()
u1.first = "Dheeraj"
u1.age = 20
u1.full_name()
print(u1.first)