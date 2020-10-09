from abc import ABC, abstractmethod

class Filter(ABC):
    __digitalFilter = None

    def __init__(self, height=3, width=3):
        self.__digitalFilter = self.make_digital_filter(height, width)

    @abstractmethod
    def make_digital_filter(self, height, width):
        raise NotImplementedError("You should implement filter first!")

    def get_height(self):
        return self.__digitalFilter.get_height()

    def get_width(self):
        return self.__digitalFilter.get_height()

    def apply_to_image(self, image):
        return self.__digitalFilter.apply(image)
