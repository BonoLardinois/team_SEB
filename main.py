from project_code.classes.land import Land
from project_code.visualisations.visualise import visualise
from sys import argv
from project_code.algorithms.render_randomise import Randomise
import cProfile
import csv

if __name__ == "__main__":

    # Check command line arguments
    if len(argv) not in [3]:
        print("Usage: python3 main.py [type of wijk: wijk_1, wijk_2 or wijk_3] [number of houses: 20, 40 or 60]")
        exit(1)

    # Load the requested wijk or else wijk_1 (20 houses)
    print("Loading...")
    
    wijk_number = argv[1]
    number_of_houses = int(argv[2])
    
    if number_of_houses not in [20, 40, 60] or wijk_number not in ["wijk_1", "wijk_2", "wijk_3"]:
        print("Usage: python3 main.py [type of wijk: wijk_1, wijk_2 or wijk_3] [number of houses: 20, 40 or 60]")
        exit(1)
    
    
    # --------------------------- Random  --------------------------
    empty_graph = Land(f"data/{wijk_number}.csv")
    winner_graph = Randomise(empty_graph, number_of_houses, 1000)
    visualise(winner_graph.winner.all_land_objects, winner_graph.winner.total)



    # ---------------------------------------------------------------

    """ housing_map = Land(f"data/{wijk_number}.csv", number_of_houses)
    housing_map.calculate_distance(housing_map.all_land_objects)
    total_value = housing_map.calculate_price(housing_map.all_land_objects)
    visualise(housing_map.all_land_objects, total_value)
    print(total_value) """

    with open("output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["structure","corner_1","corner_2","corner_3","corner_4","type"])
        writer.writerow(["water_1","0,0","180,0","180,32","0,32","WATER"])
        
        counter_f = 0
        counter_b = 0
        counter_m = 0

        for house in winner_graph.winner.all_land_objects:
            
            if house.name == "familyhome":
                counter_f += 1
                writer.writerow([f"eengezinswoning_{counter_f}",f"{house.bottom_left[0]},{house.bottom_left[1]}",f"{house.bottom_left[0] + 8},{house.bottom_left[1]}",f"{house.top_right[0]},{house.top_right[1]}",f"{house.top_right[0] - 8},{house.top_right[1]}","EENGEZINSWONING"])
                
            
            if house.name == "bungalow":
                counter_b += 1
                writer.writerow([f"bungalow_{counter_b}",f"{house.bottom_left[0]},{house.bottom_left[1]}",f"{house.bottom_left[0] + 11},{house.bottom_left[1]}",f"{house.top_right[0]},{house.top_right[1]}",f"{house.top_right[0] - 11},{house.top_right[1]}","BUNGALOW"])

           
            if house.name == "maison":
                counter_m += 1
                writer.writerow([f"maison_{counter_m}",f"{house.bottom_left[0]},{house.bottom_left[1]}",f"{house.bottom_left[0] + 12},{house.bottom_left[1]}",f"{house.top_right[0]},{house.top_right[1]}",f"{house.top_right[0] - 12},{house.top_right[1]}","MAISON"])

        integer_answer = int(winner_graph.winner.total)
        writer.writerow(["networth",f"{integer_answer}"])


