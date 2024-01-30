import tkinter as tk
from tkinter import messagebox
import random

class SudokuApp:
    def __init__(self, master):
        self.master = master
        master.title("Sudoku Game")
        self.cells = {}
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.solution = None
        self.selected_cell = None
        self.initialize_grid()
        self.add_menu()
        self.add_check_buttons()

    def initialize_grid(self):
        for row in range(9):
            for col in range(9):
                cell = tk.Entry(self.master, width=2, font=('Arial', 18), borderwidth=1, justify='center', fg='white')
                cell.grid(row=row, column=col)
                cell.bind('<FocusIn>', lambda event, r=row, c=col: self.select_cell(r, c))
                self.cells[(row, col)] = cell

    def add_menu(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Game", command=self.new_game)
        file_menu.add_command(label="Exit", command=self.master.quit)

    def add_check_buttons(self):
        check_cell_button = tk.Button(self.master, text="Check Cell", command=self.check_cell)
        check_cell_button.grid(row=9, column=0, columnspan=4, sticky="nsew")
        check_board_button = tk.Button(self.master, text="Check Board", command=self.check_solution)
        check_board_button.grid(row=9, column=4, columnspan=5, sticky="nsew")

    def select_cell(self, row, col):
        self.selected_cell = (row, col)

    def new_game(self):
        self.generate_full_board()
        self.solution = [row[:] for row in self.board]  # Store the solution
        self.remove_numbers_for_puzzle(40)  # Remove numbers for a medium difficulty puzzle
        self.populate_grid_with_puzzle()

    def check_cell(self):
        if self.selected_cell:
            row, col = self.selected_cell
            current_val = self.cells[(row, col)].get()
            if current_val.isdigit() and int(current_val) == self.solution[row][col]:
                self.cells[(row, col)].config(fg='green')
            else:
                self.cells[(row, col)].config(fg='red')

    def check_solution(self):
        user_solution = self.get_current_board_state()
        if user_solution == self.solution:
            messagebox.showinfo("Success", "Congratulations! You solved the Sudoku!")
        else:
            messagebox.showerror("Error", "Incorrect solution. Please try again.")

    def generate_full_board(self):
        base = 3
        side = base * base
        def pattern(r, c): return (base*(r%base)+r//base+c)%side
        def shuffle(s): return random.sample(s, len(s))
        rBase = range(base)
        rows  = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols  = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        nums  = shuffle(range(1, base*base+1))

        board = [[nums[pattern(r, c)] for c in cols] for r in rows]
        rows  = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
        cols  = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
        self.board = [[board[r][c] for c in cols] for r in rows]

    def remove_numbers_for_puzzle(self, number_of_cells_to_remove):
        while number_of_cells_to_remove > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                number_of_cells_to_remove -= 1

    def populate_grid_with_puzzle(self):
        for row in range(9):
            for col in range(9):
                cell = self.cells[(row, col)]
                cell.delete(0, tk.END)
                if self.board[row][col] != 0:
                    cell.insert(0, str(self.board[row][col]))
                    cell.config(state='readonly', readonlybackground='black', fg='white')
                else:
                    cell.config(state='normal', background='black', fg='white')

    def get_current_board_state(self):
        board_state = []
        for row in range(9):
            board_row = []
            for col in range(9):
                val = self.cells[(row, col)].get()
                board_row.append(int(val) if val.isdigit() else 0)
            board_state.append(board_row)
        return board_state

def main():
    root = tk.Tk()
    root.configure(background='black')
    app = SudokuApp(root)
    app.new_game()  # Start a new game immediately for testing
    root.mainloop()

if __name__ == "__main__":
    main()
