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

    if self.isSolved() != True:
      self.cleanupTwins()
      self.solveSolved()

  """
    Checks the state of the sudoku
  """
  def isSolved(self):
    unsolved = 0
    for x, rows in enumerate(self.sudoku):
      for y, cell in enumerate(rows):
        if len(cell) == 0:
          return 'Error'
        elif len(cell) != 1:
          unsolved += 1
    if unsolved > 0:
      return 'Not solved'
    else:
      return True

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

  """
    Tries to find a match where 2 numbers are found
    at 2 identical cells in a row/block/column
  """
  def cleanupTwins(self):
    # lookup
    for name, blocks in self.relation.iteritems():
      for row, block in enumerate(blocks):
        twins = [[] for x in range(10)] # twins[x][] = [cell1, cell2]
        for x in range(1, 10):
          found = []
          for cell in block:
            if x in self.sudoku[cell[0]][cell[1]]:
              found.append([cell[0], cell[1]])
          if len(found) == 2:
            twins[x].append(found)
        # cleanup
        for x in range(1, 10):
          for xItem in twins[x]:
            for y in range(x + 1, 10):
              for yItem in twins[y]:
                if xItem == yItem:
                  for clearBlock in xItem:
                    for z in range(1, 10):
                      if x == z or y == z or \
                          not z in self.sudoku[clearBlock[0]][clearBlock[1]]:
                        continue
                      self.sudoku[clearBlock[0]][clearBlock[1]].remove(z)