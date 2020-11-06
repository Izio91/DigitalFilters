from DigitalFilter import Filter
import numpy as np
import cv2

class LocalNoise(Filter):
    __kernel = None
    __local_mean_matrix = None
    __local_variance_matrix = None

    def make_convolution(self, image, output):
        hue_noise_variance = None
        sat_noise_variance = None
        val_noise_variance = None
        gray_noise_variance = None

        if not self.image_is_in_gray_scale(image):
            image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        self.create_kernel(image)
        self.fill_local_mean_matrix(image, output)
        self.fill_local_variance_matrix(image, output)

        if not self.image_is_in_gray_scale(image):
            hue_noise_variance = np.average(self.__local_variance_matrix[:, :, 0])
            sat_noise_variance = np.average(self.__local_variance_matrix[:, :, 1])
            val_noise_variance = np.average(self.__local_variance_matrix[:, :, 2])

        else:
            gray_noise_variance = np.average(self.__local_variance_matrix)

        for i in range(self.__local_variance_matrix.shape[0]):
            for j in range(self.__local_variance_matrix.shape[1]):
                if not self.image_is_in_gray_scale(image):
                    if hue_noise_variance > self.__local_variance_matrix[i, j, 0]:
                        self.__local_variance_matrix[i, j, 0] = hue_noise_variance

                    if sat_noise_variance > self.__local_variance_matrix[i, j, 1]:
                        self.__local_variance_matrix[i, j, 1] = sat_noise_variance

                    if val_noise_variance > self.__local_variance_matrix[i, j, 2]:
                        self.__local_variance_matrix[i, j, 2] = val_noise_variance

                else:
                    if gray_noise_variance > self.__local_variance_matrix[i, j]:
                        self.__local_variance_matrix[i, j] = gray_noise_variance

        if not self.image_is_in_gray_scale(image):
            output = image - (np.array([hue_noise_variance, sat_noise_variance, val_noise_variance]) /
                              self.__local_variance_matrix) * (image - self.__local_mean_matrix)
            output = cv2.cvtColor(output.astype(np.uint8), cv2.COLOR_HSV2BGR)
        else:
            output = image - (gray_noise_variance / self.__local_variance_matrix) * (image - self.__local_mean_matrix)

        return output.astype(np.uint8)

    def create_kernel(self, image):
        if not self.image_is_in_gray_scale(image):
            self.__kernel = np.zeros((self.get_height(), self.get_width(), 3))
        else:
            self.__kernel = np.zeros((self.get_height(), self.get_width()))

    def fill_local_mean_matrix(self, image, output):
        print(output.shape)
        self.__local_mean_matrix = np.zeros(output.shape)
        self.__local_mean_matrix = self.__local_mean_matrix + output
        starting_row = int(self.get_height() / 2)
        starting_column = int(self.get_width() / 2)
        ending_row = image.shape[0] - self.get_down_side_frame()
        ending_column = image.shape[1] - self.get_right_side_frame()
        for i in range(starting_row, ending_row):
            for j in range(starting_column, ending_column):
                for q in range(i - self.get_up_side_frame(), i - self.get_up_side_frame() + self.get_height()):
                    for r in range(j - self.get_left_side_frame(), j - self.get_left_side_frame() + self.get_width()):
                        row_kernel = q - i + self.get_up_side_frame()
                        column_kernel = r - j + self.get_left_side_frame()
                        self.__kernel[row_kernel, column_kernel] = image[q, r]

                if not self.image_is_in_gray_scale(image):
                    hue_avg = np.average(self.__kernel[:, :, 0])
                    sat_avg = np.average(self.__kernel[:, :, 1])
                    val_avg = np.average(self.__kernel[:, :, 2])

                    self.__local_mean_matrix[i, j] = np.array([hue_avg, sat_avg, val_avg])
                else:
                    self.__local_mean_matrix[i, j] = np.average(self.__kernel)
        return self.__local_mean_matrix

    def fill_local_variance_matrix(self, image, output):
        self.__local_variance_matrix = np.zeros(output.shape)
        self.__local_variance_matrix = self.__local_variance_matrix + output
        starting_row = int(self.get_height() / 2)
        starting_column = int(self.get_width() / 2)
        ending_row = image.shape[0] - self.get_down_side_frame()
        ending_column = image.shape[1] - self.get_right_side_frame()
        for i in range(starting_row, ending_row):
            for j in range(starting_column, ending_column):
                for q in range(i - self.get_up_side_frame(), i - self.get_up_side_frame() + self.get_height()):
                    for r in range(j - self.get_left_side_frame(), j - self.get_left_side_frame() + self.get_width()):
                        row_kernel = q - i + self.get_up_side_frame()
                        column_kernel = r - j + self.get_left_side_frame()
                        self.__kernel[row_kernel, column_kernel] = image[q, r]

                if not self.image_is_in_gray_scale(image):
                    hue_std = np.std(self.__kernel[:, :, 0])
                    sat_std = np.std(self.__kernel[:, :, 1])
                    val_std = np.std(self.__kernel[:, :, 2])

                    self.__local_variance_matrix[i, j] = np.array([hue_std, sat_std, val_std])
                else:
                    self.__local_variance_matrix[i, j] = np.std(self.__kernel)
        return self.__local_variance_matrix


    def image_is_in_gray_scale(self, image):
        return len(image.shape) == 2