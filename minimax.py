class MinimaxAI:
    def __init__(self, game_board):
        self.game_board = game_board

    def minimax(self, board, is_maximizing):
        winner = self.game_board.check_winner()
        if winner == 'O':
            return 1
        elif winner == 'X':
            return -1
        elif winner == 'Tie':
            return 0

        if is_maximizing:
            max_eval = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] is None:
                        board[row][col] = 'O'
                        eval = self.minimax(board, False)
                        board[row][col] = None
                        max_eval = max(max_eval, eval)
                        print(max_eval)
            return max_eval
        else:
            min_eval = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] is None:
                        board[row][col] = 'X'
                        eval = self.minimax(board, True)
                        board[row][col] = None
                        min_eval = min(min_eval, eval)
                        print(min_eval)
            return min_eval

    def best_move(self):
        best_val = float('-inf')
        move = None
        decision_matrix = []

        for row in range(3):
            for col in range(3):
                if self.game_board.board[row][col] is None:
                    # Simular movimiento
                    self.game_board.board[row][col] = 'O'
                    move_val = self.minimax(self.game_board.board, False)

                    # Ajustar el puntaje si es necesario
                    adjusted_score = move_val - (0.1 if move_val == 0 else 0)
                    decision_matrix.append(((row, col), adjusted_score))

                    # Restaurar estado
                    self.game_board.board[row][col] = None

                    # Buscar el mejor movimiento
                    if adjusted_score > best_val:
                        best_val = adjusted_score
                        move = (row, col)

        return move, decision_matrix