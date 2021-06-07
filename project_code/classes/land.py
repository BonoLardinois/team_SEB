import csv
import math
from .water import Water
from .house import House
from project_code.algorithms.randomise import randomise_coordinates
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import nearest_points



class Land():

    def __init__(self, source_file, number_houses):
        self.width = 180
        self.depth = 160
        # self.all_coordinates = []
        self.all_land_objects = []
        # self.waters = []
        self.water = self.load_water(source_file)
        # self.houses = []
        self.load_houses(number_houses)
        

    def overlap(self, house):
        new_house = house.polygon

        for land_object in self.all_land_objects:
            if land_object.polygon.intersects(new_house) == True:
                return True

        # for coordinate in self.all_coordinates:

        #     new_house = Polygon([house.bottom_left, (house.bottom_left[0] + house.width, house.bottom_left[1]), house.top_right, (house.bottom_left[0], house.bottom_left[1] + house.depth)])
        #     existing_land = Polygon([coordinate[0], (coordinate[0][0] + coordinate[1][0] - coordinate[0][0], coordinate[0][1]), coordinate[1], (coordinate[0][0], coordinate[0][1] + coordinate[1][1] - coordinate[0][1])])
            

        #     if existing_land.intersects(new_house) == True:
        #         return True
      
        # self.houses.append(house)
        self.all_land_objects.append(house)
        # self.all_coordinates.append(tuple((house.bottom_left, house.top_right)))
     
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
                # polygon = Polygon([bottom_left_tuple, (top_right_tuple[0] - bottom_left_tuple[0], bottom_left_tuple[1]), top_right_tuple, (bottom_left_tuple[0], top_right_tuple[1] - bottom_left_tuple[1])])

                polygon = Polygon([bottom_left_tuple, (top_right_tuple[0], bottom_left_tuple[1]), top_right_tuple, (bottom_left_tuple[0], top_right_tuple[1])])

                water = Water(bottom_left_tuple, top_right_tuple, polygon)

                # self.waters.append(water)
                self.all_land_objects.append(water)
                # self.all_coordinates.append(tuple((bottom_left_tuple, top_right_tuple)))

                
        return self.all_land_objects

    def load_houses(self, number_houses):

        for i in range(int(0.6 * number_houses)):
            overlap = True
            familyhome = None
            while(overlap):
                coordinates = randomise_coordinates(12, 12)
                polygon = Polygon([coordinates, (coordinates[0] + 12, coordinates[1]), (coordinates[0] + 12, coordinates[1] + 12), (coordinates[0], coordinates[1] + 12)])
                familyhome = House("familyhome", 12, 12, 285000, coordinates, polygon)
                overlap = self.overlap(familyhome)             

        for i in range(int(0.25 * number_houses)):
            overlap = True
            bungalow = None
            while (overlap):
                coordinates = randomise_coordinates(17, 13)
                polygon = Polygon([coordinates, (coordinates[0] + 17, coordinates[1]), (coordinates[0] + 17, coordinates[1] + 13), (coordinates[0], coordinates[1] + 13)])
                bungalow = House("bungalow", 17, 13, 399000, coordinates, polygon)
                overlap = self.overlap(bungalow)
            
        for i in range(int(0.15 * number_houses)):
            overlap = True
            maison = None
            while (overlap):
                coordinates = randomise_coordinates(24, 22)
                polygon = Polygon([coordinates, (coordinates[0] + 24, coordinates[1]), (coordinates[0] + 24, coordinates[1] + 22), (coordinates[0], coordinates[1] + 22)])
                maison = House("maison", 24, 22, 610000, coordinates, polygon)
                overlap = self.overlap(maison)
     
    def calculate_distance(self, houses):
        all_polygons = []

        for house in houses:
            if house.name != "water":
                all_polygons.append(house.polygon)
       
        for house in houses:    
            if house.name != "water": 
                origin = house.polygon
                all_polygons.remove(origin)
                polygons = MultiPolygon(all_polygons)
                nearest_geom = nearest_points(origin, polygons)
                x = math.floor(nearest_geom[0].distance(nearest_geom[1]))
                extra_space = math.floor(x / 2)
                house.nearest_neighbour = extra_space
                all_polygons.append(origin)
                print(x)
                print(extra_space)
        

    def calculate_price(self, houses):
        total = 0

        for house in houses:
            if house.name == "familyhome":
                house.price = 285000 + (285000 * 0.03 * house.nearest_neighbour)
                total += house.price

            elif house.name == "bungalow":
                house.price = 399000 + (399000 * 0.04 * house.nearest_neighbour)
                total += house.price

            elif house.name == "maison":
                house.price = 610000 + (610000 * 0.06 * house.nearest_neighbour)
                total += house.price
        
        return total



 

            

           
