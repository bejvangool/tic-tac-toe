import random

# This is the player/agent class
# The only method that MUST be implemented is move
# The only variable that MUST be present is marker
# Everything else can be modified
class human_agent:

    def __init__(self):
        #Variables
        self.marker = ''
        self.all_moves = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    
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
        print(f"What\'s your move, {self.marker}?       hint: pick a number 1-9")

        while(True):
            
            move_idx = int(input()) - 1
            move = self.all_moves[move_idx]

            try:
                if board[move[0], move[1]] == ' ':
                    break
            except:
                None
            print('Illegal move, please try again')

        return move
    