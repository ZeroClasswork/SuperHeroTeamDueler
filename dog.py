# dog.py
class Dog: 
    # Required properties are defined inside the __init__ constructor method
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print("Woof!")
    def sit(self):
        print(self.name + " sits.")
    def roll(self):
        print(self.name + " rolls over.")