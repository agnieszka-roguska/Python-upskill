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
    
    def fill_random_cell(self):
        import random
        if self.if_whole_board_filled is not True:
            while True:
                random_index = random.randint(0, len(self.cells) - 1)
                random_cell = self.cells[random_index]
                if len(random_cell.possible_values):
                    break
            random_value_to_be_set = random.choice(list(random_cell.possible_values))
            random_cell.set_value(random_value_to_be_set) 
            """
            sprawdz wartosci possible_values innych komorek po wpisaniu wartosci do komorki
            gdy possible_values jakiejs komorki (bez wartosci) bedzie zbiorem pustym - if_assigning_value_forbidden, cofnij operacje
            """
            
           
    def if_any_cell_with_one_possible_value(self):
        for cell in self.cells:
            if len(cell.possible_values) == 1:
                return True
        return False
    
    """def if_assigning_value_forbidden(self):
        for cell in self.cells:
            if (not cell.possible_values) and (cell.value is None):
                return True
        return False"""
    
    def fill_cells_with_one_possible_value(self):
        for cell in self.cells:
            if len(cell.possible_values) == 1:
                cell.set_value(list(cell.possible_values)[0])
                self.print_rows()
                print("\n\n")

    def fill_diagonals(self):
        import random
        for row_index, row in enumerate(self.rows):
            random_value_to_be_set = random.choice(list(row.row_cells[row_index].possible_values))
            row.row_cells[row_index].set_value(random_value_to_be_set)
            cell = row.row_cells[self.board_size - row_index - 1]
            if cell.possible_values:
                random_value_to_be_set = random.choice(list(cell.possible_values))
                cell.set_value(random_value_to_be_set)

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

    def erase(self, value):
        self.possible_values.discard(value)


if __name__=="__main__":
    board = Board()
    board.fill_diagonals()
    i = 0
    while not board.if_whole_board_filled(): #zle  - zostają komorki nie do uzupełnienia
        while board.if_any_cell_with_one_possible_value():
            board.fill_cells_with_one_possible_value()
        board.fill_random_cell()
    board.print_rows()