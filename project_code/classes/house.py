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