import tkinter as tk
from tkinter import messagebox

from board import GameBoard
from minimax import MinimaxAI


class TicTacToeUI:
    def __init__(self):
        # Crear ventana principal e instancias de GameBoard y MinimaxAI
        self.window = tk.Tk()
        self.window.title("TIC TAC TOE")
        self.game_board = GameBoard()
        self.ai = MinimaxAI(self.game_board)
        self.current_player = 'X'  # 'X' es el jugador humano, 'O' es la IA

        # Crear botones para el tablero
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.window, text='', font=('Arial', 20), width=5, height=2,
                                   command=lambda row=row, col=col: self.make_move(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def reset_game(self):
        self.game_board.reset()
        self.current_player = 'X'
        for row in self.buttons:
            for button in row:
                button.config(text='', state='normal')

    def make_move(self, row, col):
        if self.current_player == 'X':
            if self.game_board.make_move(row, col, 'X'):
                self.buttons[row][col].config(text='X')
                winner = self.game_board.check_winner()
                if winner:
                    self.end_game(winner)
                else:
                    self.current_player = 'O'
                    self.ai_move()

    def ai_move(self):
        best_move = self.ai.best_move()
        if best_move:
            row, col = best_move
            self.game_board.make_move(row, col, 'O')
            self.buttons[row][col].config(text='O')
            winner = self.game_board.check_winner()
            if winner:
                self.end_game(winner)
            else:
                self.current_player = 'X'

    def end_game(self, winner):
        if winner == 'Tie':
            messagebox.showinfo("TIC TAC TOE", "Es un empate!")
        else:
            messagebox.showinfo("TIC TAC TOE", f"¡El ganador es {winner}!")
        self.reset_game()

    def run(self):
        self.window.mainloop()
