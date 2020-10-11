from DigitalFilter import Filter

class Mean(Filter):
    def make_convolution(self, image, output):
        average = 1/(self.get_width() * self.get_height())
        starting_row = int(self.get_height() / 2)
        starting_column = int(self.get_width() / 2)
        ending_row = image[:, 0].size - self.get_down_side_frame()
        ending_column = image[0, :].size - self.get_right_side_frame()

        for i in range(starting_row, ending_row):
            for j in range(starting_column, ending_column):
                sum = 0
                for q in range(i - self.get_up_side_frame(), i - self.get_up_side_frame() + self.get_height()):
                    for r in range(j - self.get_left_side_frame(), j - self.get_left_side_frame() + self.get_width()):
                        sum = sum + image[q, r]
                output[i, j] = sum * average
        return output
