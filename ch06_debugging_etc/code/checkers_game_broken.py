EMPTY_CELL = '.'


class Board:
    def __init__(self):
        self.cells = [['.'] * 8] * 8
        self.cells[0] = list('b.' * 4)
        self.cells[1] = list('.b' * 4)
        self.cells[2] = self.cells[0]
        self.cells[7] = list('.w' * 4)
        self.cells[6] = list('w.' * 4)
        self.cells[5] = self.cells[7]
        
    def move(self, colour, source, target):
        source_row, source_column = source
        target_row, target_column = target
        if self.cells[source_row][source_column] != colour:
            raise ValueError
        if self.cells[target_row][target_column] != EMPTY_CELL:
            raise ValueError
        self.cells[source_row][source_column] = EMPTY_CELL
        self.cells[target_row][target_column] = colour

    def show(self):
        for row in self.cells:
            print(''.join(row))


board = Board()
board.move('b', (2, 0), (3, 1))
board.move('w', (5, 1), (4, 0))
board.show()

# output
# ..b.b.b.
# .b.b.b.b
# ..b.b.b.
# wb......
# wb......
# ...w.w.w
# w.w.w.w.
# ...w.w.w
