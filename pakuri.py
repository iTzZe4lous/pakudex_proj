
class Pakuri:

    #initializes pakuri with attributes based on species name
    def __init__(self, species):
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    # getter returns species
    def get_species(self):
        return self.species

    # getter returns attack
    def get_attack(self):
        return self.attack

    # getter returns defense
    def get_defense(self):
        return self.defense

    # getter returns speed
    def get_speed(self):
        return self.speed

    # setter sets attack
    def set_attack(self, new_attack):
        self.attack = new_attack

    # increases each stat by certain multiple and sets it to that object pakuri
    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3

    # changes operation of sort to go by species
    def __lt__(self, other):
        return self.species <= other.species

