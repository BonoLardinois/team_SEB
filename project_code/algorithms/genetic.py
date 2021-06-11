from project_code.classes.land import Land
from project_code.classes.house import House
from shapely.geometry import Polygon
import random
from project_code.algorithms.randomise import randomise_coordinates
from copy import deepcopy

NR_MOVES = 5
GENERATIONS = 10
TOP_X = 20
class Genetic():

    def __init__(self, housing_map, number_houses, iterations):
        self.housing_map = housing_map
        self.maisons = None
        self.bungalows = None 
        self.familyhomes = None
        self.calculate_houses(number_houses)
        self.winner = self.run(housing_map, number_houses, iterations)
        # self.choices = {maison: self.maisons, bungalow: self.bungalows, familyhome: self.familyhomes}

    def calculate_houses(self, number_houses):
        self.maisons = int(0.15 * number_houses)
        self.bungalows = int(0.25 * number_houses)
        self.familyhomes = int(0.6 * number_houses)

    def load_houses(self, number_houses, housing_map):
        '''
        function to load all houses in a specific neighbourhood
        '''
        for i in range(int(0.15 * number_houses)):
            width = 12
            depth = 10
            width2 = 24
            depth2 = 22
            required_free_space = 6
            overlap = True
            maison = None
            while (overlap):
                coordinates = randomise_coordinates(width2, depth2)
                polygon = Polygon([(coordinates[0] + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + depth + required_free_space), (coordinates[0] + required_free_space, coordinates[1] + depth + required_free_space)])
                
                # polygon with required free space, created to calculate price of house
                polygon_free_space = Polygon([coordinates, (coordinates[0] + width2, coordinates[1]), (coordinates[0] + width2, coordinates[1] + depth2), (coordinates[0], coordinates[1] + depth2)])
                coordinates2 = tuple((coordinates[0] + required_free_space, coordinates[1] + required_free_space))
                maison = House("maison", width, depth, 610000, coordinates2, polygon, 6, polygon_free_space)
                overlap = housing_map.overlap(maison)  

        for i in range(int(0.25 * number_houses)):
            width = 11
            depth = 7
            width2 = 17
            depth2 = 19
            required_free_space = 3
            overlap = True
            bungalow = None
            while (overlap):
                coordinates = randomise_coordinates(width2, depth2)
                polygon = Polygon([(coordinates[0] + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + depth + required_free_space), (coordinates[0] + required_free_space, coordinates[1] + depth + required_free_space)])

                # polygon with required free space, created to calculate price of house
                polygon_free_space = Polygon([coordinates, (coordinates[0] + width2, coordinates[1]), (coordinates[0] + width2, coordinates[1] + depth2), (coordinates[0], coordinates[1] + depth2)])
                coordinates2 = tuple((coordinates[0] + required_free_space, coordinates[1] + required_free_space))
                bungalow = House("bungalow", width, depth, 399000, coordinates2, polygon, 3, polygon_free_space)
                overlap = housing_map.overlap(bungalow)

        for i in range(int(0.6 * number_houses)):
            width = 8
            depth = 8
            width2 = 12
            depth2 = 12
            required_free_space = 2
            overlap = True
            familyhome = None
            while(overlap):
                coordinates = randomise_coordinates(width2, depth2)
                polygon = Polygon([(coordinates[0] + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + depth + required_free_space), (coordinates[0] + required_free_space, coordinates[1] + depth + required_free_space)])

                # polygon with required free space, created to calculate price of house
                polygon_free_space = Polygon([coordinates, (coordinates[0] + width2, coordinates[1]), (coordinates[0] + width2, coordinates[1] + depth2), (coordinates[0], coordinates[1] + depth2)])
                coordinates2 = tuple((coordinates[0] + required_free_space, coordinates[1] + required_free_space))
                familyhome = House("familyhome", width, depth, 285000, coordinates2, polygon, 2, polygon_free_space)
                overlap = housing_map.overlap(familyhome)

        return (housing_map)


    # def choose_random_house()
    #     type_house = random.choice(list(self.choices.keys()))
    #     self.choices[type_house] = self.choices[type_house] - 1
    #     if self.choices[type_house] == 0:
    #         self.choices.pop(type_house)
    #     load_houses(type_house)
    #     print(self.choices)
        
    def run(self, housing_map, number_houses, iterations):
        # initial generation
        generation= [] 

        # create a number of random maps
        for n in range(iterations):
            copy_map = deepcopy(housing_map)
            
            # place houses on those maps
            resulting_map = self.load_houses(number_houses, copy_map)
            
            # calculate value of map
            resulting_map.calculate_distance(resulting_map.all_land_objects)
            value = resulting_map.calculate_price(resulting_map.all_land_objects)

            # add map to list
            generation.append((resulting_map,value))

        # sort generation by value of map
        generation = sorted(generation,key=lambda z : z[1],reverse=True)
        print(generation[0][1])

        # for a number of generations, create new generation
        for z in range(GENERATIONS):
            new_generation = []

            # make mutations to create new maps and keep old maps
            for g in range(len(generation)):
                for x in range(NR_MOVES):
                    new_map = deepcopy(generation[g][0])
                    new_map.do_random_move()
                    new_map.calculate_distance(new_map.all_land_objects)
                    value = new_map.calculate_price(new_map.all_land_objects)
                    new_generation.append((new_map, value))
                new_generation.append(generation[g])
            
            # sort this new generation by value and keep top X
            new_generation = sorted(new_generation,key=lambda z : z [1], reverse=True)
            generation = new_generation[:TOP_X]
            # print value of the best map from this new generation
            print(new_generation[0][1])
        # return the housing map with the best value
        return generation[0][0]
   


            
        
    

        
       
