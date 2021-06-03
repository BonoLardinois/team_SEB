class Maison():

    def __init__(self, coordinates):
        self.name = "maison"
        self.width = 24
        self.depth = 22
        self.price = 610000
        self.bottom_left = coordinates

    def get_price(self):
        pass
    
    def __str__(self):
        return 'maison'