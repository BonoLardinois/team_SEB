class Bungalow():

    def __init__(self, coordinates):
        self.name = "bungalow"
        self.width = 17
        self.depth = 13
        self.price = 399000
        self.bottom_left = coordinates

    def get_price(self):
        pass

    def __str__(self):
        return 'bungalow'