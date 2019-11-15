class State(object):

    # 1 = X, -1 = O 
    human = 1
    computer = -1

    
    #Score for Min-Max algorithm
    score = int()

    """
    Initializes starting state
    [[0, 0, 0]
     [0, 0, 0]
     [0, 0, 0]]
    """
    def __init__(self):
        self.state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ]
        
    def setState(self):
        self.state[1][0] = self.human
        self.state[1][1] = self.human
        self.state[1][2] = self.human

    def printState(self):
        print(self.state)


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
            self.score = 1
        
        elif self.winningState(self.computer):
            self.score = -1
        
        else:
            self.score = 0


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



"""
Tree class creates node for every state. 
"""
class Tree(object):
    def __init__(self, stateID):
        self.state = State()
        self.leaves = list()
        
        # StateID is a 2D array with 2 columns and x rows. Where first column is depth in tree,
        # and the second is the index at the specific leaf
        self.stateID = stateID


    def addChild(self, stateID):
        self.leaves.append(stateID)


    def printTree(self, node):
        print(node.name)
        
        if len(node.leaves) == 0:
            print("No leaves")
            return
  
        for i in range(len(node.leaves)):
            child = node.leaves[i]
            node.printTree(child)


    def printState(self):
        self.state.printState()


    def getState(self):
        return self.state


    def changeState(self):
        self.state.setState()


    def getID(self):
        print(self.stateID)
        return self.stateID


            
        

a = Tree([0, 0])
b = Tree([1, 0])
b.getID()
b.changeState()
a.addChild(b)
state = a.leaves[0]
state.printState()


# for i in range(len(visited)):
#     print(visited[i].name)

# state = State()

# state.setState()
# print(state.winningState(1))
# state.emptyCell()


































'''class Node(object):

    # löv initieras senare
    def __init__(self, value):
        self.value = value
        self.leaves = list()

    def printValues(self):
        print(self.value)
        print(self.leaves)
        return self.value
    




tree = Tree()
tree.insertNode(root, 10, )'''