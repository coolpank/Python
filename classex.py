# _n        for private convention use
# __n       name mingling, will create problems
# __n__     dunder methods, they are already defined
class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi!"
        self.__msg = "I love you"

p = Person()
print(p.name, p._secret)
# print(p.__msg)    It will generate error
print(dir(p))
print(p._Person__msg)

