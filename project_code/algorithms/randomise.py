import random
# from ..classes.land import Land


def randomise_coordinates(width, depth):
    x = random.randrange(0,(180 + 1 - width))
    y = random.randrange(0,(160 + 1 - depth))
    
    return tuple((x, y))

