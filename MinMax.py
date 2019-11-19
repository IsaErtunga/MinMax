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
            score = 1
            return score
        
        elif self.winningState(self.computer):
            score = -1
            return score
        
        else:
            score = 0
            return score



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


