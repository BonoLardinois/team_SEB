from .render_randomise import Randomise
import random
from copy import deepcopy
from project_code.algorithms.rotation import rotation
from project_code.classes.house import House
from shapely.geometry import Polygon

class Hillclimber():

    def __init__(self, empty_graph, number_houses, iterations):
        self.winner = self.run(iterations, empty_graph, number_houses)

    def random_choice(self, choices):
        return (random.choice(choices))

    # def swap(self, start_map):
    #     house1 = self.random_choice(start_map.all_land_objects)
    #     house2 = self.random_choice(start_map.all_land_objects)
    #     while (house1.name == 'water' or house2.name == 'water' or house2.name == house1.name):
    #         # print("chooses again")
    #         if house1.name == 'water':
    #             house1 = self.random_choice(start_map.all_land_objects)
    #         if house2.name == 'water':
    #             house2 = self.random_choice(start_map.all_land_objects)
    #         if house2.name == house1.name:
    #             house2 = self.random_choice(start_map.all_land_objects)

    #     start_map.all_land_objects.remove(house1)
    #     start_map.all_land_objects.remove(house2)

    #     # coordinaten omwisselen
    #     copy_coordinates_house2 = deepcopy(house2.bottom_left)
    #     new_coordinates_house1 = house1.bottom_left
    #     new_coordinates_house2 = copy_coordinates_house2


    #     # house 1 naar house2 locatie
    #     coordinates = new_coordinates_house2
    #     width_with_required_free_space = house1.width +(2 * house1.free_space)
    #     depth_with_required_free_space = house1.depth + (2 * house1.free_space)
    #     polygon = Polygon([(coordinates[0] + house1.free_space, coordinates[1] + house1.free_space), (coordinates[0] + house1.width + house1.free_space, coordinates[1] + house1.free_space), (coordinates[0] + house1.width + house1.free_space, coordinates[1] + house1.depth + house1.free_space), (coordinates[0] + house1.free_space, coordinates[1] + house1.depth + house1.free_space)])
    #     polygon_free_space = Polygon([coordinates, (coordinates[0] + width_with_required_free_space, coordinates[1]), (coordinates[0] + width_with_required_free_space, coordinates[1] + depth_with_required_free_space), (coordinates[0], coordinates[1] + depth_with_required_free_space)])

    #     house_1 = House(house1.name, house1.width, house1.depth, house1.price, new_coordinates_house2, polygon, house1.free_space, polygon_free_space)

    
    #     #house 2 naar house 1 locatoe
    #     coordinates = new_coordinates_house1
    #     width_with_required_free_space = house2.width +(2 * house2.free_space)
    #     depth_with_required_free_space = house2.depth + (2 * house2.free_space)
    #     polygon = Polygon([(coordinates[0] + house2.free_space, coordinates[1] + house2.free_space), (coordinates[0] + house2.width + house2.free_space, coordinates[1] + house2.free_space), (coordinates[0] + house2.width + house2.free_space, coordinates[1] + house2.depth + house2.free_space), (coordinates[0] + house2.free_space, coordinates[1] + house2.depth + house2.free_space)])
    #     polygon_free_space = Polygon([coordinates, (coordinates[0] + width_with_required_free_space, coordinates[1]), (coordinates[0] + width_with_required_free_space, coordinates[1] + depth_with_required_free_space), (coordinates[0], coordinates[1] + depth_with_required_free_space)])

    #     house_2 = House(house2.name, house2.width, house2.depth, house2.price, new_coordinates_house1, polygon, house2.free_space, polygon_free_space)

    #     if start_map.check_valid(house_2) == True or start_map.check_valid(house_1) == True:
    #         # print("overlap house2")
    #         return None

    #     start_map.all_land_objects.append(house_2)
    #     start_map.all_land_objects.append(house_1)

    #     return start_map


    def swap_with_random_rotation(self, start_map):

        house1 = self.random_choice(start_map.all_land_objects)
        house2 = self.random_choice(start_map.all_land_objects)
        while (house1.name == 'water' or house2.name == 'water' or house2.name == house1.name):
            # print("chooses again")
            if house1.name == 'water':
                house1 = self.random_choice(start_map.all_land_objects)
            if house2.name == 'water':
                house2 = self.random_choice(start_map.all_land_objects)
            if house2.name == house1.name:
                house2 = self.random_choice(start_map.all_land_objects)

        start_map.all_land_objects.remove(house1)
        start_map.all_land_objects.remove(house2)

        # coordinaten omwisselen
        copy_coordinates_house2 = deepcopy(house2.bottom_left)
        new_coordinates_house1 = house1.bottom_left
        new_coordinates_house2 = copy_coordinates_house2



        # rotatie
        placement = random.choice(['horizontal', 'vertical'])

        # house 1 naar house2 locatie
        rotation_finished = rotation(new_coordinates_house2, house1.width, house1.depth, placement, house1.free_space)
        width = rotation_finished[0]
        depth = rotation_finished[1]
        polygon = rotation_finished[2]
        polygon_free_space = rotation_finished[3]
        coordinates_no_free_space = tuple((new_coordinates_house2[0] + house1.free_space, new_coordinates_house2[1] + house1.free_space))

        # maak new house object
        house_1 = House(house1.name, width, depth, house1.price, new_coordinates_house2, polygon, house1.free_space, polygon_free_space)

        #house 2 naar house 1 locatoe
        rotation_finished = rotation(new_coordinates_house1, house2.width, house2.depth, placement, house2.free_space)
        width = rotation_finished[0]
        depth = rotation_finished[1]
        polygon = rotation_finished[2]
        polygon_free_space = rotation_finished[3]
        coordinates_no_free_space = tuple((new_coordinates_house1[0] + house2.free_space, new_coordinates_house1[1] + house2.free_space))

        # maak new house object
        house_2 = House(house2.name, width, depth, house2.price, new_coordinates_house1, polygon, house2.free_space, polygon_free_space)
        if start_map.check_valid(house2) == True or start_map.check_valid(house1) == True:
            # print("overlap house2")
            return None

        start_map.all_land_objects.append(house_2)
        start_map.all_land_objects.append(house_1)

        return start_map


    # def swap2(self, start_map):
    #     unordered = []
    #     maisons = []
    #     most_free_space =

    #     for land_object in start_map.all_land_objects:
    #         if land_object.name == 'maison':
    #             maisons.append(land_object)
    #         if land_object.name != 'water' and land_object.name != 'maison':
    #             unordered.append(land_object)
    #             print(land_object.name, land_object.nearest_neighbour)
    #             # if land_object.nearest_neighbour > house_with_most_free_space.nearest_neighbour:
    #             #     house_with_most_free_space = land_object

    #     # land_object
    #     # print(maisons)
    #     # print(house_with_most_free_space.name, house_with_most_free_space.nearest_neighbour)
        
    
    def run(self, iterations, empty_graph, number_houses):
        highest_scoring_map = Randomise(empty_graph, number_houses, 500).winner
        highest_score = 0

        for n in range(iterations):
            copy_highest_scoring_map = deepcopy(highest_scoring_map)

            #swapped_map = self.swap(copy_highest_scoring_map)
            swapped_map = self.swap_with_random_rotation(copy_highest_scoring_map)
            if swapped_map == None:
                continue
            
            swapped_map.calculate_distance(swapped_map.all_land_objects)
            value_swapped_map = (swapped_map.calculate_price(swapped_map.all_land_objects))
            
            if value_swapped_map > highest_scoring_map.total :
                highest_scoring_map = swapped_map

        return highest_scoring_map