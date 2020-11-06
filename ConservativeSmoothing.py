from DigitalFilter import Filter
import numpy as np
import cv2

class ConservativeSmoo(Filter):
    def make_convolution(self, image, output):
        starting_row = int(self.get_height() / 2)
        starting_column = int(self.get_width() / 2)
        ending_row = image.shape[0] - self.get_down_side_frame()
        ending_column = image.shape[1] - self.get_right_side_frame()

        if not self.image_is_in_gray_scale(image):
            image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        for i in range(starting_row, ending_row):
            for j in range(starting_column, ending_column):
                min_gray_scale_value, min_hue_scale_value, min_saturation_scale_value, min_value_scale = 255,255,255,255
                max_gray_scale_value, max_hue_scale_value, max_saturation_scale_value, max_value_scale = 0,0,0,0
                row_of_middle_pixel_inside_kernel = int((i - self.get_up_side_frame() + self.get_height()) / 2)
                column_of_middle_pixel_inside_kernel = int((j - self.get_left_side_frame() + self.get_width()) / 2)
                for q in range(i - self.get_up_side_frame(), i - self.get_up_side_frame() + self.get_height()):
                    for r in range(j - self.get_left_side_frame(), j - self.get_left_side_frame() + self.get_width()):
                        if row_of_middle_pixel_inside_kernel != q and column_of_middle_pixel_inside_kernel != r:

                            if not self.image_is_in_gray_scale(image):
                                if image[q, r, 0] < min_hue_scale_value:
                                    min_hue_scale_value = image[q, r, 0]

                                if image[q, r, 0] > max_hue_scale_value:
                                    max_hue_scale_value = image[q, r, 0]

                                if image[q, r, 1] < min_saturation_scale_value:
                                    min_saturation_scale_value = image[q, r, 1]

                                if image[q, r, 1] > max_saturation_scale_value:
                                    max_saturation_scale_value = image[q, r, 1]

                                if image[q, r, 2] < min_value_scale:
                                    min_value_scale = image[q, r, 2]

                                if image[q, r, 2] > max_value_scale:
                                    max_value_scale = image[q, r, 2]
                            else:
                                if image[q, r] < min_gray_scale_value:
                                    min_gray_scale_value = image[q, r]

                                if image[q, r] > max_gray_scale_value:
                                    max_gray_scale_value = image[q, r]

                if not self.image_is_in_gray_scale(image):
                    hue_scale_value, saturation_scale_value, value_scale = 0, 0, 0
                    if image[i, j, 0] < min_hue_scale_value:
                        hue_scale_value = min_hue_scale_value
                    elif image[i, j, 0] > max_hue_scale_value:
                        hue_scale_value = max_hue_scale_value
                    else:
                        hue_scale_value = image[i, j, 0]

                    if image[i, j, 1] < min_saturation_scale_value:
                        saturation_scale_value = min_saturation_scale_value
                    elif image[i, j, 1] > max_saturation_scale_value:
                        saturation_scale_value = max_saturation_scale_value
                    else:
                        saturation_scale_value = image[i, j, 1]

                    if image[i, j, 2] < min_value_scale:
                        value_scale = min_value_scale
                    elif image[i, j, 2] > max_value_scale:
                        value_scale = max_value_scale
                    else:
                        value_scale = image[i, j, 2]

                    output[i, j] = np.array([hue_scale_value, saturation_scale_value, value_scale])
                else:
                    if image[i, j] < min_gray_scale_value:
                        output[i, j] = min_gray_scale_value
                    elif image[i, j] > max_gray_scale_value:
                        output[i, j] = max_gray_scale_value
                    else:
                        output[i, j] = image[i, j]

        if not self.image_is_in_gray_scale(image):
            output = cv2.cvtColor(output.astype(np.uint8), cv2.COLOR_HSV2BGR)
        return output.astype(np.uint8)

    def image_is_in_gray_scale(self, image):
        return len(image.shape) == 2