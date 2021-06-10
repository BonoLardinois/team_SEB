from project_code.classes.land import Land
from project_code.classes.house import House
from copy import deepcopy
from shapely.geometry import Polygon
from project_code.visualisations.visualise import visualise

class HillClimber():

    def __init__(self, housing_map):
        self.winner = self.run(housing_map)

    def run(self, housing_map):
        print("test")
        print(housing_map.total)
        copy_map = deepcopy(housing_map)
        copy_map.total = 0
        for house in copy_map.all_land_objects:
            if house.name != "water":
                house.move(1, 0)
                copy_map.calculate_distance(copy_map.all_land_objects)
                total_value = copy_map.calculate_price(copy_map.all_land_objects)
                print("test2")
                print(total_value)
                break
                visualise(copy_map.all_land_objects, copy_map.total)


    