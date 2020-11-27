class Pet:
    allowed = ["cat", "dog", "fish", "rat"]
    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet")
        self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")

# print(Pet.allowed)
# Pet.allowed.append("pig")
# print(Pet.allowed)

print(id(Pet.allowed))  #prints memory reference
print(id(cat.allowed))  #prints memory reference
print(id(dog.allowed))  #prints memory reference, All are same