from project_code.classes.land import Land
from project_code.classes.house import House
from copy import deepcopy
from shapely.geometry import Polygon
from project_code.visualisations.visualise import visualise

class HillClimber():

    def __init__(self, housing_map):
        self.winner = self.run(housing_map)

    def run(self, housing_map):
        print("housing map value:")
        print(housing_map.total)
        copy_map = deepcopy(housing_map)
        generations = []
        generations.append(copy_map)
        for i in range(3):
            for house in copy_map.all_land_objects:
                copy_map.total = 0
                if house.name != "water":
                    # print("for loop values:")

                    # moves house to the right
                    house.move(1, 0)
                    copy_map.calculate_distance(copy_map.all_land_objects)
                    total_value_right = copy_map.calculate_price(copy_map.all_land_objects)
                    copy_map_right = deepcopy(copy_map)
                    house.move(-1, 0)
                    copy_map.total = 0

                    if total_value_right > generations[0].total:
                        generations.pop(0)
                        generations.append(copy_map_right)

                    # moves house to the left
                    house.move(-1, 0)
                    copy_map.calculate_distance(copy_map.all_land_objects)
                    total_value_left = copy_map.calculate_price(copy_map.all_land_objects)
                    copy_map_left = deepcopy(copy_map)
                    house.move(-1, 0)
                    copy_map.total = 0

                    if total_value_left > generations[0].total:
                        generations.pop(0)
                        generations.append(copy_map_left)                

                    # moves house up
                    house.move(0, 1)
                    copy_map.calculate_distance(copy_map.all_land_objects)
                    total_value_up = copy_map.calculate_price(copy_map.all_land_objects)
                    copy_map_up = deepcopy(copy_map)
                    house.move(0, -1)
                    copy_map.total = 0

                    if total_value_up > generations[0].total:
                        generations.pop(0)
                        generations.append(copy_map_up)

                    # moves house down
                    house.move(0, -1)
                    copy_map.calculate_distance(copy_map.all_land_objects)
                    total_value_down = copy_map.calculate_price(copy_map.all_land_objects)
                    copy_map_down = deepcopy(copy_map)
                    house.move(0, 1)
                    copy_map.total = 0

                    if total_value_down > generations[0].total:
                        generations.pop(0)
                        generations.append(copy_map_down)   

                    copy_map = deepcopy(generations[0])   
                    # print("one for loop done")

        print(f"copy map: {copy_map.total}")
        print(f"copy map: {generations[0].total}")
            
        # visualise(copy_map.all_land_objects, copy_map.total)


    