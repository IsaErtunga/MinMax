import math

class State(object):

    # 1 = O, -1 = X 
    human = 'O'
    computer = 'X'

    #Score for Min-Max algorithm
    score = int()

    """
    Initializes starting state
    [[0, 0, 0]
     [0, 0, 0]
     [0, 0, 0]]
    """
    def __init__(self, depth = 0, leafIndex = 0):
        self.state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ]
        
        if depth == 0:
            self.leafAmount = 9
        elif depth ==1:
            self.leafAmount = 8
        elif depth == 2:
            self.leafAmount = 7
        elif depth == 3:
            self.leafAmount = 6
        elif depth == 4:
            self.leafAmount = 5
        elif depth == 5:
            self.leafAmount = 4
        elif depth == 6:
            self.leafAmount = 3
        elif depth == 7:
            self.leafAmount = 2
        elif depth == 8:
            self.leafAmount = 1
        elif depth == 9:
            self.leafAmount = 0

        self.leaves = list()
        self.depth = depth
        self.leafIndex = leafIndex
        self.stateID = [depth, leafIndex]
        self.parent = self
        self.playerTurn = human


    def addLeaf(self, leaf):
        self.leaves.append(leaf)
        leaf.parent = self


    def printState(self):
        print(self.state)


    def printStateTree(self, node):
        print("leaf ID and parent ID", node.stateID, node.parent.stateID)
        print("\n", node.state)
        
        if len(node.leaves) == 0:
            print("No leaves")
            return
  
        for i in range(len(node.leaves)):
            child = node.leaves[i]
            node.printStateTree(child)
    """
    Function that tests if the current state is in fact a winning state. 
    Can win if a player has three marks on columns, rows or the diagonal
    """
    def winningState(self, player):
        winningStates = [
            [self.state[0][0], self.state[0][1], self.state[0][2]],
            [self.state[1][0], self.state[1][1], self.state[1][2]],
            [self.state[2][0], self.state[2][1], self.state[2][2]],
            [self.state[0][0], self.state[1][0], self.state[2][0]],
            [self.state[0][1], self.state[1][1], self.state[2][1]],
            [self.state[0][2], self.state[1][2], self.state[2][2]],
            [self.state[0][0], self.state[1][1], self.state[2][2]],
            [self.state[2][0], self.state[1][1], self.state[0][2]],
        ]
        
        if [player, player, player] in winningStates:
            return True
        else:
            return False
    
    
    """ 
    Function that sets score variable depending
    on which player won.

    1 = human wins
    -1 = computer wins
    0 = draw
    """
    def checkGameScore(self):
        if self.winningState(self.human):
            return score = 1
        
        elif self.winningState(self.computer):
            return score = -1
        
        else:
            return score = 0



    def gameOver(self, state):
        return self.winningState(state, human) or self.winningState(state, computer)


    """
    Returns list of empty cells with given coordinates
    """
    def emptyCell(self):
        emptyCells = list()

        for row in range(len(self.state)):
            for column in range(len(self.state)):
                if self.state[row][column] == 0:
                    emptyCells.append([row,column])
        
        return emptyCells


    def acceptableMove(self, row, column):
        if [row, column] in self.emptyCell():
            return True
        else:
            return False

    def movePiece(self, player, row, column):
        if self.acceptableMove(row, column):
            self.state[row][column] = player
            return True
        else:
            return False

    # Maximize for human
    def max(self):
        maxValue = -2
        
        row = None
        column = None

        result = self.checkGameScore()

        if result == 1:
            return (1, 0, 0)
        
        elif result == -1:
            return (-1, 0, 0)

        elif result == 0:
            return (0, 0, 0)
        
        for i in range(0, 3):
            for j in range(0, 3):
                if self.state[i][j] == 0:
                    # On the empty field player 'O' makes a move and calls Min
                    # That's one branch of the game tree.
                    self.state[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    # Fixing the maxv value if needed
                    if m > maxValue:
                        maxValue = m
                        row = i
                        column = j
                    # Setting back the field to empty
                    self.current_state[i][j] = '.'
        return (maxValue, row, column)
    



    # Player 'X' is min, in this case AI
    def min(self):

        # We're initially setting it to 2 as worse than the worst case:
        minv = 2

        row = None
        column = None

        result = self.checkGameScore()

        if result == -1:
            return (-1, 0, 0)
        elif result == 1:
            return (1, 0, 0)
        elif result == 0:
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.state[i][j] == 0:
                    self.state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        row = i
                        column = j
                    self.current_state[i][j] = 0

        return (minv, qx, qy)



human = 1
computer = -1


def createTree(root):
    # Root node (state)
    row = int()
    column = int()

    if(root.depth == 2):
        print("No leaves from createTree function")
        return

    i = 0
    for index in range(root.leafAmount):
        
        row = math.floor(i/3)
        column = math.floor(i % 3)

        leaf = State(root.depth + 1, index)
        leaf.movePiece(human, row, column)
        root.addLeaf(leaf)
        createTree(leaf)
        i += 1

    state.printStateTree(state)

