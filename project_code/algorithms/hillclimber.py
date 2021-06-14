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
        generations.append("copy_map")
        current_best_value = copy_map.total
        counter = 0
        for i in range(400):
            for house in copy_map.all_land_objects:
                copy_map.total = 0
                if house.name != "water":
                    # print("for loop values:")

                    # moves house to the right
                    total_value_right = 0
                    if house.move(1, 0):
                        copy_map.calculate_distance(copy_map.all_land_objects)
                        total_value_right = copy_map.calculate_price(copy_map.all_land_objects)
                        # copy_map_right = deepcopy(copy_map)
                    house.move(-1, 0)
                    copy_map.total = 0

                    if total_value_right > current_best_value:
                        generations.pop(0)
                        # generations.append(copy_map_right)
                        generations.append("right")
                        current_best_value = total_value_right

                    # moves house to the left
                    total_value_left = 0
                    if house.move(-1, 0):
                        copy_map.calculate_distance(copy_map.all_land_objects)
                        total_value_left = copy_map.calculate_price(copy_map.all_land_objects)
                        # copy_map_left = deepcopy(copy_map)
                    house.move(1, 0)
                    copy_map.total = 0

                    if total_value_left > current_best_value:
                        generations.pop(0)
                        # generations.append(copy_map_left)  
                        generations.append("left")   
                        current_best_value = total_value_left            

                    # moves house up
                    total_value_up = 0
                    if house.move(0, 1):
                        copy_map.calculate_distance(copy_map.all_land_objects)
                        total_value_up = copy_map.calculate_price(copy_map.all_land_objects)
                        # copy_map_up = deepcopy(copy_map)
                    house.move(0, -1)
                    copy_map.total = 0

                    if total_value_up > current_best_value:
                        generations.pop(0)
                        # generations.append(copy_map_up)
                        generations.append("up")
                        current_best_value = total_value_up

                    # moves house down
                    total_value_down = 0
                    if house.move(0, -1):
                        copy_map.calculate_distance(copy_map.all_land_objects)
                        total_value_down = copy_map.calculate_price(copy_map.all_land_objects)
                        # copy_map_down = deepcopy(copy_map)
                    house.move(0, 1)
                    copy_map.total = 0

                    if total_value_down > current_best_value:
                        generations.pop(0)
                        # generations.append(copy_map_down)   
                        generations.append("down")
                        current_best_value = total_value_down
                    
                    if generations[0] == "right":
                        house.move(1, 0)
                        # copy_map = deepcopy(copy_map)

                    elif generations[0] == "left":
                        house.move(-1, 0)
                        # copy_map = deepcopy(copy_map)

                    elif generations[0] == "up":
                        house.move(0, 1)
                        # copy_map = deepcopy(copy_map)

                    elif generations[0] == "down":
                        house.move(0, -1)
                        # copy_map = deepcopy(copy_map)
                    
                    generations = ["copy_map"]
                    # else:
                    #     house.move(0, 0)
                        # copy_map = deepcopy(copy_map)

                    # copy_map = deepcopy(generations[0])   
                    # print("one for loop done")
                    # copy_map = deepcopy(copy_map)
            counter += 1
            print(counter)

        # calculates value for return object
        copy_map.calculate_distance(copy_map.all_land_objects)
        total_value_up = copy_map.calculate_price(copy_map.all_land_objects)

        print(f"copy map: {copy_map.total}")
        print(f"copy map: {generations[0]}")

        return copy_map
        # visualise(copy_map.all_land_objects, copy_map.total)


    