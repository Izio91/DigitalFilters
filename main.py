import numpy as np
from AverageFilter import Average

averageFilter = Average(3, 3)
image = np.ones((10, 5))
print(averageFilter.apply_to_image(image))
