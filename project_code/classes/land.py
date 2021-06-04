import csv
import random
from .water import Water
from .familyhome import Familyhome
from .bungalow import Bungalow
from .maison import Maison
from project_code.algorithms.randomise import randomise_coordinates
from shapely.geometry import Polygon

class Land():

    def __init__(self, source_file, number_houses):
        self.width = 180
        self.depth = 160
        self.all_coordinates = []
        self.waters = []
        self.water = self.load_water(source_file)
        self.houses = []
        self.load_houses(number_houses)

    def overlap(self, house):
        for coordinate in self.all_coordinates:
            print(house.bottom_left)

            new_house = Polygon([house.bottom_left, (house.bottom_left[0] + house.width, house.bottom_left[1]), house.top_right, (house.bottom_left[0], house.bottom_left[1] + house.depth)])
            existing_house = Polygon([coordinate[0], (coordinate[0][0] + house.width, coordinate[0][1]), coordinate[1], (coordinate[0][0], coordinate[0][1] + house.depth)])
            

            if new_house.intersects(existing_house) == True:
                return True

            # print((house.bottom_left[0], coordinate[0][0], house.bottom_left[1], coordinate[0][1], house.top_right[0], coordinate[1][0] + house.width, house.top_right[1], coordinate[1][1], house.depth))
            # if (house.bottom_left[0] > coordinate[0][0] and house.bottom_left[1] > coordinate[0][1] and house.top_right[0] < coordinate[1][0] + house.width and house.top_right[1] < coordinate[1][1] + house.depth):
            #     print("is overlap")
            #     return True 
      
        
        # p1 = Polygon([(0,0), (1,1), (1,0)])
        # p2 = Polygon([(0,1), (1,0), (1,1)])
        # print(p1.intersects(p2))
        self.houses.append(house)
        self.all_coordinates.append(tuple((house.bottom_left, house.top_right)))
     
        return False


    def load_water(self, source_file):
        
        with open(source_file, 'r') as in_file:
            reader = csv.reader(in_file)
            next(reader)
            
            for row in reader:
                bottom_left = row[1]
                top_right = row[2]
 
                bottom_left_tuple = tuple((int(bottom_left.split(',')[0]), int(bottom_left.split(',')[1])))
                top_right_tuple = tuple((int(top_right.split(',')[0]), int(top_right.split(',')[1])))
                
                # making water class
                water = Water(bottom_left_tuple, top_right_tuple)
                self.waters.append(water)
                self.all_coordinates.append(tuple((bottom_left_tuple, top_right_tuple)))
                
        return self.waters

    def load_houses(self, number_houses):
        
        for i in range(int(0.6 * number_houses)):
            overlap = True
            familyhome = None
            while(overlap):
                coordinates = randomise_coordinates()
                familyhome = Familyhome(coordinates)
                overlap = self.overlap(familyhome) 
                del familyhome              

            
            # self.houses.append(familyhome)
            # self.all_coordinates.append(familyhome)

        for i in range(int(0.25 * number_houses)):
            overlap = True
            bungalow = None
            while (overlap):
                coordinates = randomise_coordinates()
                bungalow = Bungalow(coordinates)
                overlap = self.overlap(bungalow)
                del bungalow

            # self.houses.append(bungalow)
            # self.all_coordinates.append(bungalow)
            
        for i in range(int(0.15 * number_houses)):
            overlap = True
            maison = None
            while (overlap):
                coordinates = randomise_coordinates()
                maison = Maison(coordinates)
                overlap = self.overlap(maison)
                del maison

            # self.houses.append(maison)
            # self.all_coordinates.append(maison)
        


