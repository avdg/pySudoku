import sys

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
  solveSudoku(sudoku1)
  solveSudoku(sudoku2)

"""
  Solves a sudoku while displaying some basic debug data
"""
def solveSudoku(sudoku):
  outputSudoku(sudoku)
  grid = SudokuSolver()
  grid.setSudoku(sudoku)
  grid.solve()
  print
  outputSudoku(grid.getSudoku())
  print
  print str(grid.sudoku)

"""
  Printing a 2d sudoku
"""
def outputSudoku(sudoku):
  for rows in sudoku:
    for columns in rows:
       sys.stdout.write(str(columns))
    print

"""
  Specialised in solving sudoku's
"""
class SudokuSolver:
  """
    Constructor
  """
  def __init__(self):
    self.reset()

  """
    Resets the sudoku status for a normal 9x9 grid sudoku
  """
  def reset(self):
    self.sudoku   = [[range(1, 10) for y in range(9)] for x in range(9)]
    self.relation = {
      'rows':    [[[y, x] for y in range(9)] for x in range(9)],
      'columns': [[[x, y] for y in range(9)] for x in range(9)],
      'blocks':  [[[
          int(y / 3) + (int(x / 3) * 3), #expecting int does floor stuff
          (y % 3)    + (x % 3 * 3)
        ] for y in range(9)] for x in range(9)]
    }

  """
    Converts a 2D sudoku to its internal 3D representation
  """
  def setSudoku(self, sudoku):
    self.sudoku = [[range(1, 10) for y in range(9)] for x in range(9)]
    for x, rows in enumerate(sudoku):
      for y, cell in enumerate(rows):
        if cell != 0:
          self.sudoku[x][y] = [cell]

  """
    Converts an internal 3d representation to a 2d sudoku
  """
  def getSudoku(self):
    sudoku = [[0] * 9 for x in range(9)]
    for x, rows in enumerate(self.sudoku):
      for y, cell in enumerate(rows):
        if len(cell) == 1:
          sudoku[x][y] = cell[0]
    return sudoku

  """
    Solve algoritme
  """
  def solve(self):
    self.solveSolved()

  """
    Scraps leftovers in grid:
      the numbers that are already used as a solution
  """
  def solveSolved(self):
    solved = False
    while not solved:
      solved = True
      for x, rows in enumerate(self.sudoku):
        for y, cell in enumerate(rows):
          if len(cell) == 1 and self.markCellSolved(x, y):
            solved = False

  """
    Returns true if the cell occurs in the given relation block
  """
  def cellInBlockRow(self, x, y, blockKey, blockRow):
    for cell in self.relation[blockKey][blockRow]:
      if [x, y] == cell:
        return True
    return False

  """
    Cleans up surrounding fields by eliminating the number in other fields in
      the same blocks
  """
  def markCellSolved(self, x, y):
    if len(self.sudoku[x][y]) != 1:
      return False
    hit = False
    number = self.sudoku[x][y][0]
    # lookup
    for name, blocks in self.relation.iteritems():
      for row, block in enumerate(blocks):
        if self.cellInBlockRow(x, y, name, row):
          # cleanup
          for cleanCell in self.relation[name][row]:
            if cleanCell[0] == x and cleanCell[1] == y:
              continue
            if number in self.sudoku[cleanCell[0]][cleanCell[1]]:
              self.sudoku[cleanCell[0]][cleanCell[1]].remove(number)
              hit = True
    return hit

if __name__ == '__main__':
  main()