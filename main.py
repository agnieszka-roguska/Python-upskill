class Board:
    board_size = 9
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
    
    def fill_random_cell(self): #randomly chooses one square and a random cell within that square; checks if this cell already has any value assigned and if not, assigns random value from its possible values
        import random
        if self.if_whole_board_filled is not True:
            while True:
                random_index = random.randint(0, len(self.cells) - 1)
                random_cell = self.cells[random_index]
                if len(random_cell.possible_values):
                    print("all set")
                    break
            try:
                random_value_to_be_set = random.choice(list(random_cell.possible_values))
                print(random_value_to_be_set)
                random_cell.set_value(random_value_to_be_set)
            except:
                print("Exception, could not set randomly choosen value for this position", random_index, random_cell.value, random_cell.possible_values)
    
    """def search_squares(self):
        import random
        if not self.if_whole_board_filled:
            while True:
                random_index = random.randint(0, len(self.squares) - 1)
                random_square = self.squares[random_index]
                if not random_square.if_whole_square_filled:
                    for cell in random_square.square_cells:
                        if len(cell.possible_values) == 1:
                            cell.set_value(list(cell.possible_values)[0])"""
    
    def fill_diagonal(self):
        import random
        for row_index, row in enumerate(self.rows):
            random_value_to_be_set = random.choice(list(row.row_cells[row_index].possible_values))
            row.row_cells[row_index].set_value(random_value_to_be_set)
            cell = row.row_cells[self.board_size - row_index - 1]
            if cell.possible_values:
                random_value_to_be_set = random.choice(list(cell.possible_values))
                cell.set_value(random_value_to_be_set)
            else:
                print("Error, possible_values: ", cell.possible_values)

    def if_whole_board_filled(self):
        for cell in self.cells:
            if cell.value == None:
                return False
        return True


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
    
    def erase(self, value):
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
        return possible_values
    
    def append(self, cell):
        self.square_cells.append(cell)
        cell.square = self
    
    def erase(self, value):
        for cell in self.square_cells:
            cell.erase(value)
    
    def if_whole_square_filled(self):
        for cell in self.square_cells:
            if cell.value == None:
                return False
        return True

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
            self.row.erase(value)
            self.column.erase(value)
            self.square.erase(value)
        else:
            print("This cell already has value set.")
    
    def erase(self, value):
        self.possible_values.discard(value)


if __name__=="__main__":
    board = Board()
    board.fill_diagonal()
    board.print_rows()