import random
import numpy as np
import copy

# If state not in Q/pi/legal
    # Check legal moves
    # Add to Q/pi/legal
# Pick a move from legal moves

PRINT = False

class phc_agent:

    def __init__(self, id):
        self.id = id
        self.marker = ''

        self.Q = {}
        self.pi = {}
        self.legal = {}
        self.all_moves = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

        self.alpha = 0.8
        self.expl = 0
        self.gamma = 0.9
        self.delta = 0.7
        self.decay = 0.999


    # Return a tuple of coordinates where the player chooses to play
    # Sample output: (0,2) or (1,1)
    def move(self, board):

        # Translate board
        board_translated = self.translate_board(board)
        state = self.board_to_state(board_translated)
        

        # Find the move
        move = self.select_move(state)
        move_idx = self.legal[state][move]
        coord = self.all_moves[move_idx]

        # Do the move
        board[coord[0],coord[1]] = self.marker
        board_translated[coord[0],coord[1]] = 1

        # Calculate
        reward = self.calculate_reward(board_translated)
        state2 = self.board_to_state(board_translated)
        # Update the player
        self.update(state, state2, move, reward)

        return board
    
    def select_move(self, state):

        # See if we explore
        num = random.uniform(0,1)
        if num < self.expl:

            move = random.randint(0,len(self.legal[state])-1)

        # Otherwise pick a pi with probability dist
        else:
            state_pi = self.pi[state]
            totalp = 0
            num2 = random.uniform(0,1)
            for i in range(len(state_pi)):
                totalp += state_pi[i]
                if totalp >= num2:
                    move = i
                    if PRINT:
                        print(move, state_pi)
                    break
        
        return move

    # Find the reward after the last move
    def calculate_reward(self, board):
        reward = 0

        sums = []
        # Rows
        sums.append(board[0,:].sum())
        sums.append(board[1,:].sum())
        sums.append(board[2,:].sum())
        #Columns
        sums.append(board[:,0].sum())
        sums.append(board[:,1].sum())
        sums.append(board[:,2].sum())
        # Diagonals
        sums.append(board[0,0] + board[1,1] + board[2,2])
        sums.append(board[2,0] + board[1,1] + board[0,2])

        if 3 in sums: # Opponent can win in 1 turn
            reward = 1
        elif -2 in sums: # We just won
            reward = -1
        
        return reward


    # Update Q and Pi
    def update(self, state, state2, action, reward):
        
        maxQ = max(self.Q[state2])
        self.Q[state][action] = (1-self.alpha) * self.Q[state][action] + self.alpha*(reward+self.gamma*maxQ)

        maxA = self.Q[state].index(max(self.Q[state]))

        if maxA == action:
            x = self.delta
        else:
            x = -self.delta/(9-1)
        
        self.pi[state][action] = self.pi[state][action]+x

        sumA = sum(self.pi[state])
        # print('before:', self.pi[state])
        self.pi[state] = [max(0, a/sumA) for a in self.pi[state]]
        # print('after:', self.pi[state])

    def translate_board(self, board):
        board2 = np.full([3,3], -1)

        board2[board == self.marker] = 1                        # Change this player moves to 1
        board2[board == ' '] = 0                                # Change empty spaces to 0

        return board2

    
    def board_to_state(self, board):
        state = []
        for i in range(3):
            for j in range(3):
                state.append(board[i,j])
        state = tuple(state)

        # Add this state to Q and Pi if it's not already there
        legal = []
        if state not in self.Q:
            for i in range(9):
                if state[i] == 0:
                    legal.append(i)
            
            n = len(legal)
            if n == 0:
                self.Q[state] = [0]
            else:
                self.legal[state] = legal
                n = len(legal)
                self.Q[state] = [0]*n
                self.pi[state] = [1/n]*n
        
        return state

    # Import previous knowledge
    def import_learnings(self, q, pi, legal):
        self.Q = q
        self.pi = pi
        self.legal = legal
    