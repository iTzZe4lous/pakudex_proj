# import Pakuri class to use its methods
from pakuri import Pakuri

class Pakudex:

    # initializes object with default capacity and list of pakuris and size of 0
    def __init__(self, capacity=20):
        self.capacity = capacity
        self.pakuris = []
        self.size = 0

    # getter to return size
    def get_size(self):
        return self.size

    # getter to return capacity
    def get_capacity(self):
        return self.capacity

    # creates and returns list of species from pakuri list objects, returns none if empty
    def get_species_array(self):
        species = []
        for pakuri in self.pakuris:
            species.append(pakuri.species)
        if len(species) > 0:
            return species
        else:
            return None

    # returns stats as list if pakuri list has obj
    def get_stats(self, species):
        stats = []
        for pakuri in self.pakuris:
            if pakuri.species == species:
                stats.extend([pakuri.attack, pakuri.defense, pakuri.speed])
                return stats
        return None

    # sorts list alphabetically by species
    def sort_pakuri(self):
        self.pakuris.sort()

    # adds pakuri to pakuris list if is not duplicate and iterates list size
    def add_pakuri(self, species):
        for pakuri in self.pakuris:
            if pakuri.species == species:
                return False
        self.pakuris.append(Pakuri(species))
        self.size += 1
        return True

    # evolves pakuri if it exists by calling evolve method in Pakuri class
    def evolve_species(self, species):
        for pakuri in self.pakuris:
            if pakuri.species == species:
                Pakuri.evolve(pakuri)
                return True
        return False
