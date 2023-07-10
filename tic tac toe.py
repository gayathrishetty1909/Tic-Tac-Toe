import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.window, text=" ", width=10, height=5,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.reset_game()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return self.board[0][col]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None

    def check_tie(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def reset_game(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        for row in self.buttons:
            for button in row:
                button.config(text=" ")

    def run(self):
        self.window.mainloop()

game = TicTacToeGUI()
game.run()
