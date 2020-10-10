import numpy as np
from AverageFilter import Average
from GaussianFilter import Gaussian

"""averageFilter = Average(3, 3)
image = np.ones((1024, 1024))
print(averageFilter.apply_to_image(image))"""

gaussianFilter = Gaussian(3, 3)
image = np.ones((100, 100))
print(gaussianFilter.apply_to_image(image))
