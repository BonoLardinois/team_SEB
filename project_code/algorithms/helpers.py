import random
from copy import deepcopy
from project_code.algorithms.rotation import rotation
from project_code.classes.house import House


def random_choice(choices):
    return (random.choice(choices))

def swap_with_random_rotation(start_map):
    copy_start_map = deepcopy(start_map)
    house1 = random_choice(copy_start_map.all_land_objects)
    house2 = random_choice(copy_start_map.all_land_objects)
    while (house1.name == 'water' or house2.name == 'water' or house2.name == house1.name):
        # print("chooses again")
        if house1.name == 'water':
            house1 = random_choice(copy_start_map.all_land_objects)
        if house2.name == 'water':
            house2 = random_choice(copy_start_map.all_land_objects)
        if house2.name == house1.name:
            house2 = random_choice(copy_start_map.all_land_objects)

    # rotatie
    placement = random.choice(['horizontal', 'vertical'])

    # house 1 naar house2 locatie
    rotation_finished = rotation(house2.bottom_left, house1.width, house1.depth, placement, house1.free_space)
    width = rotation_finished[0]
    depth = rotation_finished[1]
    polygon = rotation_finished[2]
    polygon_free_space = rotation_finished[3]
    coordinates_no_free_space = tuple((house2.bottom_left[0] + house1.free_space, house2.bottom_left[1] + house1.free_space))

    # maak new house object
    house_1 = House(house1.name, width, depth, house1.price, house2.bottom_left, polygon, house1.free_space, polygon_free_space)

    #house 2 naar house 1 locatoe
    rotation_finished_1 = rotation(house1.bottom_left, house2.width, house2.depth, placement, house2.free_space)
    width = rotation_finished_1[0]
    depth = rotation_finished_1[1]
    polygon = rotation_finished_1[2]
    polygon_free_space = rotation_finished_1[3]
    coordinates_no_free_space = tuple((house1.bottom_left[0] + house2.free_space, house1.bottom_left[1] + house2.free_space))

    # maak new house object
    house_2 = House(house2.name, width, depth, house2.price, house1.bottom_left, polygon, house2.free_space, polygon_free_space)

    copy_start_map.all_land_objects.remove(house1)
    copy_start_map.all_land_objects.remove(house2)

    if copy_start_map.check_valid(house_2) == True and copy_start_map.check_valid(house_1) == True:
        copy_start_map.all_land_objects.append(house_2)
        copy_start_map.all_land_objects.append(house_1)
        # print("New startmap")
        # print("overlap house2")
        return copy_start_map

    # print("return normal map")
    return start_map

def rotate(start_map):
    copy_start_map = deepcopy(start_map)
    old_house = random_choice(copy_start_map.all_land_objects)

    while (old_house.name == 'water'):
        old_house = random_choice(copy_start_map.all_land_objects)
    
    placement = old_house.placement
    if placement == 'vertical':
        rotation_finished = rotation(old_house.bottom_left, old_house.width, old_house.depth, 'horizontal', old_house.free_space)
    else:
        rotation_finished = rotation(old_house.bottom_left, old_house.width, old_house.depth, 'vertical', old_house.free_space)

    new_house = House(old_house.name, rotation_finished[0], rotation_finished[1], old_house.price, old_house.bottom_left, rotation_finished[2], old_house.free_space, rotation_finished[3])
    copy_start_map.all_land_objects.remove(old_house)

    if copy_start_map.check_valid(new_house) == True:
        copy_start_map.all_land_objects.append(new_house)
        return copy_start_map
    else:
        return start_map


