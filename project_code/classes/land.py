import csv
import math
from .water import Water
from .house import House
from shapely.geometry import Polygon, MultiPolygon, mapping
from shapely.ops import nearest_points



class Land():

    def __init__(self, source_file):
        self.width = 180
        self.depth = 160
        self.all_land_objects = []
        self.total = 0
        self.water = []
        self.load_water(source_file)
        #self.load_houses(number_houses)
        
    def overlap(self, house):
        '''
        function to check for overlap
        '''
        
        # checks all land objects if overlap return true
        for land_object in self.all_land_objects:
            if land_object.name != 'water':
                if house.polygon_free_space.intersects(land_object.polygon) == True or land_object.polygon_free_space.intersects(house.polygon_free_space) == True:
                    return True        
            elif land_object.name == 'water':
                if land_object.polygon.intersects(house.polygon) == True:
                    return True

        # if no overlap append polygon to list
        self.all_land_objects.append(house)

        return False

    def load_water(self, source_file):
        '''
        function to load all water objects from csv file
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
                origin = house.polygon #_free_space
                all_polygons.remove(house.polygon)
                polygons = MultiPolygon(all_polygons)
                nearest_geom = nearest_points(origin, polygons)
                extra_space = math.floor(nearest_geom[0].distance(nearest_geom[1]))
                house.nearest_neighbour = extra_space
                all_polygons.append(house.polygon)        

    def calculate_price(self, houses):
        '''
        Calculate price of house and total price of land
        '''

        for house in houses:
            if house.name == "familyhome":
                house.price = 285000 + (285000 * 0.03 * house.nearest_neighbour)
                self.total += house.price

            elif house.name == "bungalow":
                house.price = 399000 + (399000 * 0.04 * house.nearest_neighbour)
                self.total += house.price

            elif house.name == "maison":
                house.price = 610000 + (610000 * 0.06 * house.nearest_neighbour)
                self.total += house.price
        
        return self.total



 

            

           
