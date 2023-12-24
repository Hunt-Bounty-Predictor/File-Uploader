from image_processing import *

class Map:
    def __init__(self, file):
        self.file = file
        self.image = loadImage(file, True)
        self.map = getMap(self.image)
        
        