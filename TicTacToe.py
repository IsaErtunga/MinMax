"""
Tic-Tac-Toe game
"""

# Human score = 1
# Comp score = -1
human = 'X'
computer = 'O'

startingState = [['.','.','.'],
                 ['.','.','.'],
                 ['.','.','.']]


def printBoard(state):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(state[i][j]), end=" ")
            print()
        print()

"""
Function that tests if the current state is in fact a winning state. 
Can win if a player has three marks on columns, rows or the diagonal
"""
def evaluateState(state):
        winningStates = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        
        if ['X', 'X', 'X'] in winningStates:
            return 1
        elif ['O', 'O', 'O'] in winningStates:
            return -1
        elif emptyCell(state) == 0:
            return 0

     
""" 
Function that sets score variable depending
on which player won.
1 = human wins
-1 = computer wins
0 = draw
"""
def checkGameScore():
    if evaluateState(human):
        score = 1
        return score
    
    elif evaluateState(computer):
        score = -1
        return score
    
    else:
        score = 0
        return score


def gameOver(state):
    return evaluateState(state) or evaluateState(state)


"""
Returns list of empty cells with given coordinates
"""
def emptyCell(state):
    emptyCells = list()
    for row in range(len(state)):
        for column in range(len(state)):
            if state[row][column] == '.':
                emptyCells.append([row,column])
    
    return emptyCells


def acceptableMove(state, row, column):
    if [row, column] in emptyCell(state):
        return True
    else:
        return False


def movePiece(state, player, row, column):
    if acceptableMove(state, row, column):
        state[row][column] = player
        return True
    else:
        return False

"""
Computes max value for algorithm. 
* Human player. 'X' 
"""
def maxValue(state):

    utilityValue = -2

    row = 0
    column = 0

    evaluationScore = evaluateState(state)

    if evaluationScore == 1:
        return 1
    elif evaluationScore == -1:
        return -1
    elif evaluationScore == 0:
        return 0

    emptyCells = emptyCell(state)
    
    for [row, column] in emptyCells:
        movePiece(state, human, row, column)
        utilityValue = max(utilityValue, minValue(state))

        state[row][column] = '.'
    print(utilityValue)
    return utilityValue
"""
Computes min value for algorithm
* Computer player. 'O'
"""
def minValue(state):

    utilityValue = 2

    row = 0
    column = 0

    evaluationScore = evaluateState(state)

    if evaluationScore == 1:
        return 1
    elif evaluationScore == -1:
        return -1
    elif evaluationScore == 0:
        return 0

    emptyCells = emptyCell(state)
    for [row, column] in emptyCells:
        movePiece(state, computer, row, column)
        utilityValue = min(utilityValue, maxValue(state))
        state[row][column] = '.'
    print(utilityValue)
    return utilityValue
    

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



def play():
    player_turn = human
    state = startingState
    minMaxScore = int()
   
    while True:
        printBoard(state)
        result = evaluateState(state)

        if player_turn == human:
            while True:
                minMaxScore = minimax(state, human)
                row = int(input('Insert the X coordinate: '))
                column = int(input('Insert the Y coordinate: '))
                
                if acceptableMove(state, row, column):
                    movePiece(state, human, row, column)
                    player_turn = computer
                    break
                else:
                    print("bad move")

        else:
            minMaxScore = minimax(state, computer)
            print(minMaxScore)
            
play()