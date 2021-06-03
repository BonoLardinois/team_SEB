import csv

from .water import Water

class Land():

    def __init__(self, source_file):
        self.width = 180
        self.depth = 160
        self.load_water(source_file)
    
    def load_water(self, source_file):
        
        with open(source_file, 'r') as in_file:
            reader = csv.reader(in_file)
            next(reader)
            
            for row in reader: 
                # water_number = row['water_data'].split(',')[0]
                left_bottom = row[1]
                top_right = row[2]
            
                left_bottom_tuple = tuple((left_bottom.split(',')[0], left_bottom.split(',')[1]))
                top_right_tuple = tuple((top_right.split(',')[0], top_right.split(',')[1]))

                print(left_bottom_tuple)
                print(top_right_tuple)
                
                # making water class
                water = Water(left_bottom_tuple, top_right_tuple)
                print(water.left_bottom)
                print(water.top_right)



