""""Author: Sam Schickler"""
import skimage
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from skimage.external import tifffile as tiff

"""
TODO: Add documentation"""
def crop(image, circle_mask=False, circle_mask_size = 1, square_mask = False, square_mask_dim = [100,1000,100,1000], display_mask=False):

    if(len(image.shape) == 3):   # finds x,y dimensions of the image
        x1, y1, _ = image.shape
    elif len(image.shape) == 2:
        x1, y1 = image.shape
    if(circle_mask):
        X, Y = np.ogrid[0:x1, 0:y1]  # Creates grid of 0's for mask
        mask = (X - x1 / 2) ** 2 + (Y - y1 / 2) ** 2 > x1 * y1 * (circle_mask_size**2)/ 4 # defines a mask outside the
        # circle
        image[mask] = 0 # Sets image pixels in mask to 0

    if square_mask:
        mask = np.ones([x1,y1], dtype=bool)
        mask[square_mask_dim[0]:square_mask_dim[1], square_mask_dim[2]:square_mask_dim[3]] = False

        image[mask] = 0



    if display_mask:
        plt.imshow(image, cmap='gray')
        plt.show()
    return image

if __name__ == "__main__":
    file = "/media/samschickler/1F6D-D692/FiberForm_19A_air_760torr_13_fast/rec_8bit_abs_00153/FiberForm_19A_air_760torr_13_fast_00153_0001.rec.8bit.tif"
    test = crop(file, square_mask=True, display_mask=True)
    print(test)