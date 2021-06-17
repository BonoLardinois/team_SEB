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
        temp = 6514
        alpha = 0.1
        final_temp = 0.99

        current_temp = temp

        current_state = deepcopy(self.start_map)
        counter = 0

        while current_temp > final_temp:

            next_move = random.choice(['rotate', 'move', 'swap'])
            
            # iets doen met de huidige map
            highest_map = current_state

            # - draaien
            if next_move == 'rotate':
                rotated_map = rotate(highest_map)
                highest_map = rotated_map
            # if self.calc_price(rotated_map) > self.calc_price(highest_map):
            #     highest_map = rotated_map

            # - verplaatsen 
            # moved_map = move_house(rotated_map)
            elif next_move == 'move':
                moved_map = move_house(highest_map)
                highest_map = moved_map
            # if self.calc_price(moved_map) > self.calc_price(highest_map):
            #     highest_map = moved_map

            # - verwisselen
            elif next_move == 'swap':
                swapped_map = swap_with_random_rotation(highest_map)
                highest_map = swapped_map
            # if self.calc_price(swapped_map) > self.calc_price(highest_map):
            #     highest_map = swapped_map

            # new_map = moved_map
            new_map = highest_map

            # checken wat het vershil in totale prijs is
            price_new_map = self.calc_price(new_map)
            # print(f"current state: {current_state.total}")
            # print(f"new state: {price_new_map}")
            difference = price_new_map - current_state.total
            if difference == 0.0:
                counter += 1
                if counter == 500:
                    current_temp = 6514
                if counter == 1000:
                    current_temp = 6514
            # else:
            #     counter = 0 
            print(counter)
            

            # print(f"difference: {difference}")


            # als de nieuwe kaart beter is dan moet dit de huidige kaart vervangen
            if difference >= 0:
                current_state = deepcopy(new_map)
                
            print(f"difference: {difference}")
            # print(f"current temp: {current_temp}")
            probability = math.exp(difference/current_temp)
            random_number = random.uniform(0,1)
            # print(f"random: {random_number}")
            # print(f"prob: {probability}")
            if random_number < probability:
                # print("true")
                current_state = deepcopy(new_map)
  
            current_temp = current_temp - alpha
            # print(current_temp)
            # if current_temp < 3000 and counter == 0:
            #     current_temp = 4000
            #     counter += 1
            # if current_temp < 100 and counter == 1:
            #     current_temp = 3000
            #     counter += 1
            # # if current_temp < 100 and counter == 2:
            # #     current_temp = 2000
            print(current_temp)
            print(counter)
            print(current_state.total)
            


        
        return current_state