import random
import math
from .render_randomise import Randomise
from .helpers import swap_with_random_rotation, rotate, move_house
from copy import deepcopy

class Simulated_annealing():

    def __init__(self, empty_graph, number_houses):
        self.start_map = Randomise(empty_graph, number_houses, 400).winner
        self.calc_price(self.start_map)
        self.end_result = self.simulated_annealing(self.start_map)

    def calc_price(self, land_map):
        land_map.calculate_distance(land_map.all_land_objects)
        price = land_map.calculate_price(land_map.all_land_objects)
        # print(price)
        return price
    
    def simulated_annealing(self, start_map):
        # temp bepalen aan de hand van plotje. niet nooit verslechteren. 
        temp = 86858
        alpha = 0.1
        final_temp = 0.99

        current_temp = temp

        current_state = deepcopy(self.start_map)
        counter = 0
        counter2 = 0
        price_counter = 0

        while current_temp > final_temp:

            # next_move = random.choice(['rotate', 'move', 'swap'])
            
            # iets doen met de huidige map
            highest_map = current_state

            # - draaien
            rotated_map = rotate(highest_map)
            highest_map = rotated_map

            # - verplaatsen 
            moved_map = move_house(highest_map)
            highest_map = moved_map

            # - verwisselen
            swapped_map = swap_with_random_rotation(highest_map)
            highest_map = swapped_map

            # new_map = moved_map
            new_map = highest_map

            # checken wat het vershil in totale prijs is
            price_new_map = self.calc_price(new_map)

            difference = price_new_map - current_state.total
            if counter2 <= 25:
                if difference == 0.0:
                    counter += 1
                    if counter == 3:
                        counter = 0
                        counter2 += 1
                        if counter2 <= 30:
                            current_temp = 6500
                else:
                    counter = 0 
                # print(counter)
                
                # print(counter2)

            # print(f"difference: {difference}")

            # if price stays the same for 10000 times the algoritm stops
            print(price_counter)
            if price_new_map == current_state.total:
                price_counter += 1
                if price_counter >= 10000:
                    return current_state
            else:
                price_counter = 0

            # if the new map is better then the old map then it replaces it
            if difference >= 0.0:
                current_state = deepcopy(new_map)
                
            probability = math.exp(difference/current_temp)
            random_number = random.uniform(0,1)
            if random_number < probability:
                current_state = deepcopy(new_map)
  
            current_temp = current_temp - alpha

            print(current_state.total)
        
        return current_state