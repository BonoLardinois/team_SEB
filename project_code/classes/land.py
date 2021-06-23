# Team SEB 
# Minor Programmeren (Programmeertheorie)  
# land.py
#
# - Renders land for land objects.
# - Checks validity of houses.
# - Calculates price of houses.
# - Calculates distance between houses.

import csv
import math
from .water import Water
from .house import House
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import nearest_points


class Land():

    def __init__(self, source_file):
        self.width = 180
        self.depth = 160
        self.all_land_objects = []
        self.total = 0
        self.total_real = 0
        self.water = []
        self.load_water(source_file)
        #self.load_houses(number_houses)
        
    def overlap(self, house):
        '''
        Function to check for overlap between land objects
        '''
        
        # checks all land objects if overlap return true
        for land_object in self.all_land_objects:
            if land_object.name != 'water':
                # with constraints
                if house.polygon_free_space.intersects(land_object.polygon) == True or land_object.polygon_free_space.intersects(house.polygon_free_space) == True:
                # without constraints
                # if house.polygon.intersects(land_object.polygon) == True:
                    return True        
            elif land_object.name == 'water':
                if land_object.polygon.intersects(house.polygon) == True:
                    return True

        # if no overlap append polygon to list
        self.all_land_objects.append(house)

        return False

    def load_water(self, source_file):
        '''
        Function to load all water objects from csv file
        '''
        with open(source_file, 'r') as in_file:
            reader = csv.reader(in_file)
            next(reader)
            
            for row in reader:
                bottom_left = row[1]
                top_right = row[2]
 
                bottom_left_tuple = tuple((int(bottom_left.split(',')[0]), int(bottom_left.split(',')[1])))
                top_right_tuple = tuple((int(top_right.split(',')[0]), int(top_right.split(',')[1])))
                
                polygon = Polygon([bottom_left_tuple, (top_right_tuple[0], bottom_left_tuple[1]), top_right_tuple, (bottom_left_tuple[0], top_right_tuple[1])])
                
                water = Water(bottom_left_tuple, top_right_tuple, polygon)

                self.all_land_objects.append(water)
                self.water.append(water)

    def check_valid(land, house):
        '''
        Function that checks land bounds/overlap, does not append houses
        '''
        if not house.check_bounds(land.width, land.depth):
            return False
        # checks all land objects if overlap return true
        for land_object in land.all_land_objects:
            if land_object.name != 'water':
                if house.polygon_free_space.intersects(land_object.polygon) == True or land_object.polygon_free_space.intersects(house.polygon_free_space) == True:
                    return False     
            elif land_object.name == 'water':
                if land_object.polygon.intersects(house.polygon) == True or house.polygon.intersects(land_object.polygon) == True:
                    return False
        return True
         
    def calculate_distance(self, houses):
        '''
        Calculate distance to closest house
        '''
        all_polygons = []

        for house in houses:
            if house.name != "water":
                all_polygons.append(house.polygon)
       
        for house in houses:    
            if house.name != "water": 
                origin = house.polygon
                all_polygons.remove(house.polygon)
                polygons = MultiPolygon(all_polygons)
                nearest_geom = nearest_points(origin, polygons)
                # extra_space = math.floor(nearest_geom[0].distance(nearest_geom[1]))
                extra_space = nearest_geom[0].distance(nearest_geom[1])
                house.nearest_neighbour = extra_space
                all_polygons.append(house.polygon)  
                house.fine = extra_space - house.free_space   
                if house.fine > 0:
                    house.fine = 0   

    def calculate_price(self, houses):
        '''
        Calculate price of house and total price of land (not rounded)
        '''
        self.total = 0
        for house in houses:
            
            if house.name == "familyhome":
                house.price = 285000 + (285000 * 0.03 * house.nearest_neighbour) + (house.fine * 100000)
                self.total += house.price

            elif house.name == "bungalow":                
                house.price = 399000 + (399000 * 0.04 * house.nearest_neighbour) + (house.fine * 100000)
                self.total += house.price

            elif house.name == "maison":                
                house.price = 610000 + (610000 * 0.06 * house.nearest_neighbour) + (house.fine * 100000)
                self.total += house.price
        return self.total

    def calculate_price_real(self, houses):
        '''
        Calculate price of house and total price of land (rounded)
        '''

        for house in houses:
            if house.name == "familyhome":
                house.price = 285000 + (285000 * 0.03 * math.floor(house.nearest_neighbour)) + (house.fine * 100000)
                self.total_real += house.price

            elif house.name == "bungalow":
                house.price = 399000 + (399000 * 0.04 * math.floor(house.nearest_neighbour)) + (house.fine * 100000)
                self.total_real += house.price

            elif house.name == "maison":
                house.price = 610000 + (610000 * 0.06 * math.floor(house.nearest_neighbour)) + (house.fine * 100000)
                self.total_real += house.price
        
        return self.total_real



 

            

           
