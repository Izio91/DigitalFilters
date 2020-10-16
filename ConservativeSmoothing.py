from DigitalFilter import Filter
from Utilities import show_image

class ConservativeSmoo(Filter):
    def make_convolution(self, image, output):
        starting_row = int(self.get_height() / 2)
        starting_column = int(self.get_width() / 2)
        ending_row = image[:, 0].size - self.get_down_side_frame()
        ending_column = image[0, :].size - self.get_right_side_frame()

        for i in range(starting_row, ending_row):
            for j in range(starting_column, ending_column):
                min_value = 255
                max_value = 0
                row_of_middle_pixel_inside_kernel = int((i - self.get_up_side_frame() + self.get_height()) / 2)
                column_of_middle_pixel_inside_kernel = int((j - self.get_left_side_frame() + self.get_width()) / 2)
                for q in range(i - self.get_up_side_frame(), i - self.get_up_side_frame() + self.get_height()):
                    for r in range(j - self.get_left_side_frame(), j - self.get_left_side_frame() + self.get_width()):
                        if row_of_middle_pixel_inside_kernel != q and column_of_middle_pixel_inside_kernel != r:
                            if image[q, r] < min_value:
                                min_value = image[q, r]

                            if image[q, r] > max_value:
                                max_value = image[q, r]
                if image[i, j] < min_value:
                    output[i, j] = min_value
                elif image[i, j] > max_value:
                    output[i, j] = max_value
                else:
                    output[i, j] = image[i, j]
        return output