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
            return -1
        elif ['O', 'O', 'O'] in winningStates:
            return 1
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
        return state
    else:
        return False


def minimax(state, depth, player):
    emptyCells = emptyCell(state)
    depth = len(emptyCells)
    
    evaluationScore = evaluateState(state)

    if evaluationScore == 1:
        return evaluationScore
    elif evaluationScore == -1:
        return evaluationScore
    elif evaluationScore == 0:
        return evaluationScore

    if len(emptyCells) == 0:
        return


    if player == computer:
        maxUtility = -2
        for i in range (0,3):
            for j in range (0,3):
                if state[i][j] == '.':
                    state[i][j] = computer
                    newUt = minimax(state, depth + 1, human)
                    if (newUt == None):
                        return
                    bestUtility = max(maxUtility, newUt)
                    state[i][j] = '.'
        return bestUtility
    
    elif player == human:
        minUtility = 2
        for i in range (0,3):
            for j in range (0,3):
                if state[i][j] == '.':
                    state[i][j] = human
                    newUt = minimax(state, depth + 1, human)
                    if (newUt == None):
                        return
                    bestUtility = min(minUtility, newUt) 
                    state[i][j] = '.'
                    
        return bestUtility

def findBestMove(state):
    bestVal = -2
    row = -1
    column = -1
    emptyCells = emptyCell(state)
    for i in range (0,3):
        for j in range (0,3):
            if state[i][j] == '.':
                state[i][j] = computer
                moveVal = minimax(state, 0, computer)
                state[i][j] = '.'
                if  moveVal > bestVal:
                    row = i
                    column = j
                    bestVal = moveVal
    return (row, column)

def play():
    
    
    state = startingState
    state[0][0] = human    
    state[0][2] = human 
    state[1][2] = human 
    state[0][1] = computer 
    state[1][0] = computer 
    state[1][1] = computer 
    
    print(findBestMove(state)) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''player_turn = human
    state = startingState
    minMaxScore = int()
   
    while True:
        
        printBoard(state)
        result = evaluateState(state)

        if result == 1:
            print("Computer won")
        elif result == -1:
            print("You won")
        elif result == 0:
            print("Draw")

        if player_turn == human:
        
            while True:
                
                (state, minScore, x, y) = minValue(state)
                print("Recommended move: ", x, "+", y)
                row = int(input('Insert the X coordinate: '))
                column = int(input('Insert the Y coordinate: '))
                
                if acceptableMove(state, row, column):
                    state = movePiece(state, human, row, column)
                    player_turn = computer
                    break
                else:
                    print("bad move")

        elif player_turn == computer:
            (state, maxScore, x, y) = maxValue(state)
            print(x,y)
            if acceptableMove(state, x, y):
                    state = movePiece(state, computer, x, y)
            player_turn = human'''
            
play()