class GameBoard:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        if self.board[row][col] is None:
            self.board[row][col] = player
            return True
        return False

    def check_winner(self):
        win_conditions = [
            [(0, 0), (0, 1), (0, 2)],  # Fila superior
            [(1, 0), (1, 1), (1, 2)],  # Fila central
            [(2, 0), (2, 1), (2, 2)],  # Fila inferior
            [(0, 0), (1, 0), (2, 0)],  # Columna izquierda
            [(0, 1), (1, 1), (2, 1)],  # Columna central
            [(0, 2), (1, 2), (2, 2)],  # Columna derecha
            [(0, 0), (1, 1), (2, 2)],  # Diagonal principal
            [(0, 2), (1, 1), (2, 0)]   # Diagonal secundaria
        ]
        for condition in win_conditions:
            if self.board[condition[0][0]][condition[0][1]] == \
               self.board[condition[1][0]][condition[1][1]] == \
               self.board[condition[2][0]][condition[2][1]] and \
               self.board[condition[0][0]][condition[0][1]] is not None:
                return self.board[condition[0][0]][condition[0][1]]
        
        if all(cell is not None for row in self.board for cell in row):
            return 'Tie'
        return None