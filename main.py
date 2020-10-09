import numpy as np
from AverageDigitalFilter import AverageDigitalFilter
from MedianDigitalFilter import MedianDigitalFilter

averageFilter = AverageDigitalFilter(3, 3)
image = np.ones((1024, 1024))
print(averageFilter.apply_to_image(image))
