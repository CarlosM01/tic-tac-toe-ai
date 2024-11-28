import tkinter as tk
from tkinter import messagebox

from board import GameBoard
from minimax import MinimaxAI


class TicTacToeUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("TIC TAC TOE")
        self.game_board = GameBoard()
        self.ai = MinimaxAI(self.game_board)
        self.current_player = 'X'

        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.window, text='', font=('Arial', 20), width=5, height=2,
                                   command=lambda row=row, col=col: self.make_move(row, col))
                button.grid(row=row, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

        self.create_decision_window()

    def create_decision_window(self):
        self.decision_window = tk.Toplevel(self.window)
        self.decision_window.title("Matriz de Decisión")
        self.decision_window.geometry("300x200")
        self.decision_labels = [[tk.Label(self.decision_window, text='', font=('Arial', 10), bg='white', width=10)
                                 for _ in range(3)] for _ in range(3)]
        for i, row in enumerate(self.decision_labels):
            for j, label in enumerate(row):
                label.grid(row=i, column=j, padx=5, pady=5)

    def update_decision_window(self, decision_matrix):
        for row in self.decision_labels:
            for label in row:
                label.config(text='', bg='white')

        for (row, col), score in decision_matrix:
            self.decision_labels[row][col].config(text=f"{score:.2f}", bg='lightblue')

    def reset_game(self):
        self.game_board.reset()
        self.current_player = 'X'
        for row in self.buttons:
            for button in row:
                button.config(text='', state='normal')
        self.update_decision_window([])

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
        move, decision_matrix = self.ai.best_move()
        self.update_decision_window(decision_matrix)
        if move:
            row, col = move
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