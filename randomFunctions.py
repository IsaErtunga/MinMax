
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


