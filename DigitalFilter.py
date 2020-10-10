from abc import ABC, abstractmethod
import numpy as np

class Filter(ABC):
    __height = 0
    __width = 0
    __up_side_frame = 0
    __down_side_frame = 0
    __left_side_frame = 0
    __right_side_frame = 0

    def __init__(self, height=3, width=3):
        self.__height = height
        self.__width = width

    @abstractmethod
    def make_convolution(self, image, output):
        raise NotImplementedError("You should implement filter first!")

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def get_up_side_frame(self):
        return self.__up_side_frame

    def get_down_side_frame(self):
        return self.__down_side_frame

    def get_left_side_frame(self):
        return self.__left_side_frame

    def get_right_side_frame(self):
        return self.__right_side_frame

    def apply_to_image(self, image):
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
        number_of_rows_image = image[:, 0].size
        number_of_columns_image = image[0, :].size
        self.calculate_dimensions_for_each_side_frame()

        output = np.zeros((number_of_rows_image, number_of_columns_image))
        if self.__up_side_frame != 0:
            """ fill upside of frame"""
            for i in range(0, self.__up_side_frame):
                for j in range(0, number_of_columns_image):
                    output[i, j] = image[i, j]
        if self.__down_side_frame != 0:
            """ fill down_side of frame"""
            for i in range(number_of_rows_image - self.__down_side_frame, number_of_rows_image):
                for j in range(0, number_of_columns_image):
                    output[i, j] = image[i, j]
        if self.__left_side_frame != 0:
            """ fill left_side of frame"""
            for i in range(self.__up_side_frame, number_of_rows_image - self.__down_side_frame):
                for j in range(0, self.__left_side_frame):
                    output[i, j] = image[i, j]
        if self.__right_side_frame != 0:
            """ fill right_side of frame"""
            for i in range(self.__up_side_frame, number_of_rows_image - self.__down_side_frame):
                for j in range(number_of_columns_image - self.__right_side_frame, number_of_columns_image):
                    output[i, j] = image[i, j]

        return output

    def calculate_dimensions_for_each_side_frame(self):
        row_of_middle_pixel_inside_kernel = int(self.__height / 2)
        column_of_middle_pixel_inside_kernel = int(self.__width / 2)
        self.__left_side_frame = column_of_middle_pixel_inside_kernel
        self.__right_side_frame = self.__width - column_of_middle_pixel_inside_kernel - 1
        self.__up_side_frame = row_of_middle_pixel_inside_kernel
        self.__down_side_frame = self.__height - row_of_middle_pixel_inside_kernel - 1
