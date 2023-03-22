import random

# This is the player/agent class
# The only method that MUST be implemented is move
# The only variable that MUST be present is marker
# Everything else can be modified
class random_agent:

    def __init__(self, id):
        #Variables
        self.id = id
        self.marker = ''
    
    # Return a tuple of coordinates where the player chooses to play
    # Sample output: (0,2) or (1,1)
    def move(self, board):

        # Find the move
        move = self.select_move(board)

        # Do the move
        board[move[0],move[1]] = self.marker

        return board
    
    # Get the next move
    def select_move(self, board):
        
        legal_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    legal_moves.append((i,j))
        move = random.randint(0,len(legal_moves)-1)
        move = legal_moves[move]
        return move
    