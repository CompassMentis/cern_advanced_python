class Board:
    def __init__(self):
        self.squares = {(x, y): '' for x in range(8) for y in range(8)}

    def __setitem__(self, key, value):
        self.squares[key] = value

    def __getitem__(self, key):
        return self.squares[key]


board = Board()
board[1, 2] = 'King'
print(board[1, 2])
