""""Author: Sam Schickler"""
import skimage
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from skimage.external import tifffile as tiff

"""
Definition: This function finds the porosity of a given image file. 
Input: image file(including path), circle_mask controls whether a circular mask is applied before calculating
    the porosity, circle_mask_size describe the size of the circle 1 is the full width and height of the image and .1 
    1/10 of the height/width of the image. display_mask is a debugging tool that will display the masked image.
    image_loaded if the image should be passed as data(True) or as a path (False)
Output: Percentage of porosity"""
def calculate_porosity(file, circle_mask=False, circle_mask_size = 1, display_mask=False, image_loaded = False, threshold=True):
    if image_loaded:
        image = file
    else:
        image = tiff.imread(file)    # reads image

    if(len(image.shape) == 3):   # finds x,y dimensions of the image
        x1, y1, _ = image.shape
    elif len(image.shape) == 2:
        x1, y1 = image.shape
    if(circle_mask):
        X, Y = np.ogrid[0:x1, 0:y1]  # Creates grid of 0's for mask
        mask = (X - x1 / 2) ** 2 + (Y - y1 / 2) ** 2 > x1 * y1 * (circle_mask_size**2)/ 4 # defines a mask outside the
        # circle
        image[mask] = 0 # Sets image pixels in mask to 0
        original_image = image
        if(threshold):
            image[image<148] = 0
            image[image >= 148] = 1
        # print(np.amax(image))
        total_area = (x1 * y1 * (circle_mask_size**2) / 4) * 3.141592 # Calculates total area of cirlce
        if display_mask:
            plt.imshow(original_image, cmap='gray')
            plt.show()
    else:
        total_area = x1*y1

    if (len(image.shape) == 3):
        image_channel = image[::, ::, 0]  # if the image has 3 channels take the first one
    elif len(image.shape) == 2:
        image_channel = image
    non_zero = np.nonzero(image_channel)  # this finds all the non_zero indices in the image
    fiber_area = non_zero[0].shape[0]      # this counts all the non_zero indices in the image

    return fiber_area/total_area
if __name__ == "__main__":
    file = "/media/samschickler/1F6D-D692/Test/rec_8bit_phase_00010/FiberForm_19A_air_760torr_13_fast_00010_0200.rec.8bit.tif"
    test = calculate_porosity(file, circle_mask=True, circle_mask_size=.8, display_mask=True, threshold=False)
