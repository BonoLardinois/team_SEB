import random

def randomise_coordinates(width, depth):

    x = random.randrange(0,(180 - width))
    y = random.randrange(0,(160 - depth))
    return tuple((x, y))