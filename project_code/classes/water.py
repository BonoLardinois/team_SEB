# Team SEB 
# Minor Programmeren (Programmeertheorie)  
# render_randomise.py
#
# - Water class.

class Water():

    def __init__(self, bottom_left, top_right, polygon):
        self.name = "water"
        self.width = top_right[0] - bottom_left[0]
        self.depth = top_right[1] - bottom_left[1]
        self.bottom_left = bottom_left 
        self.top_right = top_right
        self.polygon = polygon