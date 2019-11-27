import pygame, TicTacToe as TTT
from pygame.locals import *

pygame.init()


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic Tac Toe')
white = (255, 255, 255)
black = (0, 0, 0)
screen.fill(white)

mouseX = int()
mouseY = int()

def eventHandling(event, state):
    if event.type == pygame.QUIT:
        raise SystemExit
        return 0

    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            print("Up")
        
        elif event.key == pygame.K_DOWN:
            print("Down")

        elif event.key == pygame.K_RIGHT:
            print("Right")

        elif event.key == pygame.K_LEFT:
            print("left")

        elif event.key == pygame.K_SPACE:
            print("Space")
        return 0

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            drawMousePos(mouseX, mouseY, state)
        return 1
            

def drawMousePos(mouseX, mouseY, state):
    if mouseX >= 50 and mouseX <= 200 and mouseY >= 50 and mouseY <= 200:
        state[0][0] = TTT.human
        drawX(positionsX[0])
    
    elif mouseX >= 215 and mouseX <= 380 and mouseY >= 50 and mouseY <= 200:
        state[0][1] = TTT.human
        drawX(positionsX[1])
    elif mouseX >= 395 and mouseX <= 545 and mouseY >= 50 and mouseY <= 200:
        state[0][2] = TTT.human
        drawX(positionsX[2])
    
    elif mouseX >= 50 and mouseX <= 200 and mouseY >= 215 and mouseY <= 380:
        state[1][0] = TTT.human
        drawX(positionsX[3])
    elif mouseX >= 215 and mouseX <= 380 and mouseY >= 215 and mouseY <= 380:
        state[1][1] = TTT.human
        drawX(positionsX[4])
    elif mouseX >= 395 and mouseX <= 545 and mouseY >= 215 and mouseY <= 380:
        state[1][2] = TTT.human
        drawX(positionsX[5])
    elif mouseX >= 50 and mouseX <= 200 and mouseY >= 395 and mouseY <= 545:
        state[2][0] = TTT.human
        drawX(positionsX[6])
    elif mouseX >= 215 and mouseX <= 380 and mouseY >= 395 and mouseY <= 545:
        state[2][1] = TTT.human
        drawX(positionsX[7])
    elif mouseX >= 395 and mouseX <= 545 and mouseY >= 395 and mouseY <= 545:
        state[2][2] = TTT.human
        drawX(positionsX[8])

"""
Draw board lines
"""
def drawCross(left, top, width, height):
    dimensions = (left, top, width, height)
    pygame.draw.rect(screen, black, dimensions)

def drawBoard():
    #Vertical lines
    drawCross(205, 50, 10, 500)
    drawCross(385, 50, 10, 500)
    # Horizontal lines 
    drawCross(50, 205, 500, 10)
    drawCross(50, 385, 500, 10)

"""
Draw Circle
"""
def drawCircle(position):
    radius = 70
    center = (position[0], position[1])
    pygame.draw.circle(screen, black, center, radius, 10)


"""
Draw lines for X's
"""
def drawLine(startX, startY, endX, endY):
    startPos = (startX, startY)
    endPos = (endX, endY)
    pygame.draw.line(screen, black, startPos, endPos, 15)

def drawX(position):
    left = position[0]
    top = position[1]
    width, height = 140, 140
    drawLine(left, top, left + width, top + height)
    drawLine(left + width, top, left, top + height)

"""
Positions for X in squares
(left, top) - values
"""
positionsX = [(50, 55), (230, 55), (410, 55), 
              (50, 230), (230, 230), (410, 230), 
              (50, 405), (230, 405), (410, 405)
              ]

positionsCircle = [(120, 120), (300, 120), (480, 120),
                   (120, 300), (300, 300), (480, 300),
                   (120, 480), (300, 480), (480, 480)
                   ]

"""
Game loop
"""
def play():
    
    playerTurn = TTT.human
    state = TTT.startingState
    
    while True:
        
        drawBoard()
        result = TTT.evaluateState(state)

        pygame.display.update()

        if result == 1:
            print("Computer won")
        elif result == -1:
            print("You won")
        elif result == 0:
            print("Draw")
        
        
        if playerTurn == TTT.human: 
            for event in pygame.event.get():
                res = eventHandling(event, state)
                if res == 1:
                    playerTurn = TTT.computer
                   
                    
        elif playerTurn == TTT.computer:
            (x, y) = TTT.findBestMove(state)
            drawCircle(positionsCircle[(x*3) + y])
            state[x][y] = TTT.computer
            playerTurn = TTT.human

    pygame.quit()

play()
'''
def play():

    playerTurn = human
    state = startingState
   
    while True:
        
        printBoard(state)
        result = evaluateState(state)

        if result == 1:
            print("Computer won")
        elif result == -1:
            print("You won")
        elif result == 0:
            print("Draw")

        if playerTurn == human:
        
            while True:
                row = int(input('Insert the X coordinate: '))
                column = int(input('Insert the Y coordinate: '))
                
                if acceptableMove(state, row, column):
                    state[row][column] = human
                    playerTurn = computer
                    break
                else:
                    print("bad move")

        elif playerTurn == computer:
            (x, y) = findBestMove(state)
            state[x][y] = computer
            playerTurn = human
'''