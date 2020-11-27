#Class methods are methods (with the @classmethod decorater)
#    'cls' is a class instance same as 'self' is an instance of an object
#   with class method we can create a new instance of a class
class Users:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

    @classmethod
    def from_string(cls,data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        Users.active_users += 1

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

class Moderator(Users):
    active_mod = 0
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.active_mod += 1

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_mod} active moderators"
    def remove_post(self):
        return f"{self.fullname()} removed a post from {self.community}"

u1 = Users("Dheer", "Bharv", 25)
jasmine = Moderator("Jasmine", "O'conner", 30, "Piano")
pankaj = Moderator("Pankaj", "Kumar", 34, "Philosophy")
print(jasmine.fullname())
print(Users.display_active_users())
print(Moderator.display_active_users())

