# Team SEB 
# Minor Programmeren (Programmeertheorie)  
# simulated_annealing.py
#
# - Simulated Annealing algorithm.
# - probabillity of accepting a worse map drops when the temperatur drops
# - eventually returns the map close to the global opitmum 

import random
import math
from .render_randomise import Randomise
from .helpers import swap_with_random_rotation, rotate, move_house
from copy import deepcopy
from project_code.visualisations.visualise import visualise

class Simulated_annealing():

    def __init__(self, empty_graph, number_houses):
        self.start_map = Randomise(empty_graph, number_houses, 400).winner
        self.calc_price(self.start_map)
        self.end_result = self.simulated_annealing(self.start_map)

    def calc_price(self, land_map):
        '''
        Calculates total price of a map
        '''
        land_map.calculate_distance(land_map.all_land_objects)
        price = land_map.calculate_price(land_map.all_land_objects)
        # print(price)
        return price
    
    def simulated_annealing(self, start_map):
        '''
        Performce
        '''
        # setting starting temperatur
        temp = 76001
        alpha = 1
        final_temp = 0.99

        current_temp = temp

        current_state = deepcopy(self.start_map)
        counter = 0
        counter2 = 0
        price_counter = 0

        while current_temp > final_temp:
            highest_map = current_state

            # rotate house
            rotated_map = rotate(highest_map)
            highest_map = rotated_map

            # move house
            moved_map = move_house(highest_map)
            highest_map = moved_map

            # swap two houses
            swapped_map = swap_with_random_rotation(highest_map)
            highest_map = swapped_map

            # new_map = moved_map
            new_map = highest_map

            # calculate difference in price
            price_new_map = self.calc_price(new_map)

            difference = price_new_map - current_state.total
            
            # if a shoulder is being reached then the algoritm reheats
            if counter2 <= 10:
                if difference == 0.0:
                    counter += 1
                    if counter == 4:
                        counter = 0
                        counter2 += 1
                        current_temp = 76000
                else:
                    counter = 0 

            print(f"difference: {difference}")

            # if the new map is better then the old map then it replaces it
            if difference >= 0.0:
                current_state = deepcopy(new_map)
                
            probability = math.exp(difference/current_temp)
            random_number = random.uniform(0,1)
            if random_number < probability:
                current_state = deepcopy(new_map)
  
            current_temp = current_temp - alpha

            print(f"current temp: {current_temp}")
            print(f"value:{current_state.total}")
        
        return current_state