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

path= 'images/1577x1365.png'
image = read_image(path)
show_image(image)
"""meanFilter = Mean(3, 3)
output = meanFilter.apply_to_image(image)"""

"""gaussianFilter = Gaussian(3)
output = gaussianFilter.apply_to_image(image)
show_image(output)"""

"""medianFilter = Median(3, 3)
output = medianFilter.apply_to_image(image)
show_image(output)"""

"""conservativeSmoo = ConservativeSmoo(5, 5)
output = conservativeSmoo.apply_to_image(image)
show_image(output)"""

"""localNoise = LocalNoise(3, 3)
output = localNoise.apply_to_image(image)
show_image(output)"""

"""sharpening = Sharpening()
output = sharpening.apply_to_image(image)
show_image(output)"""

unsharpening = Unsharpening(5)
output = unsharpening.apply_to_image(image)
show_image(output)