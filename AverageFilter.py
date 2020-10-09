class Average:
    __height = 0
    __width = 0
    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        print("Average Filter")

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def apply(self, image):
        print("I'm average filter and these is the image:", image)
        print("Those are my sizes:", self.get_height(), self.get_width())