from AverageDigitalFilter import AverageDigitalFilter
from MedianDigitalFilter import MedianDigitalFilter

averageFilter = AverageDigitalFilter()
medianFilter = MedianDigitalFilter(3, 5)

print(averageFilter.get_height(), averageFilter.get_width())
print(medianFilter.get_height(), medianFilter.get_width())
averageFilter.apply_to_image(5)
medianFilter.apply_to_image(10)
