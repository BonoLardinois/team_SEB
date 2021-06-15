import random
import math
from .render_randomise import Randomise
from .helpers import swap_with_random_rotation, rotate

class Simulated_annealing():

    def __init__(self, empty_graph, number_houses):
        self.start_map = Randomise(empty_graph, number_houses, 1).winner
        # self.calc_price(self.start_map)
        self.simulated_annealing(self.start_map)

    def calc_price(self, land_map):
        land_map.calculate_distance(land_map.all_land_objects)
        price = land_map.calculate_price(land_map.all_land_objects)
        print(price)
    
    def simulated_annealing(self, start_map):
        # temp bepalen aan de hand van plotje. niet nooit verslechteren. 
        # temp = 10000
        # alpha = 0.01
        # final_temp = 0.01

        # current_temp = temp

        current_state = self.start_map
        solution = current_state

        # while current_temp > final_temp:

            # iets doen met de huidige map
                # dus huisje uitzoeken en dan:
                    # - draaien
        rotated_map = rotate(current_state)
        self.calc_price(rotated_map)

        # - verplaatsen 

        # - verwisselen
        swapped_map = swap_with_random_rotation(current_state)
        self.calc_price(swapped_map)

            # checken wat het vershil in totale prijs is

            # als de nieuwe kaart beter is dan moet dit de huidige kaart vervangen
                # als dit gebeurt moet ook de current temp - alpha

            # als de nieuwe kaart niet beter is dan moet deze alsnog worden geaccepteerd maar met een probabillity??
                # nieuwe kaart 
                # # probability = 2^(- (verschil nieuwe en oude prijs)/temp)
                # if random getal(tussen 0 en 1) > probability
                #     dan wijziging terugdraaien
                #     # als dit gebeurt moet ook de current temp - alpha


