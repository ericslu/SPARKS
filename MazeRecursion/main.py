
import sys, time
from Board import Board
board = Board([['#','#','#','#','#'], 
               ['#','S','#','E','#'], 
               ['#',' ',' ',' ','#'], 
               ['#',' ','#',' ','#'], 
               ['#','#','#','#','#']] )

def updateData(board, x, y):
  board.put(x, y, '0')
  board.posX = x
  board.posY = y
  board.pos = [x, y]
  print(board)

def solve(board, x, y):
  # Condition
  if (board.checkIndex(x, y)):
    # Base Case
    if (board.E == board.pos):
      sys.exit()
    else:
      # Recursive cases
      # Moving right
      solve(board, x, y + 1)
      # Moving left
      solve(board, x, y - 1)
      # Moving down
      solve(board, x + 1, y)
      # Moving up
      solve(board, x - 1, y)

solve(board, 1, 1)
