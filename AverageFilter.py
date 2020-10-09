import numpy as np

class Average:
    __height = 0
    __width = 0
    __up_side_frame = 0
    __down_side_frame = 0
    __left_side_frame = 0
    __right_side_frame = 0

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def apply(self, image):
        self.check_image_properties(image)
        output = self.fill_frame(image)
        output = self.make_convolution(image, output)
        return output

    def check_image_properties(self, image):
        errorMsg = ""
        errorMsg, isCorrectFormat = self.check_image_format(errorMsg, image)
        errorMsg, areDimensionsCompatible = self.check_dimensions(errorMsg, image)

        if not isCorrectFormat or not areDimensionsCompatible:
            raise RuntimeError(errorMsg)

    def check_image_format(self, errorMsg, image):
        result = True
        if not isinstance(image, np.ndarray):
            result = False
            errorMsg = errorMsg + "Image is not instance of np.ndarray\n"
        return errorMsg, result

    def check_dimensions(self, errorMsg, image):
        result = True
        if self.__width > image[0, :].size or self.__height > image[:, 0].size:
            result = False
            errorMsg = errorMsg + "Dimensions are not compatibles\n"
        return errorMsg, result

    def fill_frame(self, image):
        self.calculate_dimensions_for_each_side_frame()

        output = np.zeros((image[0, :].size, image[:, 0].size))
        if self.__up_side_frame != 0:
            """ fill upside of frame"""
            for i in range(0, self.__up_side_frame):
                for j in range(0, image[0, :].size):
                    output[i, j] = image[i, j]
        if self.__down_side_frame != 0:
            """ fill down_side of frame"""
            for i in range(image[:, 0].size - self.__down_side_frame, image[:, 0].size):
                for j in range(0, image[0, :].size):
                    output[i, j] = image[i, j]
        if self.__left_side_frame != 0:
            """ fill left_side of frame"""
            for i in range(self.__up_side_frame, image[:, 0].size - self.__down_side_frame):
                for j in range(0, self.__left_side_frame):
                    output[i, j] = image[i, j]
        if self.__right_side_frame != 0:
            """ fill right_side of frame"""
            for i in range(self.__up_side_frame, image[:, 0].size - self.__down_side_frame):
                for j in range(image[0, :].size - self.__right_side_frame, image[0, :].size):
                    output[i, j] = image[i, j]

        return output

    def calculate_dimensions_for_each_side_frame(self):
        row_of_middle_pixel_inside_kernel = int(self.__height / 2)
        column_of_middle_pixel_inside_kernel = int(self.__width / 2)
        self.__left_side_frame = column_of_middle_pixel_inside_kernel
        self.__right_side_frame = self.__width - column_of_middle_pixel_inside_kernel - 1
        self.__up_side_frame = row_of_middle_pixel_inside_kernel
        self.__down_side_frame = self.__height - row_of_middle_pixel_inside_kernel - 1

    def make_convolution(self, image, output):
        average = 1/(self.__width * self.__height)
        starting_row = int(self.__height / 2)
        starting_column = int(self.__width / 2)
        ending_row = image[:, 0].size - self.__down_side_frame
        ending_column = image[0, :].size - self.__right_side_frame

        for i in range(starting_row, ending_row):
            for j in range(starting_column, ending_column):
                sum = 0
                for q in range(i - self.__up_side_frame, i + self.__down_side_frame):
                    for r in range(j - self.__left_side_frame, j + self.__right_side_frame):
                        sum = sum + image[q, r]
                output[i, j] = sum * average
        return output