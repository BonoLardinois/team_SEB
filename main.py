from project_code.classes.land import Land
from project_code.visualisations.visualise import visualise
from sys import argv

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

    #create map
    housing_map = Land(f"data/{wijk_number}.csv", number_of_houses)
    visualise(housing_map.all_land_objects)

    housing_map.calculate_distance(housing_map.all_land_objects)
 
    total_value = housing_map.calculate_price(housing_map.all_land_objects)

    print(total_value)
