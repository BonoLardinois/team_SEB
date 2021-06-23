# Team SEB 
# Minor Programmeren (Programmeertheorie)  
# house.py
#
# - House class.

from shapely.geometry import Polygon


class House():

    def __init__(self, type_house, width, depth, price, coordinates_no_free_space, polygon, free_space, polygon_free_space):
        self.name = type_house
        self.width = width
        self.depth = depth
        self.price = price
        self.bottom_left = coordinates_no_free_space
        self.top_right = tuple((self.bottom_left[0] + self.width, self.bottom_left[1] + self.depth))
        self.polygon = polygon
        self.nearest_neighbour = None
        self.free_space = free_space
        self.width_with_freespace = self.width + (self.free_space * 2)
        self.depth_with_freespace = self.depth + (self.free_space * 2)
        self.polygon_free_space = polygon_free_space
        self.placement = None
        self.fine = 12



    def __str__(self):
        return (f"name:{self.name}, left_bottom: {self.bottom_left}, top_right: {self.top_right}")

    def move(self, change_x, change_y):

        # moves house to the right
        self.bottom_left = tuple((self.bottom_left[0] + change_x, self.bottom_left[1] + change_y))
        self.top_right = tuple((self.top_right[0] + change_x, self.top_right[1] + change_y))

        # update the polygons
        self.polygon = Polygon([(self.bottom_left[0], self.bottom_left[1]), (self.bottom_left[0] + self.width, self.bottom_left[1]), (self.bottom_left[0] + self.width, self.bottom_left[1] + self.depth), (self.bottom_left[0], self.bottom_left[1] + self.depth)])
        self.polygon_free_space = Polygon([(self.bottom_left[0] - self.free_space, self.bottom_left[1] - self.free_space), (self.bottom_left[0] + self.width_with_freespace - self.free_space, self.bottom_left[1] - self.free_space), (self.bottom_left[0] + self.width_with_freespace - self.free_space, self.bottom_left[1] + self.depth_with_freespace - self.free_space), (self.bottom_left[0] - self.free_space, self.bottom_left[1] + self.depth_with_freespace - self.free_space)])
        
    def check_bounds(self, width, depth):
        if self.bottom_left[0] - self.free_space < 0 or self.bottom_left[0] + self.free_space > width:
            return False
        if self.bottom_left[1] - self.free_space < 0 or self.bottom_left[1] + self.free_space > depth:
            return False
        if self.top_right[0] - self.free_space < 0 or self.top_right[0] + self.free_space > width: 
            return False
        if self.top_right[1] - self.free_space < 0 or self.top_right[1] + self.free_space > depth:
            return False
        return True
       
