# 'active_users' is a class attribute not an instance attribute
#   class attributes can be used to keep track of individual instances
#  and to create validations next example
class Users:
    active_users = 0
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self. age = age
        Users.active_users += 1

    def logout(self):
        Users.active_users -= 1
        return f"{self.first} has logged out"


print(Users.active_users)

user1 = Users("pankaj", "bharvey", 30)
user2 = Users("Dheeraj", "bharvey", 25)

print(Users.active_users)

print(user2.logout())

print(Users.active_users)
