import random

class phc_agent:

    def __init__(self):
        self.marker = ''

        self.Q = {}
        self.pi = {}

        self.alpha = 0.6
        self.expl = 0.4
        self.gamma = 0.6
        self.delta = 0.01
        self.decay = 0.999

        self.all_moves = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

    # Return a tuple of coordinates where the player chooses to play
    # Sample output: (0,2) or (1,1)
    def move(self, board):

        # Translate board
        state = self.translate_board(board)

        # Find the move
        move = self.select_move(state)

        # Do the move
        board[move[0],move[1]] = self.marker

        # Calculate
        reward = self.calculate_reward(board)

        # Update the player
        self.update(move, reward)

        return board

    def select_move(self, state):
        # See if we explore
        num = random.uniform(0,1)
        if num < self.expl:
            move = random.randint(0,9)
        # Otherwise pick a pi with probability dist
        else:
            state_pi = self.pi[state]
            totalp = 0
            num2 = random.uniform(0,1)
            for i in range(len(state_pi)):
                totalp += state_pi[i]
                if totalp >= num2:
                    move = self.all_moves[i]

        return move

    def calculate_reward(board):
        
        

    def translate_board(self, board):
        board2 = board.copy()
        board2[(board2 ==' ') | (board2 == self.marker)] == 2   # Change opponent moves to 2
        board2[board2 == self.marker] == 1                      # Change this player moves to 1
        board2[board2 == ' '] == 0                              # Change empty spaces to 0

        state = []
        for i in range(3):
            for j in range(3):
                state.append(board2[i,j])
        state = tuple(state)

        # Add this state to Q and Pi if it's not already there
        if state not in self.Q:
            self.Q[state] = [0]*9
            self.pi[state] = [1/9]*9
        
        return state

    