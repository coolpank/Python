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



# u1 = Users("Pankaj", "Bharvey", 30)
# print(Users.display_active_users())
# u2 = Users("dheeraj", "Bharvey", 29)
# u3 = Users("papa","Ko", 50)
# print(Users.display_active_users())

#We created a new instance of a class by class method from_string

tom = Users.from_string("Pankaj,Bharvey,30")
print(tom.first)
print(tom.fullname())

a = "Pankaj,Kumar,Bharvey".split(',')
print(a)