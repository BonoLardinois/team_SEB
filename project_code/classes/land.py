import csv
import math
from .water import Water
from .house import House
from project_code.algorithms.randomise import randomise_coordinates
from shapely.geometry import Polygon, MultiPolygon, mapping
from shapely.ops import nearest_points



class Land():

    def __init__(self, source_file, number_houses):
        self.width = 180
        self.depth = 160
        self.all_polygons = []
        self.all_land_objects = []
        # self.available_coordinates = []
        self.total = 0

        # for x in range(180+1):
        #     for y in range(160+1):
        #         coordinate = tuple((x,y))
        #         self.available_coordinates.append(coordinate)
        
        self.water = self.load_water(source_file)
        self.load_houses(number_houses, )
        
    # def remove_used_point(self, land_object):
        
        # for x in range(land_object.bottom_left[0], land_object.top_right[0]+1):
        #     for y in range(land_object.bottom_left[1], land_object.top_right[1]+1):
        #         coordinate = tuple((x, y))
        #         #print(coordinate)
        #         self.available_coordinates.remove(coordinate)
        # #print(len(self.available_coordinates))

    def overlap(self, house):
        '''
        function to check for overlap
        '''
        new_house = house.polygon
        
        # checks all landobjects if overlap return true
        for land_object in self.all_land_objects:
            if land_object.polygon.intersects(new_house) == True:
                # del house
                return True
        
            if land_object.name != 'water':
                origin = house.polygon
                polygons = MultiPolygon(self.all_polygons)
                nearest_geom = nearest_points(origin, polygons)
                x = math.floor(nearest_geom[0].distance(nearest_geom[1]))
                extra_space = math.floor(x)
                if extra_space < land_object.free_space:
                    #print(f"extra space: {extra_space}")
                    #print (f'fout {land_object.name}')
                    return True
                

        # if no overlap append polygon to list
        self.all_land_objects.append(house)
        self.all_polygons.append(house.polygon)

        return False
    
    def check_free_space(self):
        pass


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
                self.all_polygons.append(water.polygon)
         
        return self.all_land_objects

    def load_houses(self, number_houses):
        '''
        function to load all houses in a specific neighbourhood
        '''

        for i in range(int(0.15 * number_houses)):
            width = 12
            depth = 10
            overlap = True
            maison = None
            while (overlap):
                coordinates = randomise_coordinates(width, depth)
                polygon = Polygon([coordinates, (coordinates[0] + width, coordinates[1]), (coordinates[0] + width, coordinates[1] + depth), (coordinates[0], coordinates[1] + depth)])
                maison = House("maison", width, depth, 610000, coordinates, polygon, 6)
                overlap = self.overlap(maison)         

        for i in range(int(0.25 * number_houses)):
            width = 11
            depth = 7
            overlap = True
            bungalow = None
            while (overlap):
                coordinates = randomise_coordinates(width, depth)
                polygon = Polygon([coordinates, (coordinates[0] + width, coordinates[1]), (coordinates[0] + width, coordinates[1] + depth), (coordinates[0], coordinates[1] + depth)])
                bungalow = House("bungalow", width, depth, 399000, coordinates, polygon, 3)
                overlap = self.overlap(bungalow)

        for i in range(int(0.6 * number_houses)):
            width = 8
            depth = 8
            overlap = True
            familyhome = None
            while(overlap):
                coordinates = randomise_coordinates(width, depth)
                polygon = Polygon([coordinates, (coordinates[0] + width, coordinates[1]), (coordinates[0] + width, coordinates[1] + depth), (coordinates[0], coordinates[1] + depth)])
                familyhome = House("familyhome", width, depth, 285000, coordinates, polygon, 2)
                overlap = self.overlap(familyhome)
            
     
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
                all_polygons.remove(origin)
                polygons = MultiPolygon(all_polygons)
                nearest_geom = nearest_points(origin, polygons)
                x = math.floor(nearest_geom[0].distance(nearest_geom[1]))
                extra_space = math.floor(x) # /2 weghalen
                house.nearest_neighbour = extra_space
                all_polygons.append(origin)        

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



 

            

           
