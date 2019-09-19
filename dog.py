import animal

class Dog(animal.Animal):
    # Required properties are defined inside the __init__ constructor method
    def bark(self):
        print("Woof! Woof!")
    def sit(self):
        print(self.name + " sits.")
    def roll(self):
        print(self.name + " rolls over.")

if __name__ == "__main__":
    my_dog = Dog("Sophie", 12)
    my_dog.sleep()
    my_dog.bark()
