class House():

    def __init__(self, type_house, width, depth, price, coordinates, polygon):
        self.name = type_house
        self.width = width
        self.depth = depth
        self.price = price
        self.bottom_left = coordinates
        self.top_right = tuple((self.bottom_left[0] + self.width, self.bottom_left[1] + self.depth))
        self.polygon = polygon
        self.nearest_neighbour = None

    def __str__(self):
        return (f"name:{self.name}, left_bottom: {self.bottom_left}, top_right: {self.top_right}")