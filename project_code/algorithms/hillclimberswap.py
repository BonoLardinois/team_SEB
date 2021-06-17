from .render_randomise import Randomise
import random
from copy import deepcopy
from project_code.algorithms.rotation import rotation
from project_code.classes.house import House
from shapely.geometry import Polygon
from .helpers import swap_with_random_rotation, rotate

class Hillclimber():

    def __init__(self, graph, iterations):
        self.winner = self.run(graph, iterations)

    def random_choice(self, choices):
        return (random.choice(choices))

    def run(self, graph, iterations):

        for n in range(iterations):
            copy_graph = deepcopy(graph)

            swapped_map = swap_with_random_rotation(copy_graph)
            
            swapped_map.calculate_distance(swapped_map.all_land_objects)
            value_swapped_map = (swapped_map.calculate_price(swapped_map.all_land_objects))
            
            if value_swapped_map > graph.total :
                graph = swapped_map
            
            
        print(f"Total number land objects placed: {len(graph.all_land_objects)}")
        return graph