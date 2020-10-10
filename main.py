import numpy as np
from AverageFilter import Average
from GaussianFilter import Gaussian

averageFilter = Average(3, 3)
image = np.ones((10, 5))
print(averageFilter.apply_to_image(image))

"""gaussianFilter = Gaussian(3, 3)
image = np.ones((10, 5))
print(gaussianFilter.apply_to_image(image))"""
