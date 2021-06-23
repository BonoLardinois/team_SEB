# Team SEB 
# Minor Programmeren (Programmeertheorie)  
# genetic.py
#
# - Genetic algorithm; 
# - Creates multiple generations of maps and attempts to find the highest score.

from project_code.classes.house import House
from copy import deepcopy
from project_code.algorithms.helpers import rotation, randomise_coordinates
import matplotlib.pyplot as plt
from random import choice
from .helpers import swap_with_random_rotation

DIRECTIONS = ["UP","RIGHT","DOWN","LEFT","TOP_RIGHT", "BOTTOM_RIGHT", "TOP_LEFT", "BOTTOM_LEFT"]
STEPS = 1
NR_MOVES = 10
GENERATIONS = 200
TOP_X = 20


def do_random_move(land):
    '''
    Randomly moves houses on map and returns new map
    '''
    # create local variables to use in both loops
    i = 0
    house = None
    # get a land object that isn't water by index
    while True:
        i = choice(range(len(land.all_land_objects)))
        if land.all_land_objects[i].name == 'water':
            continue
        house = deepcopy(land.all_land_objects[i])
        break
    for x in range(100):
        # get random direction
        direction = choice(DIRECTIONS)
        # move houses by STEPS number of coordinates
        if direction == "UP":
            house.move(0,STEPS)
        elif direction == "RIGHT":
            house.move(STEPS,0)
        elif direction == "DOWN":
            house.move(0,-STEPS)
        elif direction == "LEFT":
            house.move(-STEPS,0)
        elif direction == "TOP_RIGHT":
            house.move(STEPS, STEPS)
        elif direction == "TOP_LEFT":
            house.move(-STEPS, STEPS)
        elif direction == "BOTTOM_RIGHT":
            house.move(STEPS, -STEPS)
        else:
            house.move(-STEPS, -STEPS)
        if check_valid(land, house):
            # if there is no overlap we add the random house
            land.all_land_objects[i] = house
            break

    return land

def check_valid(land, house):
    '''
    Function to check for overlap (doesn't append land_objects)
    '''
    if not house.check_bounds(land.width, land.depth):
        return False
    # checks all land objects; if no overlap, return true
    for land_object in land.all_land_objects:
        if land_object.name != 'water':
            if house.polygon_free_space.intersects(land_object.polygon) == True or land_object.polygon_free_space.intersects(house.polygon_free_space) == True:
                return False     
        elif land_object.name == 'water':
            if land_object.polygon.intersects(house.polygon) == True:
                return False
    return True

class Genetic():

    def __init__(self, housing_map, number_houses, iterations):
        self.housing_map = housing_map
        self.maisons = None
        self.bungalows = None 
        self.familyhomes = None
        self.calculate_houses(number_houses)
        self.winner = self.run(housing_map, number_houses, iterations)

    def calculate_houses(self, number_houses):
        '''
        Calculates how many houses need to be placed
        '''
        self.maisons = int(0.15 * number_houses)
        self.bungalows = int(0.25 * number_houses)
        self.familyhomes = int(0.6 * number_houses)

    def load_houses(self, number_houses, housing_map):
        '''
        Function to load all houses in a specific neighbourhood
        '''
        numb_maisons = int(0.15 * number_houses)
        numb_bungalows = int(0.25 * number_houses)
        numb_familyhouses = int(0.6 * number_houses)
        houses_to_place = {
            'maison': [12,10,24,22,6,numb_maisons, 610000],
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
                placement = choice(['horizontal', 'vertical'])
                while (overlap):
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

        return (housing_map)



    def run(self, housing_map, number_houses, iterations):
        '''
        Gets multiple maps, mutates them and keeps track of highest scoring one
        '''
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
            generation.append((resulting_map, value))

        # sort generation by value of map
        generation = sorted(generation,key=lambda z : z[1],reverse=True)
        # print(generation[0][1])

        # define variables for generation graph
        results = []
        total_generations = []
        generation_counter = 1

        # define variables to increase number of moves if best map remains the same
        best_so_far = -1
        extra_moves = 0

        # for a number of generations, create new generation
        for z in range(GENERATIONS):
            new_generation = []

            # make mutations to create new maps and keep old maps
            for g in range(len(generation)):
                for x in range(NR_MOVES):
                    new_map = deepcopy(generation[g][0]) 

                    swapped_map = swap_with_random_rotation(new_map)
                    for _ in range( 1 + extra_moves):
                        swapped_map = do_random_move(swapped_map)
                    swapped_map.calculate_distance(swapped_map.all_land_objects)
                    value = swapped_map.calculate_price(swapped_map.all_land_objects)

                    new_generation.append((swapped_map, value))
                            
                new_generation.append(generation[g])
            
            # sort this new generation by value and keep top X
            new_generation = sorted(new_generation,key=lambda z : z [1], reverse=True)
            generation = new_generation[:TOP_X]

            # if the best map of the previous generation has the same value as the new one, 
            # increase the number of moves
            if generation[0][1]  == best_so_far:
                extra_moves += 1
            else:
                extra_moves = 0 
            best_so_far = generation [0][1]

            # keep track of generations
            generation_counter += 1
            total_generations.append(generation_counter)

            results.append(new_generation[0][1])

            # print value of the best map from this new generation
            value = round(new_generation[0][1])
            print(f"Generation number: {generation_counter}")
            print(value)

        # visualise generations graph
        plt.plot(total_generations, results)
        plt.xlabel('x axis')
        plt.ylabel('y axis') 
        plt.title('Graph')
        plt.margins(0,0)
        plt.savefig('output/genetic_graph.png')

        # return the housing map with the best value
        return generation[0][0]
   

    
            
        
    

        
       
