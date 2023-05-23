class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[None for _ in range(columns)] for _ in range(rows)]
    def set_value(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.matrix[row][column] = value
            
    def get_value(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return self.matrix[row][column]
        return None

    def get_size(self):
        return (self.rows, self.columns)




matrix = Matrix(10, 10)
for row in range(matrix.get_size()[0]):
    for column in range(matrix.get_size()[1]):
        matrix.set_value(row, column, 1)

for row in range(matrix.get_size()[0]):
    for column in range(matrix.get_size()[1]):
        print(matrix.get_value(row, column), end=' ')
    print()