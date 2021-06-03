from project_code.classes.land import Land
from project_code.visualisations.visualise import visualise

if __name__ == "__main__":

    #create map
    housing_map = Land("data/wijk_1.csv")

    visualise(housing_map.houses)