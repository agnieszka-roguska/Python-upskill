class Board:
    board_size = 4
    def __init__(self):
        self.rows = [Row() for row_number in range(self.board_size)]
        self.columns = [Column() for column_number in range(self.board_size)]
        self.cells = [Cell(self.board_size) for cell in range(self.board_size**2)]
        for index, cell in enumerate(self.cells):
            self.rows[index // self.board_size].append(cell)
            self.columns[index % self.board_size].append(cell)

    def print_rows(self):
        for row in self.rows:
            row.print_row()

    def print_columns(self):
        for column in self.columns:
            column.print_column()


class Row():
    row_number = None
    def __init__(self):
        self.row_cells = []

    def get_possible_values_row(self):
        possible_values = set()
        for cell in self.row_cells:
            possible_values = possible_values.union(cell.possible_values)
        return possible_values
    
    def print_row(self):
        for cell in self.row_cells:
            print(cell.value, end = "\t")
        print("\n")
    
    def append(self, cell):
        self.row_cells.append(cell)
        cell.row = self
    
    def erase(self, value):
        for cell in self.row_cells:
            cell.erase(value)


class Column():
    def __init__(self):
        self.column_cells = []

    def get_possible_values_column(self):
        possible_values_col = set()
        for cell in self.column_cells:
            possible_values_col = possible_values_col.union(cell.possible_values)
        return possible_values_col

    def print_column(self):
        for cell in self.column_cells:
            print(cell.value, end = "\t")
        print("\n")

    def append(self, cell):
        self.column_cells.append(cell)
        cell.column = self

    def erase(self, value):
        for cell in self.column_cells:
            cell.erase(value)


class Cell():
    def __init__(self, value_space):
        self.possible_values = set(range(1, value_space + 1))
        self.value = None
        self.row = None
        self.column = None

    def set_value(self, value):
        if value in self.possible_values:
            self.value = value
            self.possible_values = set()
            self.row.erase(value)
            self.column.erase(value)
        else:
            print("This cell already has value.")
    
    def erase(self, value):
        self.possible_values.discard(value)


if __name__=="__main__":    
    board = Board()
    board.cells[0].set_value(1)
    board.cells[10].set_value(2)
    board.cells[10].set_value(3)
    board.print_rows()
    print("Possible values for this row",board.rows[0].get_possible_values_row())
    print("Possible values for this row",board.rows[1].get_possible_values_row())
    print("Possible values for this row",board.rows[2].get_possible_values_row())
    print("Possible values for this row",board.rows[3].get_possible_values_row())
    print("Possible values for this column",board.columns[0].get_possible_values_column())
    print("Possible values for this column",board.columns[1].get_possible_values_column())
    print("Possible values for this column",board.columns[2].get_possible_values_column())
    print("Possible values for this column",board.columns[3].get_possible_values_column())