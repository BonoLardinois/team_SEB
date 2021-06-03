import csv

from .water import Water
from .familyhome import Familyhome
from .bungalow import Bungalow
from .maison import Maison

class Land():

    def __init__(self, source_file):
        self.width = 180
        self.depth = 160
        self.load_water(source_file)
        self.load_houses()
        self.houses = []
    
    def load_water(self, source_file):
        
        with open(source_file, 'r') as in_file:
            reader = csv.reader(in_file)
            next(reader)
            
            for row in reader: 
                # water_number = row['water_data'].split(',')[0]
                left_bottom = row[1]
                top_right = row[2]

                # 
                left_bottom_tuple = tuple((left_bottom.split(',')[0], left_bottom.split(',')[1]))
                top_right_tuple = tuple((top_right.split(',')[0], top_right.split(',')[1]))
                
                # making water class
                water = Water(left_bottom_tuple, top_right_tuple)
                print(water.left_bottom)
                print(water.top_right)

    def load_houses(self):

        for i in range(12):
            familyhome = Familyhome()
            self.houses.append(familyhome)

        for i in range(5):
            bungalow = Bungalow()
            self.houses.append(bungalow)
            
        for i in range(3):
            maison = Maison()
            self.houses.append(maison)
        
        print(self.houses)
        

