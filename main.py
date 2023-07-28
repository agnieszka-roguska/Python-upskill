import random
from math import sqrt
from copy import deepcopy


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
        print("\n\n")

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

    def fill_squares_on_diagonal(self):
        diagonal_square_indexes = range(
            0, self.board_size, int(sqrt(self.board_size)) + 1
        )
        for square_no in diagonal_square_indexes:
            possible_values = list(range(1, self.board_size + 1))
            for cell in self.squares[int(square_no)].square_cells:
                random_value = random.choice(possible_values)
                cell.set_value(random_value)
                possible_values.remove(random_value)

    def if_whole_board_filled(self):
        for cell in self.cells:
            if cell.value == None:
                return False
        return True

    def find_empty_cell(self):
        for cell_no in range(len(self.cells)):
            if not self.cells[cell_no].value:
                return self.calculate_coords(cell_no)
        return None

    def solve_sudoku(self):
        # sometimes works for 4x4 board, doesn't work for 9x9(yet)
        # besed on backtracking algorithm
        # checks if there are any empty cells on the board - find_empty_cell returns the coordinates of the first empty cell it finds
        if not self.find_empty_cell():
            return True
        else:
            row_no, col_no, _ = self.find_empty_cell()
        cell = self.rows[row_no].row_cells[col_no]
        # iterate through all possile_values for this cell
        # set value
        # call `solve_sudoku` for resulted board <- if does not work, undo set_cell and try another value from possible_values
        for value in sorted(list(cell.possible_values)):
            cell.set_value(value)
            self.print_rows()
            if self.solve_sudoku():
                return True
            cell.undo_set_value(value)
        return False


class Row:
    def __init__(self):
        self.row_cells = []

    def get_possible_values(self):
        possible_values = set()
        for cell in self.row_cells:
            possible_values = possible_values.union(cell.possible_values)
        return possible_values

    def print_row(self):
        for cell in self.row_cells:
            print(cell.value, end="\t")
        print("\n")

    def append(self, cell):
        self.row_cells.append(cell)
        cell.row = self

    def erase(self, value):
        for cell in self.row_cells:
            cell.erase(value)

    def undo_erase(self, value):
        for cell in self.row_cells:
            cell.undo_erase(value)


class Column:
    def __init__(self):
        self.column_cells = []

    def get_possible_values(self):
        get_possible_values = set()
        for cell in self.column_cells:
            get_possible_values = get_possible_values.union(cell.possible_values)
        return get_possible_values

    def print_column(self):
        for cell in self.column_cells:
            print(cell.value, end="\t")
        print("\n")

    def append(self, cell):
        self.column_cells.append(cell)
        cell.column = self

    def erase(self, value):
        for cell in self.column_cells:
            cell.erase(value)

    def undo_erase(self, value):
        for cell in self.column_cells:
            cell.undo_erase(value)


class Square:
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

    def undo_erase(self, value):
        for cell in self.square_cells:
            cell.undo_erase(value)


class Cell:
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

    def undo_set_value(self, value):
        self.possible_values.add(value)

        self.value = None

        self.row.undo_erase(value)
        self.column.undo_erase(value)
        self.square.undo_erase(value)
        self.possible_values = self.row.get_possible_values().intersection(
            self.column.get_possible_values(), self.square.get_possible_values()
        )

    def erase(self, value):
        if value in self.possible_values:
            self.possible_values.remove(value)

    def undo_erase(self, value):
        self.possible_values = self.row.get_possible_values().intersection(
            self.column.get_possible_values(), self.square.get_possible_values()
        )


if __name__ == "__main__":
    import random

    board = Board()
    #board.fill_squares_on_diagonal()
    if not board.solve_sudoku():
        print("Failed")
    board.print_rows()
