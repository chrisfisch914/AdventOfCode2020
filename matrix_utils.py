class MatrixUtils:
    @staticmethod
    def get_column(tile, col):
        return [row[col] for row in tile]

    @staticmethod
    def rotate_clockwise(matrix):
        result = []
        for tup in zip(*matrix[::-1]):
            result.append(list(tup))
        return result
   
    @staticmethod
    def rotate_counter_clockwise(matrix):
        for i in range(3):
            matrix = MatrixUtils.rotate_clockwise(matrix)
        return matrix

    @staticmethod
    def invert_x(matrix):
        new_matrix = []
        for row in range(len(matrix)):
            new_row = []
            for col in range(len(matrix[row])):
                new_row.append(matrix[row][len(matrix[row]) - 1 - col])
            new_matrix.append(new_row)
        return new_matrix

    @staticmethod
    def invert_y(matrix):
        new_matrix = []
        for row in range(len(matrix)):
            new_row = []
            for col in range(len(matrix[row])):
                new_row.append(matrix[len(matrix) -1 - row][col])
            new_matrix.append(new_row)
        return new_matrix

    @staticmethod
    def print_matrix(matrix):
        for row in matrix:
            row_string = ""
            for value in row:
                row_string += value
            print(row_string)
