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
        else:
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
* Human player.
"""
def maxValue(state, row, column):
    if gameOver(startingState):
        return evaluateState(state), row, column
    
    # Lower than worst. -inf in book 
    utilityVal = -2 
    for [row, column] in emptyCell(state):
        utilityVal = max(utilityVal, minValue(state, row, column))

    
"""
Computes min value for algorithm
* Computer player.
"""
def minValue(state, row, column):
    if gameOver(startingState):
        return evaluateState(state), row, column

    utilityVal = 2

    for [row, column] in emptyCell(state):
        utilityVal = min(utilityVal, maxValue(state, row, column))

def play():
    player_turn = 'X'
    state = startingState
    while True:
        printBoard(state)


play()