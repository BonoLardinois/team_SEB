from project_code.classes.land import Land
from project_code.classes.house import House
from copy import deepcopy
from shapely.geometry import Polygon
from project_code.visualisations.visualise import visualise
import matplotlib.pyplot as plt

class HillClimber():

    def __init__(self, housing_map):
        self.winner = self.run(housing_map)

    def valid_move(self, house, waters):

        # checks if house intersects with water
        for water in waters:
            if water.polygon.intersects(house.polygon):
                return False

        # if house.bottom_left[0] - house.free_space < 0 or house.bottom_left[0] + house.free_space > 180:
        #     return False
        # if house.bottom_left[1] - house.free_space < 0 or house.bottom_left[1] + house.free_space > 160:
        #     return False
        # if house.top_right[0] - house.free_space < 0 or house.top_right[0] + house.free_space > 180: 
        #     return False
        # if house.top_right[1] - house.free_space < 0 or house.top_right[1] + house.free_space > 160:
        #     return False
        # return True


        if house.bottom_left[0] < house.free_space or house.bottom_left[0] > 180 - house.width_with_freespace or house.bottom_left[1] < house.free_space or house.bottom_left[1] > 160 - house.depth_with_freespace or house.top_right[0] < house.width_with_freespace or house.top_right[0] > 180 - house.free_space or house.top_right[1] < house.depth_with_freespace or house.top_right[1] > 160 - house.free_space:
            return False
    
        return True

    def run(self, housing_map):
        print("housing map value:")
        print(housing_map.total)
        copy_map = deepcopy(housing_map)
        generations = []
        generations.append("copy_map")
        current_best_value = copy_map.total
        counter = 0
        # steps = 8
        iterations = 30

        # data for iteration graph
        iteration_counter = 0
        results = []
        total_iterations = []
        # steps = 2
        for i in range(iterations):

            if i < 7:
                steps = 8 
            if i >= 7 and i < 13:
                steps = 4
            if i >= 13 and i < 20:
                steps = 2
            if i >= 20:
                steps = 1

            for house in copy_map.all_land_objects:
                copy_map.total = 0
                if house.name != "water":
                    # print("for loop values:")

                    # moves house to the right
                    total_value_right = 0
                    house.move(steps, 0)

                    # checks for overlap
                    if self.valid_move(house, housing_map.water):
                        copy_map.calculate_distance(copy_map.all_land_objects)
                        total_value_right = copy_map.calculate_price(copy_map.all_land_objects)
                        # copy_map_right = deepcopy(copy_map)
                    house.move(-steps, 0)
                    copy_map.total = 0

                    if total_value_right > current_best_value:
                        generations.pop(0)
                        # generations.append(copy_map_right)
                        generations.append("right")
                        current_best_value = total_value_right

                    # moves house to the left
                    total_value_left = 0
                    house.move(-steps, 0)

                    # checks for overlap
                    if self.valid_move(house, housing_map.water):
                        copy_map.calculate_distance(copy_map.all_land_objects)
                        total_value_left = copy_map.calculate_price(copy_map.all_land_objects)
                        # copy_map_left = deepcopy(copy_map)
                    house.move(steps, 0)
                    copy_map.total = 0

                    if total_value_left > current_best_value:
                        generations.pop(0)
                        # generations.append(copy_map_left)  
                        generations.append("left")   
                        current_best_value = total_value_left            

                    # moves house up
                    total_value_up = 0
                    house.move(0, steps)
                    
                    # checks for overlap
                    if self.valid_move(house, housing_map.water):
                        copy_map.calculate_distance(copy_map.all_land_objects)
                        total_value_up = copy_map.calculate_price(copy_map.all_land_objects)
                        # copy_map_up = deepcopy(copy_map)
                    house.move(0, -steps)
                    copy_map.total = 0

                    if total_value_up > current_best_value:
                        generations.pop(0)
                        # generations.append(copy_map_up)
                        generations.append("up")
                        current_best_value = total_value_up

                    # moves house down
                    total_value_down = 0
                    house.move(0, -steps)
                    
                    # checks for overlap
                    if self.valid_move(house, housing_map.water):
                        copy_map.calculate_distance(copy_map.all_land_objects)
                        total_value_down = copy_map.calculate_price(copy_map.all_land_objects)
                        # copy_map_down = deepcopy(copy_map)
                    house.move(0, steps)
                    copy_map.total = 0

                    if total_value_down > current_best_value:
                        generations.pop(0)
                        # generations.append(copy_map_down)   
                        generations.append("down")
                        current_best_value = total_value_down
                    
                    if generations[0] == "right":
                        house.move(steps, 0)
                        # copy_map = deepcopy(copy_map)

                    elif generations[0] == "left":
                        house.move(-steps, 0)
                        # copy_map = deepcopy(copy_map)

                    elif generations[0] == "up":
                        house.move(0, steps)
                        # copy_map = deepcopy(copy_map)

                    elif generations[0] == "down":
                        house.move(0, -steps)
                        # copy_map = deepcopy(copy_map)
                    
                    generations = ["copy_map"]
                    # else:
                    #     house.move(0, 0)
                        # copy_map = deepcopy(copy_map)

                    # copy_map = deepcopy(generations[0])   
                    # print("one for loop done")
                    # copy_map = deepcopy(copy_map)
            counter += 1

            # data for iteration graph
            iteration_counter += 1
            total_iterations.append(iteration_counter)
            results.append(current_best_value)

            print(counter)

        # calculates value for return object
        copy_map.calculate_distance(copy_map.all_land_objects)
        total_value_up = copy_map.calculate_price(copy_map.all_land_objects)
        copy_map.calculate_price_real(copy_map.all_land_objects)
        
        print(f"total: {copy_map.total}")
        print(f"total_real: {copy_map.total_real}")
        
        # print(total_iterations)
        # print(results)
        
        plt.plot(total_iterations, results)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis') 
        plt.title('Iteration graph')
        plt.savefig('output/iteration_graph.png')

        return copy_map
        # visualise(copy_map.all_land_objects, copy_map.total)

    

    