import csv

# from .water import Water

class Land():

    def __init__(self, source_file):
        self.width = 180
        self.depth = 160
        # self.get_water_coordinates(source_file)

    def load_water(self, x, y):
        pass
    
    # def get_water_coordinates(self, source_file):
    #     with open(source_file, 'r') as in_file:
    #         reader = csv.DictReader(in_file)

    #         for row in reader: 
    #             water_data = []

    #             left_bottom = row['water_data'].split(',')[1]
    #             top_right = row['water_data'].split(',')[2]
                
    #             left_bottom_tuple = tuple((left_bottom.split(',')[0], left_bottom.split(',')[1]))
    #             top_right_tuple = tuple((top_right.split(',')[0], top_right.split(',')[1]))



