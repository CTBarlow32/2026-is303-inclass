'''
Inputs
- A string containing a attribute guess or the guess of the animals name

Proccesses:
- Randomly select an Animal
- Allow user to guess until they guess correct animal
- When they guess, tell them if the animal has attribute or not
- Tell user when they guess correctly

Output
- Attribute guess correctness
- Congratulations message
'''

import random
   #teach python how to create random stuff

ANIMALS = {
    "Lion" : ["Mammal", "Four legs", "Predator", "Africa", "Main", "Roar", "Yellow", "Eats meat"],
    "Hyena" : ["Mammal", "Four legs", "Predator", "Spots", "Scavanger", "Lion king", "Dirty", "Pack"],
    "Black bear" : [ "Mammal", "Four legs", "Herbavore", "Carnivore", "Brown", "Claws", "Hibernation", "Forests"],
    "Snake" : [ "Reptile", "No legs", "Predator", "Venomous", "Slither", "Hiss", "Scales", "Cold blooded"],
    "Eagle" : [ "Bird", "Two legs", "Predator", "Fly", "Sharp vision", "Beak", "Feathers", "Nest"],
    "Shark" : [ "Fish", "No legs", "Predator", "Swim", "Fins", "Teeth", "Gills", "Ocean"],
    "Frog" : [ "Amphibian", "Four legs", "Herbavore", "Jump", "Croak", "Tadpole", "Wet skin", "Ponds"],
    "Elephant" : [ "Mammal", "Four legs", "Herbavore", "Trunk", "Tusks", "Large ears", "Gray", "Africa"],
    "Giraffe" : [ "Mammal", "Four legs", "Herbavore", "Long neck", "Spots", "Tall", "Africa", "Leaves"],
    "Cheetah" : [ "Mammal", "Four legs", "Predator", "Fast", "Spots", "Africa", "Roar", "Carnivore"],
    "Zebra" : [ "Mammal", "Four legs", "Herbavore", "Stripes", "Africa", "Hooves", "Grazing", "Wild"]
}

WELCOME_MESSAGE = """Animal guessing game
I have picked a random animal. Guess an 
attribute or the name of the animal.
"""

CONGRATUALTIONS_MESSAGE = "You won!"

list_of_animal_names = list(ANIMALS.keys())
random_animal = random.choice(list_of_animal_names)
random_animal_attributes = ANIMALS[random_animal]

print(WELCOME_MESSAGE)

guess = ""

while guess != random_animal:
    guess = input("Please guess an attribute or the animal name: ").capitalize()
    if guess in random_animal_attributes:
        print(f"Yes, {guess} is an attribute of the animal.")
    elif guess == random_animal:
        print(CONGRATUALTIONS_MESSAGE)
    else:
        print(f"No, {guess} is NOT an attribute of an animal.")
