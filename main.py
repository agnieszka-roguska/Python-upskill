board_size = 4

class Cell:
    """
    The smallest part of a sudoku board - the class that stores the data for a single cell
    """
    possible_values = set()
    for i in range(board_size):
        possible_values.add(i + 1)

    def __init__(self): #default cell properties
        self.value = None
        self.row_number = None
        self.column_number = None
    def set_value(self, value): #sets cell to a given value(method's input)
        if value in self.possible_values:
            self.value = value
            self.possible_values = {}
    
class Row:
    def __init__(self): #creates N Cell class instances (N = board size)
        self.row_cells = [Cell() for cell in range(board_size)]
    def get_possible_values(self): #gets the possible values for this row
        possible_values = set()
        for cell in range(len(self.row_cells)):
            possible_values = possible_values.union(self.row_cells[cell].possible_values)
        return possible_values
    def print_row(self):
        for cell in self.row_cells:
            print(cell.value, end = "\t")
        print("\n")

class Column:
    def __init__(self):
        self.column_cells = [None] * board_size
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
        self.rows = [Row() for row_number in range(board_size)]
        self.columns = [Column() for column_number in range(board_size)]
        for column_number in range(board_size):
            temp = []
            for row_number in range(board_size):
               temp.append(self.rows[row_number].row_cells[column_number])
            self.columns[column_number].column_cells = temp[:]
        for row_number in range(len(self.rows)):
            for cell in self.rows[row_number].row_cells:
                cell.row_number = row_number
        for column_number in range(len(self.columns)):
            for cell in self.columns[column_number].column_cells:
                cell = column_number
    def set_cell_value(self, row_number, column_number, value):
        (self.rows[row_number].row_cells[column_number]).set_value(value)
        ################################################################# Do poprawy - possible values źle ustawiane podczas wpisywania wartosci do komorki
        """for cell in self.rows[row_number].row_cells:
            if value in cell.possible_values:
                cell.possible_values.remove(value)"""
        """for column in self.columns:
            for cell in range(len(column)):
                if value in column.column_cells[cell]"""
        #################################################################
    def print_rows(self):
        for row in self.rows:
            row.print_row()
    def print_columns(self):
        for column in self.columns:
            column.print_column()

board = Board()
board.set_cell_value(1,1,3)
board.set_cell_value(1,2,1)
board.set_cell_value(2,0,2)
print("\n\n")
board.print_rows()
print(board.rows[1].row_cells[2].value, board.rows[1].row_cells[2].possible_values)
print(board.rows[0].row_cells[1].value, board.rows[1].row_cells[1].possible_values)
print(board.rows[3].get_possible_values())