class Median:
    __height = 0
    __width = 0

    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        print("Median Filter")

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def apply(self, image):
        print("I'm median filter and these is the image:", image)