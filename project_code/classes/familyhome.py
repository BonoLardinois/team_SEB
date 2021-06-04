class Familyhome():

    def __init__(self, coordinates):
        self.name = "familyhome"
        self.width = 12
        self.depth = 12
        self.price = 285000
        self.bottom_left = coordinates
        self.top_right = tuple((self.bottom_left[0] + self.width, self.bottom_left[1] + self.depth))
        # print(f" familyhome {self.bottom_left} {self.top_right}")

    def get_price(self):
        pass
    
    def __str__(self):
        return 'familyhome'