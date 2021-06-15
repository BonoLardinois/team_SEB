import random
import math
from .render_randomise import Randomise
from .helpers import swap_with_random_rotation, rotate

class Simulated_annealing():

    def __init__(self, empty_graph, number_houses):
        self.start_map = Randomise(empty_graph, number_houses, 400).winner
        self.calc_price(self.start_map)
        self.simulated_annealing(self.start_map)
        self.end_result = None

    def calc_price(self, land_map):
        land_map.calculate_distance(land_map.all_land_objects)
        price = land_map.calculate_price(land_map.all_land_objects)
        # print(price)
        return price
    
    def simulated_annealing(self, start_map):
        # temp bepalen aan de hand van plotje. niet nooit verslechteren. 
        temp = 10100
        alpha = 0.1
        final_temp = 10000

        current_temp = temp

        current_state = self.start_map

        while current_temp > final_temp:

                # iets doen met de huidige map
                    # dus huisje uitzoeken en dan:
            # - draaien
            rotated_map = rotate(current_state)
            self.calc_price(rotated_map)

            # - verplaatsen 

            # - verwisselen
            swapped_map = swap_with_random_rotation(rotated_map)
            self.calc_price(swapped_map)

            new_map = swapped_map

            # checken wat het vershil in totale prijs is
            price_new_map = self.calc_price(new_map)
            difference = price_new_map - current_state.total
            # print(difference)

            # als de nieuwe kaart beter is dan moet dit de huidige kaart vervangen
            if difference > 0:
                current_state = new_map
                # als dit gebeurt moet ook de current temp - alpha
                current_temp = current_temp - alpha
                
            # als de nieuwe kaart niet beter is dan moet deze alsnog worden geaccepteerd maar met een probabillity??
            if difference < 0:
                probability = math.exp((-(difference))/current_temp)
                random_number = random.uniform(0,1)
                if random_number > probability:
                    current_state = new_map
                    current_temp = current_temp - alpha
                current_temp = current_temp - alpha    
            # print(current_temp)
            # print(current_state.total)

        print(current_state.total)
        self.end_result = current_state

                # nieuwe kaart 
                # # probability = 2^(- (verschil nieuwe en oude prijs)/temp)
                # if random getal(tussen 0 en 1) > probability
                #     dan wijziging terugdraaien
                #     # als dit gebeurt moet ook de current temp - alpha


