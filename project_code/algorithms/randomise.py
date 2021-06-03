import random

def randomise_coordinates():

    x = random.randrange(0,180)
    y = random.randrange(32,160)
    return tuple((x, y))