import numpy as np
from MeanFilter import Mean
from GaussianFilter import Gaussian
from MedianFilter import Median

"""meanFilter = Mean(3, 3)
image = np.ones((1024, 1024))
print(meanFilter.apply_to_image(image))"""

gaussianFilter = Gaussian(5)
image = np.ones((100, 100))*255
print(gaussianFilter.apply_to_image(image))

"""medianFilter = Median(3, 3)
image = np.ones((100, 100))
print(medianFilter.apply_to_image(image))"""
