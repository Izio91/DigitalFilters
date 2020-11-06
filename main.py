import numpy as np
from MeanFilter import Mean
from GaussianFilter import Gaussian
from MedianFilter import Median
from ConservativeSmoothing import ConservativeSmoo
from SharpeningFilter import Sharpening
from UnsharpeningFilter import Unsharpening
from AdaptiveLocalNoiseFilter import LocalNoise
from Utilities import read_image
from Utilities import show_image
from Utilities import show_couple_of_images
import cv2

path= 'images/1577x1365.png'
path= 'images/745x419.jpg'
#path= 'images/306x341.png'
color_scale = "rgb"
title1 = "Original"
image = read_image(path, color_scale)
"""title2 = "Average"
meanFilter = Mean(5, 5)
output = meanFilter.apply_to_image(image)"""

"""
title2 = "Gaussian"
gaussianFilter = Gaussian(3)
output = gaussianFilter.apply_to_image(image)"""


"""title2 = "Median"
medianFilter = Median(3, 3)
output = medianFilter.apply_to_image(image)"""


"""title2 = "Conservative Smoothing"
conservativeSmoo = ConservativeSmoo(5, 5)
output = conservativeSmoo.apply_to_image(image)
"""


"""title2 = "Adaptive"
localNoise = LocalNoise(3, 3)
output = localNoise.apply_to_image(image)
"""

title2 = "Sharpening"
gaussianFilter = Gaussian(3)
image_filtered = gaussianFilter.apply_to_image(image)
sharpening = Sharpening()
output = sharpening.apply_to_image(image_filtered)

"""title2 = "Unsharpening"
unsharpening = Unsharpening(3)
output = unsharpening.apply_to_image(image)"""

show_couple_of_images(image, output, title1, title2, color_scale)