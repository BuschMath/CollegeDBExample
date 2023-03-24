import random

def generateRandomName():
    # Define a list of possible characters for first names
    possible_chars = "abcdefghijklmnopqrstuvwxyz"

    name_length = random.randint(3,12)
    name_chars = [random.choice(possible_chars) for _ in range(name_length)]
    name = ''.join(name_chars).capitalize()

    return name