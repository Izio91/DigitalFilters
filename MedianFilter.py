from DigitalFilter import Filter
import numpy as np
import statistics
import cv2

class Median(Filter):
    def make_convolution(self, image, output):
        starting_row = int(self.get_height() / 2)
        starting_column = int(self.get_width() / 2)
        ending_row = image.shape[0] - self.get_down_side_frame()
        ending_column = image.shape[1] - self.get_right_side_frame()
        tmp_list_with_gray_scale_value = None
        tmp_list_with_hue_scale_value = None
        tmp_list_with_saturation_scale_value = None
        tmp_list_with_value_scale = None

        if not self.image_is_in_gray_scale(image):
            image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        for i in range(starting_row, ending_row):
            for j in range(starting_column, ending_column):
                if not self.image_is_in_gray_scale(image):
                    tmp_list_with_hue_scale_value = []
                    tmp_list_with_saturation_scale_value = []
                    tmp_list_with_value_scale = []
                else:
                    tmp_list_with_gray_scale_value = []
                for q in range(i - self.get_up_side_frame(), i - self.get_up_side_frame() + self.get_height()):
                    for r in range(j - self.get_left_side_frame(), j - self.get_left_side_frame() + self.get_width()):
                        if not self.image_is_in_gray_scale(image):
                            tmp_list_with_hue_scale_value.append(image[q, r, 0])
                            tmp_list_with_saturation_scale_value.append(image[q, r, 1])
                            tmp_list_with_value_scale.append(image[q, r, 2])
                        else:
                            tmp_list_with_gray_scale_value.append(image[q, r])
                if  not self.image_is_in_gray_scale(image):
                    median_hue_value = statistics.median(tmp_list_with_hue_scale_value)
                    median_saturation_value = statistics.median(tmp_list_with_saturation_scale_value)
                    median_value_scale = statistics.median(tmp_list_with_value_scale)
                    output[i, j] = np.array([median_hue_value, median_saturation_value, median_value_scale])
                else:
                    output[i, j] = statistics.median(tmp_list_with_gray_scale_value)

        if not self.image_is_in_gray_scale(image):
            output = cv2.cvtColor(output.astype(np.uint8), cv2.COLOR_HSV2BGR)
        return output.astype(np.uint8)

    def image_is_in_gray_scale(self, image):
        return len(image.shape) == 2