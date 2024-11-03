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
            return min_eval

    def best_move(self):
        best_val = float('-inf')
        move = None
        for row in range(3):
            for col in range(3):
                if self.game_board.board[row][col] is None:
                    self.game_board.board[row][col] = 'O'
                    move_val = self.minimax(self.game_board.board, False)
                    self.game_board.board[row][col] = None
                    if move_val > best_val:
                        best_val = move_val
                        move = (row, col)
        return move