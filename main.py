import random
from math import sqrt


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
        self.cells_checked = []

    def __str__(self):
        result = ''
        for row in self.rows:
            result += row.get_row_str()
            result += "\n\n"
        return result
    
    def get_board_str(self):
        return self.__str__()

    def calculate_coords(self, cell_no):
        square_size = int(sqrt(self.board_size))
        row_no = cell_no // self.board_size
        col_no = cell_no % self.board_size
        square_no = row_no // square_size * square_size + col_no // square_size
        return row_no, col_no, square_no
    
    def fill_first_row(self):
        for cell in self.rows[0].row_cells:
            random_value = random.choice(list(cell.possible_values))
            cell.set_value(random_value)

    def find_empty_cell(self):
        for cell_no in range(len(self.cells)):
            if not self.cells[cell_no].value:
                return self.calculate_coords(cell_no)
        return None

    def solve_sudoku(self):
        # based on backtracking algorithm
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
            if self.solve_sudoku():
                return True
            cell.undo_set_value(value)
        return False
    
    def get_random_cell(self):
        return random.choice(self.cells)
    
    def remove_random_cell_value(self):
        """
        Randomly selects one cell and checks if has not been already selected. Removes value from this cell and checks how many possible values this cell has - if more than 1, undo (set this value again)
        """
        cell = self.get_random_cell()
        if cell in self.cells_checked:
            return False
        self.cells_checked.append(cell)
        removed_value = cell.value
        cell.undo_set_value(removed_value)
        if len(cell.possible_values) > 1:
            cell.set_value(removed_value)
            return False
        return True
    
    def create_puzzle(self):
        while set(self.cells) != set(self.cells_checked):
            self.remove_random_cell_value()


class Row:
    def __init__(self):
        self.row_cells = []

    def __str__(self):
        result = ''
        for cell in self.row_cells:
            if not cell.value:
                result += "X"
            else:
                result += str(cell.value)
            if cell != self.row_cells[-1]:
                result += ",\t"
        return result
    
    def get_row_str(self):
        return self.__str__()

    def get_possible_values(self):
        possible_values = set()
        for cell in self.row_cells:
            possible_values = possible_values.union(cell.possible_values)
        return possible_values

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
    board.fill_first_row()
    board.solve_sudoku()
    board.create_puzzle()
    print(board)
    with open("sudoku_puzzle.txt", "w") as sudoku_file:
        sudoku_file.write(board.get_board_str())
        sudoku_file.close()