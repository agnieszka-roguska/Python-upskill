board_size = 9
class Cell:
    """
    The smallest part of a sudoku board - the class that stores the data of a single cell
    """
    possible_values = set()
    for i in range(board_size):
        possible_values.add(i + 1)

    def __init__(self): #default cell properties
        self.value = None
        self.row_number = None
        self.column_number = None
    def set_value(self, value): #set cell to a given value(method input) and remove this element from possible values for this column/row
        if value in self.possible_values:
            self.value = value
            self.possible_values = {}
    
class Row:
    def __init__(self): #creates N Cell class instances (N = board size)
        self.row_cells = [Cell() for cell in range(board_size)]
    def get_possible_values(self): #gets the possible values for this row
        possible_values = {}
        for cell in range(self.row_cells):
            if self.row_cells[cell].value in possible_values:
                possible_values = possible_values.union(self.row_cells[cell].possible_values)
    def print_row(self):
        for cell in self.row_cells:
            print(cell.value, end = "\t")
        print("\n")

class Column:
    def __init__(self):
        column_cells = [None] * board_size
        for i in range(board_size):
            for row in Board.rows:
                column_cells[i] += row.row_cells[i]
        self.column_cells = [Row.row_cells[i] for i in range(Row.row_cells)]
    def get_possible_values(self): #gets the possible values for this column
        possible_values = {}
        for cell in range(self.row_cells):
            if self.row_cells[cell].value in possible_values:
                possible_values = possible_values.union(self.row_cells[cell].possible_values)
    def print_column(self):
        for cell in self.column_cells:
            print(cell.value, end = "\t")
        print("\n")

class Board:
    def __init__(self):
        self.rows = [Row() for row in range(board_size)]
        self.columns = [self.rows[i] for i in range(board_size)]
        for row_number in range(len(self.rows)):
            for cell in self.rows[row_number].row_cells:
                cell.row_number = row_number
        """for column_number in range(len(self.columns)):
            for cell in self.columns[column_number].column_cells:
                cell.column_number = column_number"""
    def print_rows(self):
        for row in self.rows:
            row.print_row()
    def print_columns(self):
        for column in self.columns:
            column.print_row()

board = Board()
board.rows[1].row_cells[1].set_value(3)
board.columns[3].column_cells[2].set_value(1)
board.print_columns()
print("\n\n")
board.print_rows()
print(board.rows[1].row_cells[1].row_number, board.rows[1].row_cells[1].column_number)