# repr method is an instance method. repr means representations
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

    def __repr__(self):
        return f"{self.first} is {self.age} year old"

    def fullname(self):
        return f"{self.first} {self.last}"



Pankaj = Users("pankaj", "kumar",30)
print(Pankaj)