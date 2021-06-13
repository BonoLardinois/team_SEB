from project_code.classes.land import Land
from project_code.classes.house import House
from shapely.geometry import Polygon
import random
from project_code.algorithms.randomise import randomise_coordinates
from copy import deepcopy
from project_code.algorithms.rotation import rotation


class Randomise():

    def __init__(self, housing_map, number_houses, iterations):
        self.housing_map = housing_map
        self.maisons = None
        self.bungalows = None 
        self.familyhomes = None
        self.calculate_houses(number_houses)
        self.winner = self.run(housing_map, number_houses, iterations)

    def calculate_houses(self, number_houses):
        self.maisons = int(0.15 * number_houses)
        self.bungalows = int(0.25 * number_houses)
        self.familyhomes = int(0.6 * number_houses)

    def load_houses(self, number_houses, housing_map):
        '''
        function to load all houses in a specific neighbourhood
        '''
        numb_maisons = int(0.15 * number_houses)
        numb_bungalows = int(0.25 * number_houses)
        numb_familyhouses = int(0.6 * number_houses)
        houses_to_place = {
            'maison': [12,10,24,22,6,int(0.15 * number_houses), 610000],
            'bungalow': [11,7,17,19,3,numb_bungalows, 399000],
            'familyhome': [8,8,12,12,2,numb_familyhouses, 285000]
            }
        for house_type in houses_to_place:
            values = (houses_to_place[house_type])

            for i in range(values[5]):

                # all values for one house
                width = values[0]
                depth = values[1]
                width_with_required_free_space = values[2]
                depth_with_required_free_space = values[3]
                required_free_space = values[4]
                price = values[6]
                overlap = True
                placement = random.choice(['horizontal', 'vertical'])
                counter = 0
                while (overlap):
                    if counter == 200:
                        counter = 0
                        break
                    # get coordinates
                    coordinates = randomise_coordinates(width_with_required_free_space, depth_with_required_free_space)

                    # get type of placement
                    rotation_finished = rotation(coordinates, width, depth, placement, required_free_space)
                    width = rotation_finished[0]
                    depth = rotation_finished[1]
                    polygon = rotation_finished[2]
                    polygon_free_space = rotation_finished[3]

                    # get coordinates with required free space
                    coordinates_with_free_space = tuple((coordinates[0] + required_free_space, coordinates[1] + required_free_space))

                    # make house object
                    house = House(house_type, width, depth, price, coordinates_with_free_space, polygon, required_free_space, polygon_free_space)

                    # check if overlap
                    overlap = housing_map.overlap(house) 
                    counter += 1

        return (housing_map)
        
    def run(self, housing_map, number_houses, iterations):
        '''
        function for generating maps with randomly placed houses and picking the highest value map
        '''

        highest_scoring_map = None
        highest_score = 0
        for n in range(iterations):
            copy_map = deepcopy(housing_map)
            resulting_map = self.load_houses(number_houses, copy_map)
            
            resulting_map.calculate_distance(resulting_map.all_land_objects)
            total_value = resulting_map.calculate_price(resulting_map.all_land_objects)
            
            if total_value > highest_score:
                highest_scoring_map = resulting_map
                highest_score = total_value
        
        return highest_scoring_map
   


            
        
    

        
       
