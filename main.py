class Board:
    board_size = 4
    def __init__(self):
        self.rows = [Row() for row_number in range(self.board_size)]
        self.columns = [Column() for column_number in range(self.board_size)]
        self.squares = [Square() for square_number in range(self.board_size)]
        self.cells = [Cell(self.board_size) for cell in range(self.board_size**2)]
        for cell_index, cell in enumerate(self.cells):
            row_no, col_no, square_no = self.calculate_coords(cell_index)
            self.rows[row_no].append(cell)
            self.columns[col_no].append(cell)
            self.squares[square_no].append(cell)

    def print_rows(self):
        for row in self.rows:
            row.print_row()

    def print_columns(self):
        for column in self.columns:
            column.print_column()
    
    def calculate_coords(self, cell_no):
        from math import sqrt
        square_size = int(sqrt(self.board_size))
        row_no = cell_no // self.board_size 
        col_no = cell_no % self.board_size 
        square_no = row_no // square_size * square_size + col_no // square_size 
        return row_no, col_no, square_no


class Row():
    def __init__(self):
        self.row_cells = []

    def get_possible_values(self):
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
    
    def erase(self, value): #what is this method doing?
        for cell in self.row_cells:
            cell.erase(value)


class Column():
    def __init__(self):
        self.column_cells = []

    def get_possible_values(self):
        get_possible_values = set()
        for cell in self.column_cells:
            get_possible_values = get_possible_values.union(cell.possible_values)
        return get_possible_values

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


class Square():
    def __init__(self):
        self.square_cells = []
    
    def get_possible_values(self):
        possible_values = set()
        for cell in self.square_cells:
            possible_values = possible_values.union(cell.possible_values)
            #print(cell.possible_values)
        return possible_values
    
    def append(self, cell):
        self.square_cells.append(cell)
        cell.square = self
    
    def erase(self, value):
        for cell in self.square_cells:
            cell.erase(value)

class Cell():
    def __init__(self, value_space):
        self.possible_values = set(range(1, value_space + 1))
        self.value = None
        self.row = None
        self.column = None
        self.square = None

    def set_value(self, value):
        if value in self.possible_values:
            self.value = value
            self.possible_values = set()
            self.row.erase(value) #what is this part of code doing?
            self.column.erase(value)
            self.square.erase(value)
        else:
            print("This cell already has value set.")
    
    def erase(self, value):
        self.possible_values.discard(value)


if __name__=="__main__":    
    board = Board()
    board.cells[0].set_value(1)
    board.cells[10].set_value(2)
    board.cells[10].set_value(3)
    board.cells[15].set_value(3)
    board.print_rows()
    print("Rows")
    print("Possible values for this row",board.rows[0].get_possible_values())
    print("Possible values for this row",board.rows[1].get_possible_values())
    print("Possible values for this row",board.rows[2].get_possible_values())
    print("Possible values for this row",board.rows[3].get_possible_values())
    print("Columns")
    print("Possible values for this column",board.columns[0].get_possible_values())
    print("Possible values for this column",board.columns[1].get_possible_values())
    print("Possible values for this column",board.columns[2].get_possible_values())
    print("Possible values for this column",board.columns[3].get_possible_values())
    print("Squares")
    print("Possible values for this square",board.squares[0].get_possible_values())
    print("Possible values for this square",board.squares[1].get_possible_values())
    print("Possible values for this square",board.squares[2].get_possible_values())
    print("Possible values for this square",board.squares[3].get_possible_values())
