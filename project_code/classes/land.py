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
        self.total = 0
        
        self.water = self.load_water(source_file)
        self.load_houses(number_houses)
        
    def overlap(self, house):
        '''
        function to check for overlap
        '''
        
        # checks all landobjects if overlap return true
        for land_object in self.all_land_objects:
            if land_object.name != 'water':
                if house.polygon_free_space.intersects(land_object.polygon) == True or land_object.polygon_free_space.intersects(house.polygon_free_space) == True:
                    return True        
            if land_object.name == 'water':
                if land_object.polygon.intersects(house.polygon) == True:
                    return True

                

        # if no overlap append polygon to list
        self.all_land_objects.append(house)
        #self.all_polygons.append(house.polygon)

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
                #self.all_polygons.append(water.polygon)
         
        return self.all_land_objects

    def load_houses(self, number_houses):
        '''
        function to load all houses in a specific neighbourhood
        '''
        for i in range(int(0.15 * number_houses)):
            width = 12
            depth = 10
            width2 = 24
            depth2 = 22
            required_free_space = 6
            overlap = True
            maison = None
            while (overlap):
                coordinates = randomise_coordinates(width2, depth2)
                polygon = Polygon([(coordinates[0] + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + depth + required_free_space), (coordinates[0] + required_free_space, coordinates[1] + depth + required_free_space)])
                
                # polygon met verplichte vrij ruimte aangemaakt voor berekening van prijs
                polygon_free_space = Polygon([coordinates, (coordinates[0] + width2, coordinates[1]), (coordinates[0] + width2, coordinates[1] + depth2), (coordinates[0], coordinates[1] + depth2)])
                coordinates2 = tuple((coordinates[0] + required_free_space, coordinates[1] + required_free_space))
                maison = House("maison", width, depth, 610000, coordinates2, polygon, 6, polygon_free_space)
                overlap = self.overlap(maison)  

        for i in range(int(0.25 * number_houses)):
            width = 11
            depth = 7
            width2 = 17
            depth2 = 19
            required_free_space = 3
            overlap = True
            bungalow = None
            while (overlap):
                coordinates = randomise_coordinates(width2, depth2)
                polygon = Polygon([(coordinates[0] + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + depth + required_free_space), (coordinates[0] + required_free_space, coordinates[1] + depth + required_free_space)])

                # polygon met verplichte vrij ruimte aangemaakt voor berekening van prijs
                polygon_free_space = Polygon([coordinates, (coordinates[0] + width2, coordinates[1]), (coordinates[0] + width2, coordinates[1] + depth2), (coordinates[0], coordinates[1] + depth2)])
                coordinates2 = tuple((coordinates[0] + required_free_space, coordinates[1] + required_free_space))
                bungalow = House("bungalow", width, depth, 399000, coordinates2, polygon, 3, polygon_free_space)
                overlap = self.overlap(bungalow)

        for i in range(int(0.6 * number_houses)):
            width = 8
            depth = 8
            width2 = 12
            depth2 = 12
            required_free_space = 2
            overlap = True
            familyhome = None
            while(overlap):
                coordinates = randomise_coordinates(width2, depth2)
                polygon = Polygon([(coordinates[0] + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + required_free_space), (coordinates[0] + width + required_free_space, coordinates[1] + depth + required_free_space), (coordinates[0] + required_free_space, coordinates[1] + depth + required_free_space)])

                # polygon met verplichte vrij ruimte aangemaakt voor berekening van prijs
                polygon_free_space = Polygon([coordinates, (coordinates[0] + width2, coordinates[1]), (coordinates[0] + width2, coordinates[1] + depth2), (coordinates[0], coordinates[1] + depth2)])
                coordinates2 = tuple((coordinates[0] + required_free_space, coordinates[1] + required_free_space))
                familyhome = House("familyhome", width, depth, 285000, coordinates2, polygon, 2, polygon_free_space)
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
                origin = house.polygon_free_space
                # eigen polygon even uit huisverwijderen 
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



 

            

           
