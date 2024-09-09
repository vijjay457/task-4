import numpy as np
# Function to check if a number is a possibility in a given position
def possibility(row, column, num, sudoku_puzzle):
    # Check if the number is not in the current row and column
    for i in range(9):
        if sudoku_puzzle[row][i] == num or sudoku_puzzle[i][column] == num:
            return False  
    # Check if the number is not in the current 3x3 grid
    x0, y0 = (column // 3) * 3, (row // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku_puzzle[y0 + i][x0 + j] == num:
                return False   
    return True
# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku(sudoku_puzzle):
    for row in range(9):
        for column in range(9):
            if sudoku_puzzle[row][column] == 0:
                for num in range(1, 10):
                    if possibility(row, column, num, sudoku_puzzle):
                        sudoku_puzzle[row][column] = num
                        if solve_sudoku(sudoku_puzzle):
                            return True
                        sudoku_puzzle[row][column] = 0
                return False
    return True
# Function to display the Sudoku puzzle
def print_sudoku(sudoku_puzzle):
    print(np.matrix(sudoku_puzzle))
# User input for the Sudoku puzzle
sudoku_puzzle = []
for i in range(9):
    row = input(f"Enter values for row {i + 1} (use 0 for empty spaces): ")
    sudoku_puzzle.append([int(num) for num in row])

# Solve the Sudoku puzzle
if solve_sudoku(sudoku_puzzle):
    print("Solved Sudoku:")
    print_sudoku(sudoku_puzzle)
else:
    print("No solution exists.")