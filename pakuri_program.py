# import Pakudex class to use its methods
from pakudex import Pakudex


# main method
if __name__ == '__main__':
    # prints welcome statement and takes in capacity until valid value is entered
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        capacity = input("Enter max capacity of the Pakudex: ")
        if capacity.isdigit() == False:
            print("Please enter a valid size.")
        else:
            break
    # initializes pakudex object
    u_Pakudex = Pakudex(capacity)
    print(f"The Pakudex can hold {u_Pakudex.capacity} species of Pakuri.")

    # main menu while loop that prints menu and does all the functions based on input
    while True:
        print("\nPakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit\n")
        u_option = input("What would you like to do? ")
        # lists pakuri in a numbered list as long as list isn't empty
        if u_option == "1":
            species_list = u_Pakudex.get_species_array()
            if species_list == None:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex:")
                for i in range(1, len(species_list) + 1):
                    print(f"{i}. {species_list[i-1]}")
        # If list isn't empty and species is in list, prints all details for given species
        elif u_option == "2":
            species_name = input("Enter the name of the species to display: ")
            if u_Pakudex.get_species_array() == None:
                print("Error: No such Pakuri!")
            elif species_name in u_Pakudex.get_species_array():
                species_stats = u_Pakudex.get_stats(species_name)
                print(f"\nSpecies: {species_name}")
                print(f"Attack: {species_stats[0]}")
                print(f"Defense: {species_stats[1]}")
                print(f"Speed: {species_stats[2]}")
            else:
                print("Error: No such Pakuri!")
        # If capacity isn't reached, takes input and appends to list if not duplicate, if full prints error
        elif u_option == "3":
            if u_Pakudex.get_size() < int(u_Pakudex.get_capacity()):
                new_species = input("Enter the name of the species to add: ")
                add_pak = u_Pakudex.add_pakuri(new_species)
                if add_pak == True:
                    print(f"Pakuri species {new_species} successfully added!")
                elif add_pak == False:
                    print("Error: Pakudex already contains this species!")
                elif add_pak == "full":
                    print("Error: Pakudex is full!")

            else:
                print("Error: Pakudex is full!")
        # Evolved specified species by calling evolve_species method if species is in list
        elif u_option == "4":
            e_species = input("Enter the name of the species to evolve: ")
            if u_Pakudex.evolve_species(e_species) == True:
                print(f"{e_species} has evolved!")
            else:
                print("Error: No such Pakuri!")
        # sorts by species name alphabetically
        elif u_option == "5":
            u_Pakudex.sort_pakuri()
            print("Pakuri have been sorted!")
        # breaks while loop and ends program
        elif u_option == "6":
            print("Thanks for using Pakudex! Bye!")
            break
        # prompts for new input if 1-6 isn't inputted
        else:
            print("Unrecognized menu selection!")

