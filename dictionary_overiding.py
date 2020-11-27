# __missing__ is already defined in dict class, we are just overriding it in GrumpyDict

class GrumpyDict(dict):
    def __repr__(self):
        print("None of your business")
        return super().__repr__()

    def __missing__(self, key):
        print(f"You want {key}? WELL IT AINT HERE")

    def __setitem__(self, key, value):
        print("YOU WANT TO CHANGE THE DICTIONARY")
        print("OK FINE...")
        super().__setitem__(key, value)

    def __contains__(self, item):
        print("NO IT AINT IN HERE")
        return False
data = GrumpyDict({"first": "Tom", "Animal": "Cat"})
# print(data)
data['city'] = "Tokyo"
print(data)
'city' in data