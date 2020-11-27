# Anytime we define a instance method, we pass self parameter
# fullname , initials,likes, is_senior, birthday are instance methods, not class methods. Class methods are diffrent
# instance methods take 'self' as a parameter
class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def fullname(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th {self.first}"



p = Person("Pankaj", "Bharvey", 30)
# print(p.fullname())
# print(p.initials())
# print(p.likes("Cake"))
print(p.is_senior())
print(p.birthday())