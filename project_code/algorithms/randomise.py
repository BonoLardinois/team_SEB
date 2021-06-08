import random
# from ..classes.land import Land

def randomise_coordinates(width, depth):
    #width1 = width
    #depth1 = depth
    #available_coordinates1 = available_coordinates

    x = random.randrange(0,(180 + 1 - width))
    y = random.randrange(0,(160 + 1 - depth))

    #for x in range(181 - width, 181):
        #for y in range(161 - depth, 161):
            #coordinate = tuple((x, y))
            #if coordinate not in available_coordinates1:
                #print(coordinate)
                #continue
    #z = random.choice(available_coordinates)
    #print(z)
    #return z
    return tuple((x, y))

