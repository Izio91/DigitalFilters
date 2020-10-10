from DigitalFilter import Filter
import statistics

class Median(Filter):
    def make_convolution(self, image, output):
        starting_row = int(self.get_height() / 2)
        starting_column = int(self.get_width() / 2)
        ending_row = image[:, 0].size - self.get_down_side_frame()
        ending_column = image[0, :].size - self.get_right_side_frame()

        for i in range(starting_row, ending_row):
            for j in range(starting_column, ending_column):
                tmp_list = []
                for q in range(i - self.get_up_side_frame(), i - self.get_up_side_frame() + self.get_height()):
                    for r in range(j - self.get_left_side_frame(), j - self.get_left_side_frame() + self.get_width()):
                        tmp_list.append(image[q, r])
                output[i, j] = statistics.median(tmp_list)
        return output
