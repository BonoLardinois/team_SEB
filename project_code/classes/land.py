import csv
import random
from .water import Water
from .familyhome import Familyhome
from .bungalow import Bungalow
from .maison import Maison
from project_code.algorithms.randomise import randomise_coordinates

class Land():

    def __init__(self, source_file):
        self.width = 180
        self.depth = 160
        self.water = self.load_water(source_file)
        self.houses = []
        self.load_houses()
    
    def load_water(self, source_file):
        
        with open(source_file, 'r') as in_file:
            reader = csv.reader(in_file)
            next(reader)
            
            for row in reader: 
                # water_number = row['water_data'].split(',')[0]
                left_bottom = row[1]
                top_right = row[2]

                # 
                left_bottom_tuple = tuple((int(left_bottom.split(',')[0]), int(left_bottom.split(',')[1])))
                top_right_tuple = tuple((int(top_right.split(',')[0]), int(top_right.split(',')[1])))
                
                # making water class
                water = Water(left_bottom_tuple, top_right_tuple)
                print(water.left_bottom)
                print(water.top_right)

    def load_houses(self):

        for i in range(12):
            coordinates = randomise_coordinates()
            familyhome = Familyhome(coordinates)
            # print(familyhome.bottom_left)
            self.houses.append(familyhome)

        for i in range(5):
            coordinates = randomise_coordinates()
            bungalow = Bungalow(coordinates)
            # print(bungalow.bottom_left)
            self.houses.append(bungalow)
            
        for i in range(3):
            coordinates = randomise_coordinates()
            maison = Maison(coordinates)
            # print(maison.bottom_left)
            self.houses.append(maison)
        


