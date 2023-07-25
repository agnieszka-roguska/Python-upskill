class Board:
    board_size = 4
    def __init__(self):
        self.rows = [Row() for row_number in range(self.board_size)]
        self.columns = [Column() for column_number in range(self.board_size)]
        self.cells = [Cell(self.board_size) for cell in range(self.board_size**2)]
        for index, cell in enumerate(self.cells):
            self.rows[index//self.board_size].append(cell)
            self.columns[index % self.board_size].append(cell)

    def set_cell_value(self, row_number, column_number, value):
        (self.rows[row_number].row_cells[column_number]).set_value(value)

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

    def get_possible_values_row(self): #gets the possible values for this row
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
    column_number = None
    def __init__(self):
        self.column_cells = []

    def get_possible_values_column(self): #gets the possible values for this column
        possible_values = set()
        for cell in range(len(self.column_cells)):
            possible_values = possible_values.union(self.column_cells[cell].possible_values)

    def print_column(self):
        for cell in self.column_cells:
            print(cell.value, end = "\t")
        print("\n")

    def set_cells_column_numbers(self):
        for cell in self.column_cells:
            cell.column_number = self.column_number

    def append(self, cell):
        self.column_cells.append(cell)
        cell.column = self

    def erase(self, value):
        for cell in self.column_cells:
            cell.erase(value)


class Cell():
    def __init__(self, value_space): #default cell properties
        self.possible_values = set(range(1, value_space + 1))
        self.value = None
        self.row = None
        self.column = None

    def set_value(self, value):
        if value in self.possible_values:
            self.value = value
            self.possible_values = {}
            self.row.erase(value)
    
    def erase(self, value):
        self.possible_values.remove(value)


if __name__=="__main__":    
    board = Board()
    print("\n\n")
    board.print_rows()
    print("Row 0")
    print("Value and possible_values",board.rows[0].row_cells[0].value, board.rows[0].row_cells[0].possible_values)
    print("Value and possible_values", board.rows[0].row_cells[1].value, board.rows[0].row_cells[1].possible_values)
    print("Value and possible_values", board.rows[0].row_cells[2].value, board.rows[0].row_cells[2].possible_values)
    print("Value and possible_values", board.rows[0].row_cells[3].value, board.rows[0].row_cells[3].possible_values)
    print("Row 1")
    print("Value and possible_values",board.rows[1].row_cells[0].value, board.rows[1].row_cells[0].possible_values)
    print("Value and possible_values", board.rows[1].row_cells[1].value, board.rows[1].row_cells[1].possible_values)
    print("Value and possible_values", board.rows[1].row_cells[2].value, board.rows[1].row_cells[2].possible_values)
    print("Value and possible_values", board.rows[1].row_cells[3].value, board.rows[1].row_cells[3].possible_values)
    print("Row 2")
    print("Value and possible_values",board.rows[2].row_cells[0].value, board.rows[2].row_cells[0].possible_values)
    print("Value and possible_values", board.rows[2].row_cells[1].value, board.rows[2].row_cells[1].possible_values)
    print("Value and possible_values", board.rows[2].row_cells[2].value, board.rows[2].row_cells[2].possible_values)
    print("Value and possible_values", board.rows[2].row_cells[3].value, board.rows[2].row_cells[3].possible_values)
    print("Row 3")
    print("Value and possible_values",board.rows[3].row_cells[0].value, board.rows[3].row_cells[0].possible_values)
    print("Value and possible_values", board.rows[3].row_cells[1].value, board.rows[3].row_cells[1].possible_values)
    print("Value and possible_values", board.rows[3].row_cells[2].value, board.rows[3].row_cells[2].possible_values)
    print("Value and possible_values", board.rows[3].row_cells[3].value, board.rows[3].row_cells[3].possible_values)
    print(board.rows[2].get_possible_values_row())
    print(board.columns[2].get_possible_values_column())