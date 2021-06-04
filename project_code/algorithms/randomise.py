import random

def randomise_coordinates():

    x = random.randrange(0,180)
    y = random.randrange(0,160)
    return tuple((x, y))