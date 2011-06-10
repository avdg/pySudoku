import sys
import sudokuSolver

"""
  Main function

  Executes testdata
"""
def main():
  sudoku1 = [
    [8, 9, 0, 1, 0, 4, 0, 2, 0],
    [0, 0, 1, 0, 6, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 9, 5, 1],
    [0, 0, 0, 8, 9, 0, 3, 4, 0],
    [3, 0, 0, 7, 0, 0, 1, 0, 0],
    [0, 5, 8, 0, 3, 6, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 5, 0, 4],
    [6, 0, 7, 5, 0, 0, 0, 0, 0],
    [4, 8, 0, 0, 0, 9, 0, 3, 6],
  ]
  sudoku2 = [
    [0, 8, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 2],
    [1, 0, 0, 0, 0, 9, 0, 0, 0],
    [8, 0, 5, 0, 4, 0, 0, 0, 7],
    [0, 0, 0, 0, 3, 1, 0, 0, 4],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [3, 2, 0, 0, 8, 0, 1, 5, 0],
  ]
  sudoku3 = [
    [6, 0, 0, 8, 5, 0, 9, 3, 1],
    [3, 5, 8, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 2],
    [0, 0, 0, 0, 1, 8, 3, 9, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 8, 3, 0, 6, 0, 1, 0, 0],
    [8, 3, 0, 0, 9, 0, 0, 0, 0],
    [0, 6, 0, 0, 8, 0, 2, 1, 9],
    [1, 0, 9, 0, 0, 5, 0, 0, 3],
  ]
  sudoku4 = [
    [0, 0, 7, 0, 1, 3, 0, 0, 6],
    [0, 2, 0, 0, 9, 0, 0, 7, 0],
    [0, 3, 0, 8, 0, 0, 0, 0, 9],
    [0, 4, 3, 1, 0, 0, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 4, 3, 5, 0],
    [0, 0, 0, 0, 0, 1, 0, 9, 0],
    [0, 1, 0, 0, 7, 0, 0, 8, 0],
    [5, 0, 0, 6, 4, 0, 7, 0, 0],
  ]
  solveSudoku(sudoku1)
  solveSudoku(sudoku2)
  solveSudoku(sudoku3)
  solveSudoku(sudoku4)

"""
  Solves a sudoku while displaying some basic debug data
"""
def solveSudoku(sudoku):
  outputSudoku(sudoku)
  grid = sudokuSolver.SudokuSolver()
  grid.setSudoku(sudoku)
  grid.solve()
  print
  outputSudoku(grid.getSudoku())
  print
  print str(grid.sudoku)
  print str(grid.isSolved())
  print
  print '--------------------------------------------------------------------------------'
  print

"""
  Printing a 2d sudoku
"""
def outputSudoku(sudoku):
  for rows in sudoku:
    for columns in rows:
       sys.stdout.write(str(columns))
    print

if __name__ == '__main__':
  main()