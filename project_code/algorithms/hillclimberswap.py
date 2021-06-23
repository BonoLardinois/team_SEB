# Team SEB 
# Minor Programmeren (Programmeertheorie)  
# hillclimberswap.py
#
# - HillClimber algorithm that swaps houses when beneficial to value of map.
# - Swaps two houses and checks if this is valid
# - if valid compare the two maps and choose the highest

from .render_randomise import Randomise
import random
from copy import deepcopy
from .helpers import swap_with_random_rotation

class Hillclimber():

    def __init__(self, empty_graph, number_houses, iterations, iterations_randomise):
        self.winner = self.run(iterations, empty_graph, number_houses, iterations_randomise)

    def random_choice(self, choices):
    '''
    Makes random choice
    '''
        return (random.choice(choices))

    def run(self, iterations, empty_graph, number_houses, iterations_randomise):
    '''
    Runs swap alogoritm for n iterations and returns the highest scoring map
    '''
        highest_scoring_map = Randomise(empty_graph, number_houses, iterations_randomise).winner
        print(f"price after randomise: {highest_scoring_map.total}")
        
        for n in range(iterations):
            copy_highest_scoring_map = deepcopy(highest_scoring_map)

            swapped_map = swap_with_random_rotation(copy_highest_scoring_map)
            
            swapped_map.calculate_distance(swapped_map.all_land_objects)
            value_swapped_map = (swapped_map.calculate_price(swapped_map.all_land_objects))
            
            if value_swapped_map > highest_scoring_map.total :
                highest_scoring_map = swapped_map
            
            
        print(f"Total number land objects placed: {len(highest_scoring_map.all_land_objects)}")
        return highest_scoring_map