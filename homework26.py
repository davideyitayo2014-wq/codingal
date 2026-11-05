# Dog class

class Dog:
    # Class variable - same for all dogs
    species = "Canis familiaris"

    # __init__ - to create instance variables
    def __init__(self, breed, name):
        self.breed = breed  # instance variable 1
        self.name = name    # instance variable 2

    # Method to display details
    def display(self):
        print("Breed:", self.breed)
        print("Name:", self.name)
        print("Species:", Dog.species)
        print("-----------------")

# Creating 2 dogs of different breeds
dog1 = Dog("German Shepherd", "Max")
dog2 = Dog("Labrador", "Bella")

# Display details
dog1.display()
dog2.display()