class Bungalow():

    def __init__(self, coordinates):
        self.name = "bungalow"
        self.width = 17
        self.depth = 13
        self.price = 399000
        self.bottom_left = coordinates
        self.top_right = tuple((self.bottom_left[0] + self.width, self.bottom_left[1] + self.depth))
        # print(f" bungalow {self.bottom_left} {self.top_right}")
        
    def get_price(self):
        pass

    def __str__(self):
        return 'bungalow'