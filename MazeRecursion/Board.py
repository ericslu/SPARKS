class Board:

    # Constructor
    # NOTE: Input MUST be a 2-D List
    def __init__(self, board):
        self.board = board
        self.isValid()
        self.S = self.get('s')
        self.E = self.get('e')
        self.posX = (self.S)[0]
        self.posY = (self.S)[1]
        self.pos = [self.posX, self.posY]


    # Checks if board is a valid maze (a rectangle)
    # Checks if board has a Start and an End
    # NOTE: Does not check if board is solvable
    def isValid(self):
        # Checks if board is empty
        if (not any(self.board)):
            raise TypeError('Not a valid board: Board is empty')
        
        # Checks if board has straight edges
        row_len = len(self.board[0])
        for row in range(len(self.board)):
            if (len(self.board[row]) != row_len):
                raise TypeError('Not a valid board: Board is jagged')
        
        # Check for Start
        if (not (any('s' in sub_list for sub_list in self.board) or
                 any('S' in sub_list for sub_list in self.board))):
            raise TypeError('Not a valid board: Does not have a Start')
        
        # Check for End
        if (not (any('e' in sub_list for sub_list in self.board) or
                 any('E' in sub_list for sub_list in self.board))):
            raise TypeError('Not a valid board: Does not have an End')

    # toString
    def __str__(self):
        return_s = ' '
        # Add column indexes
        for col in range(len(self.board[0])):
            return_s += ' ' + str(col)
        return_s += '\n'

        # Print rows
        for row in range(len(self.board)):
            # Add row indexes
            return_s += str(row) + ' '
            for col in range(len(self.board[row])):
                return_s += str(self.board[row][col]) + ' '
            return_s += '\n'
        
        return return_s

    # Checks if Inputted Index exists and isnt a wall
    def checkIndex(self, x: int, y: int) -> bool:
        return (x < (len(self.board[0])) 
        and y < (len(self.board))
        and self.board[x][y] != '#' 
        and self.board[x][y] != '0')
#        return ((x < (len(self.board[0])) and (y < (len(self.board))))
#        and ((self.board[x][y] != '#') and (self.board[x][y] != '0')))
    
    # Change value in index
    def put(self, startX, startY, val):
        if (self.checkIndex(startX, startY)):
            self.board[startX][startY] = val
        else:
            raise IndexError('Inputted Coordinates are Out of Range')

    # Check value
    def check(self, startX, startY):
        if (self.checkIndex(startX, startY)):
            return self.board[startX][startY]
        else:
            raise IndexError('Inputted Coordinates are Out of Range')

    # Remove value
    def remove(self, x, y):
        if (self.checkIndex(x, y)):
            coords = [x, y]
            if (coords == self.S):
                self.board[x][y] = 'S'
            elif (coords == self.E):
                self.board[x][y] = 'E'
            else:
                self.board[x][y] = ' '

    # Get index of value
    def get(self, val):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if (self.board[row][col]).upper() == val.upper():
                    coords = [row, col]
                    return coords
        raise IndexError('Value does not exist on board')

    # Get position
    def getPos(self):
        return self.pos

    # Get x position
    def getPosX(self):
        return self.posX

    # Get y position
    def getPosY(self):
        return self.posY
    
    # Move cursor
    def move(self, newX, newY):
        if (self.checkIndex(newX, newY)):
 #           self.put(self.board, #self.posX, self.posY, 'O')
#            self.put(self.board, newX, newY, 'X')
            self.posX = newX
            self.posY = newY
            self.pos = [newX, newY]
        else:
            print('Cannot move here')
                
