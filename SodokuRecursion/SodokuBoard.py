class SodokuBoard:

  # Instance Variable
  gameBoard = []
  
  # Constructors
  def __init__(self, path):
    self.gameBoard = []
    
    # process file line by line
    with open(path) as f:
        # read rows
        for i in range(9):
            self.gameBoard.append([])
            line = f.readline()
            # read columns
            for j in range(9):
                self.gameBoard[i].append(line[j])


  # isValid
  def isValid(self) -> bool:
    data_check = self.checkData()
    row_check = self.checkRows()
    column_check = self.checkColumns()
    square_check = self.checkSquares()

    return ((data_check and row_check) and (column_check & square_check))

  # isSolved
  def isSolved(self) -> bool:
    if (not self.isValid()):
        return False

    # Now we know the board is valid
    boardMap = {}

    for i in range(len(self.gameBoard)):
        for j in range(len(self.gameBoard[0])):
            currentChar = self.gameBoard[i][j]
            if currentChar in boardMap:
                boardMap[currentChar] += 1
            elif (currentChar == "."):
              return False
            else:
                boardMap[currentChar] = 1
                
    # We now have a map that only has numeric keys. 
    # We can now check if each key is equal to 9
    # (There's 9 instances of each number in 1-9 on the board)
    keySet = boardMap.keys()
    for key in keySet:
        if (boardMap[key] != 9):
            return False

    return True

  # checkData: This method checks that all items in grid are either 1-9 or a .
  def checkData(self) -> bool:
    for i in range(len(self.gameBoard)):
        for j in range(len(self.gameBoard[0])):
            # Get char value at this index of gameBoard
            currentChar = self.gameBoard[i][j]
            # Check if it is a period or a number character between 1-9
            if (not ((str(currentChar).isdigit()) or (currentChar == "."))):
                return False
    return True

  # checkRows: This method checks each row to find duplicates (excluding spaces)
  def checkRows(self) -> bool:
    # Check every row
    for i in range(len(self.gameBoard)):
        # Create set to check for duplicates on each row
        rowSet = set()

        for j in range(len(self.gameBoard[0])):
            currentChar = self.gameBoard[i][j]
            # if the current char is not in the set, add it
            if (not (currentChar in rowSet)):
                rowSet.add(currentChar)
            # Otherwise, if it isn't a space, then it is a duplicat
            elif (currentChar != "."):
                return False
    return True
        
  # checkColumns: This method checks each column to find duplicates (excluding spaces)
  def checkColumns(self) -> bool:
    for i in range(len(self.gameBoard)):
        # Create set to check for duplicates on each column
        columnSet = set()

        # Iterate through every array in gameBoard at index i
        for j in range(len(self.gameBoard[0])):
            currentChar = self.gameBoard[j][i]
            # if the current char is not in the set, add it
            if (not (currentChar in columnSet)):
                columnSet.add(currentChar)
            # Otherwise, if it isn't a space, then it is a duplicat
            elif (currentChar != "."):
                return False
    return True

  def miniSquare(self, spot):
    # I dont feel like doin the math today ngl
    rowStarters = [0, 0, 0, 3, 3, 3, 6, 6, 6]
    columnStarters = [0, 3, 6]
    mini = [['','',''], ['','',''], ['','','']]
    for r in range(3):
        for c in range(3):
          mini[r][c] = self.gameBoard[rowStarters[spot - 1] + r][columnStarters[(spot - 1) // 3] + c]
    return mini

  # Checks each 3x3 grid of squares
  def checkSquares(self) -> bool:
    for squareIndex in range(1, 10):
        currentSquare = self.miniSquare(squareIndex)
        squareSet = set()

        # Iterate through square row
        for i in range(len(currentSquare)):
            for j in range(len(currentSquare[0])):
                currentChar = currentSquare[i][j];
                # if the current char is not in the set, add it
                if (not (currentChar in squareSet)):
                    squareSet.add(currentChar)
                elif (currentChar != "."):
                    return False
    return True

  def place(self, row, column, val):
    self.gameBoard[row][column] = val

  def remove(self, row, column):
    self.gameBoard[row][column] = "."

  # toString
  def __str__(self):
    boardStr = ""
    
    for i in range(len(self.gameBoard)):
        for j in range(len(self.gameBoard[0])):
            boardStr += str(self.gameBoard[i][j])
            # If we're on a 3rd char, separate the 'squares'
            if (((j + 1) % 3) == 0):
                boardStr += ' '
            # If we're on the 9th char, add new line
            if (((j + 1) % 9) == 0):
                boardStr += '\n'
            # If we're on a 3rd line, add another line to seperate 'squares'
        if (((i + 1) % 3) == 0):
            boardStr += '\n'
    return boardStr

  def solve(self):
    # Conditions
    if (not self.isValid()):
      return False
    # Base Case
    if (self.isSolved()):
      return True
    else:
      # Recursive Cases
      for r in range(9):
        for c in range(9):
          for val in range(1, 10):
            if (self.gameBoard[r][c] == '.'):
              self.place(r, c, str(val))
              if (self.solve()):
                return True
              self.remove(r, c)
  
