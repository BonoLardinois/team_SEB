from .render_randomise import Randomise
import random
from copy import deepcopy
from project_code.algorithms.rotation import rotation
from project_code.classes.house import House
from shapely.geometry import Polygon

class Hillclimber():

    def __init__(self, empty_graph, number_houses, iterations, iterations_randomise):
        self.winner = self.run(iterations, empty_graph, number_houses, iterations_randomise)

    def random_choice(self, choices):
        return (random.choice(choices))

    def swap_with_random_rotation(self, start_map):
        copy_start_map = deepcopy(start_map)
        house1 = self.random_choice(copy_start_map.all_land_objects)
        house2 = self.random_choice(copy_start_map.all_land_objects)
        while (house1.name == 'water' or house2.name == 'water' or house2.name == house1.name):
            # print("chooses again")
            if house1.name == 'water':
                house1 = self.random_choice(copy_start_map.all_land_objects)
            if house2.name == 'water':
                house2 = self.random_choice(copy_start_map.all_land_objects)
            if house2.name == house1.name:
                house2 = self.random_choice(copy_start_map.all_land_objects)

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

    def run(self, iterations, empty_graph, number_houses, iterations_randomise):
        highest_scoring_map = Randomise(empty_graph, number_houses, iterations_randomise).winner
        print(f"price after randomise: {highest_scoring_map.total}")

        for n in range(iterations):
            copy_highest_scoring_map = deepcopy(highest_scoring_map)

            swapped_map = self.swap_with_random_rotation(copy_highest_scoring_map)
            
            swapped_map.calculate_distance(swapped_map.all_land_objects)
            value_swapped_map = (swapped_map.calculate_price(swapped_map.all_land_objects))
            
            if value_swapped_map > highest_scoring_map.total :
                highest_scoring_map = swapped_map
            
            
        print(f"Total number land objects placed: {len(highest_scoring_map.all_land_objects)}")
        return highest_scoring_map