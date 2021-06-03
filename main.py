from project_code.classes.land import Land

if __name__ == "__main__":

    #create map
    housing_map = Land("data/wijk_1.csv")
    print(housing_map.width)