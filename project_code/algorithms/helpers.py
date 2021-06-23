# Team SEB 
# Minor Programmeren (Programmeertheorie)  
# helpers.py
#
# - Performs helper functions.

import random
from project_code.classes.house import House
from shapely.geometry import Polygon
from copy import deepcopy


def randomise_coordinates(width, depth):
    x = random.randrange(0,(180 + 1 - width))
    y = random.randrange(0,(160 + 1 - depth))
    
    return tuple((x, y))

def random_choice(choices):
    return (random.choice(choices))

def rotation(coordinates, width, depth, placement, required_free_space): 
    if placement == 'vertical':
        # calculating new width and depth
        copy_width = deepcopy(width)
        copy_width_required_free_space = deepcopy(width + (2 * required_free_space))

        width = depth
        depth = copy_width
        width_with_required_free_space = depth + (2 * required_free_space)
        depth_with_required_free_space = copy_width_required_free_space
        

        # making polygons
        polygon = Polygon([(coordinates[0] + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + depth + required_free_space), (coordinates[0] + required_free_space, coordinates[1] + depth + required_free_space)])
        polygon_free_space = Polygon([coordinates, (coordinates[0] + width_with_required_free_space, coordinates[1]), (coordinates[0] + width_with_required_free_space, coordinates[1] + depth_with_required_free_space), (coordinates[0], coordinates[1] + depth_with_required_free_space)])

    if placement == 'horizontal':
        # making polygons
        width_with_required_free_space = width +(2 * required_free_space)
        depth_with_required_free_space = depth + (2 * required_free_space)
        polygon = Polygon([(coordinates[0] + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + depth + required_free_space), (coordinates[0] + required_free_space, coordinates[1] + depth + required_free_space)])
        polygon_free_space = Polygon([coordinates, (coordinates[0] + width_with_required_free_space, coordinates[1]), (coordinates[0] + width_with_required_free_space, coordinates[1] + depth_with_required_free_space), (coordinates[0], coordinates[1] + depth_with_required_free_space)])


    return (width, depth, polygon, polygon_free_space)

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
    
    # placement = old_house.placement
    # if placement == 'vertical':
        # rotation_finished = rotation(old_house.bottom_left, old_house.width, old_house.depth, 'horizontal', old_house.free_space)
    # else:
    rotation_finished = rotation(old_house.bottom_left, old_house.width, old_house.depth, 'vertical', old_house.free_space)

    new_house = House(old_house.name, rotation_finished[0], rotation_finished[1], old_house.price, old_house.bottom_left, rotation_finished[2], old_house.free_space, rotation_finished[3])
    copy_start_map.all_land_objects.remove(old_house)

    if copy_start_map.check_valid(new_house) == True:
        copy_start_map.all_land_objects.append(new_house)
        return copy_start_map
    else:
        return start_map

def calc_price(land_map):
    land_map.calculate_distance(land_map.all_land_objects)
    price = land_map.calculate_price(land_map.all_land_objects)
    # print(price)
    return price

def make_new_house(new_coordinates, old_house):
    x = new_coordinates[0]
    y = new_coordinates[1]
    # nieuwe polygonen maken
    # print(old_house.polygon)
    polygon = Polygon([(x, y), (x + old_house.width, new_coordinates[1]), (x, y + old_house.depth), (x + old_house.width, y + old_house.depth)])
    polygon_free_space = Polygon([(x + old_house.free_space, y + old_house.free_space), (x + old_house.width + old_house.free_space, new_coordinates[1] + old_house.free_space), (x + old_house.free_space, y + old_house.depth + old_house.free_space), (x + old_house.width + old_house.free_space, y + old_house.depth + old_house.free_space)])
    # print(polygon)
    # new huis maken
    new_house = House(old_house.name, old_house.width, old_house.depth, old_house.price, new_coordinates, polygon, old_house.free_space, polygon_free_space)
    return new_house

def move_house(start_map):
    price_startmap = calc_price(start_map)
    copy_start_map = deepcopy(start_map)

    old_house = random_choice(copy_start_map.all_land_objects)
    while (old_house.name == 'water'):
        old_house = random_choice(copy_start_map.all_land_objects)

    choices_move = ['left', 'right', 'up', 'down', 'up_left', 'up_right', 'down_left', 'down_right','left_1', 'right_1', 'up_1', 'down_1', 'up_left_1', 'up_right_1', 'down_left_1', 'down_right_1']

    direction_dict = {"left":(-2, 0), "down_left":(-2, -2), "up_left":(-2, 2), "right":(2, 0), "up_right":(2, 2), "down_right": (2, -2),
                    "up": (0, 2), "down":(0, -2), "left_1":(-1, 0), "down_left_1":(-1, -1), "up_left_1":(-1, 1), "right_1":(1, 0),
                    "up_right_1": (1, 1), "down_right_1":(1, -1), "up_1": (0, 1), "down_1":(0, -1)}

    highest_price = price_startmap
    best_map = start_map
    move = random_choice(choices_move)
    # for move in choices_move:
    (bottom_left_x_change , bottom_left_y_change)  = direction_dict[move]
    new_coordinates = tuple((old_house.bottom_left[0] + bottom_left_x_change, old_house.bottom_left[1] + bottom_left_y_change))
    new_house = make_new_house(new_coordinates, old_house)
    copy_start_map.all_land_objects.remove(old_house)

    if copy_start_map.check_valid(new_house) == True:
        copy_start_map.all_land_objects.append(new_house)
        price = calc_price(copy_start_map)
        if price >= highest_price:
            highest_price = price
            best_map = copy_start_map

    return best_map

