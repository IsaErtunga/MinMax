
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

 
"""
Computes max value for algorithm. 
* Computer player. 'O' 
"""
def maxValue(state):

    utilityValue = -2
    evaluationScore = evaluateState(state)

    if evaluationScore == 1:
        return (state, 1, -1, -1)
    elif evaluationScore == -1:
        return (state, -1, -1, -1)
    elif evaluationScore == 0:
        return (state, 0, -1, -1)

    row = 0
    column = 0
    newRow = None
    newColumn = None
    emptyCells = emptyCell(state)

    for i in range (0, 3):
        for j in range (0, 3):
            if state[i][j] == '.':
                state[i][j] = computer
                (state, minUtility, row, column) = minValue(state)
                
                if minUtility > utilityValue:
                    utilityValue = minUtility
                    newRow = i
                    newColumn = j
                state[i][j] = '.'

    return (state, utilityValue, newRow, newColumn)


"""
Computes min value for algorithm
* Human player. 'X'
"""
def minValue(state):

    utilityValue = 2
    evaluationScore = evaluateState(state)

    if evaluationScore == 1:
        return (state,1, -1, -1)
    elif evaluationScore == -1:
        return (state,-1, -1, -1)
    elif evaluationScore == 0:
        return (state,0, -1, -1)

    row = 0
    column = 0
    newRow = None
    newColumn = None
    emptyCells = emptyCell(state)

    for i in range (0, 3):
        for j in range (0, 3):
            if state[i][j] == '.':
                state[i][j] = human
                (state, maxUtility, row, column) = maxValue(state)
        
                if (maxUtility < utilityValue):
                    utilityValue = maxUtility
                    newRow = i
                    newColumn = j
                state[i][j] = '.'

    return (state, utilityValue, newRow, newColumn)
    




"""
Minimax from youtube video
"""

def minimax(state, player):
    emptyCells = emptyCell(state)
    depth = len(emptyCells)
    
    if depth == 0 or evaluateState(state) == 1 or evaluateState(state) == -1 or evaluateState(state) == 0:
        return evaluateState(state)

    if player == human:
        maxUtility = -2
        for [row, column] in emptyCells:
            state[row][column] = human
            newUtility = minimax(state, computer)
            print(type(maxUtility), type(newUtility))
            maxUtility = max(maxUtility, newUtility)
            state[row][column] = '.'
        return maxUtility
    
    else:
        minUtility = 2
        for [row, column] in emptyCells:
            state[row][column] = computer
            newUtility = minimax(state, human)
            minUtility = min(minUtility, newUtility)
            state[row][column] = '.'
        return minUtility