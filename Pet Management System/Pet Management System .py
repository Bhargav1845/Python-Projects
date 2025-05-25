class Pet:
    def __init__(self, name ,species , age):
        self.name = name
        self.species = species
        self.age = age

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")

    def make_sound(self):
        if self.species.lower() == "dog":
            print(f"{self.name} says Woof!")
        elif self.species.lower() == "cat":
            print(f"{self.name} says moew!")
        else:
            print(f"{self.name} makes sound!")

pet1 = Pet("Buddy", "dog", 3)
pet2 = Pet("Whiskers", "cat", 2)

pet1.eat()
pet1.sleep()
pet1.make_sound()

pet2.eat()
pet2.sleep()
pet2.make_sound()