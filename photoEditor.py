
from PIL import Image
from numpy import array
import numpy as np

class ImageProcessor: 

    def __init__(self, image:str) -> None:
        self.image = Image.open(image)
        self.matrix = array(self.image)

    def bw(self, threshold):
        for rn, row in enumerate(self.matrix):
            for cn, column in enumerate(row):
                average = (int(column[0]) + int(column[1]) + int(column[2]))/3
                if average > threshold:
                    self.matrix[rn,cn] = [255,255,255]
                else:
                    self.matrix[rn,cn] = [0,0,0]
        return self

    def save(self, save_as:str):
        save_image = Image.fromarray(self.matrix.astype(np.uint8))
        save_image.save(save_as)
        return self
    
    def contrast(self, percent:int):
        percent /= 100
        for rn, row in enumerate(self.matrix):
            for cn, column in enumerate(row):
                for color_num, rgb in enumerate(column):
                    if rgb > 127.5:
                        self.matrix[rn,cn,color_num] = rgb + ((255 - float(rgb)) * percent)
                    else:
                        self.matrix[rn,cn,color_num] = rgb - (float(rgb) * percent)
        return self
                    