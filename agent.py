# This is the player/agent class
# The only method that MUST be implemented is move
# The only variable that MUST be present is marker
# Everything else can be modified
class agent:

    def __init__(self) -> None:
        #Variables
        self.marker = ''

        # Some parameters the agent might need
        self.Q = None
        self.pi = None
        self.alpha = None
        self.beta = None
        self.gamma = None
        self.decay = None
        
    
    # Return a tuple of coordinates where the player chooses to play
    # Sample output: (0,2) or (1,1)
    def move(self, board):

        # Translate board
        board2 = self.translate_board(board)

        # Find the move
        move = self.select_move(board2)

        # Do the move
        board[move[0],move[1]] = self.marker

        # Calculate
        reward = calculate_reward(board)

        # Update the player
        self.update(move, reward)

        return board
    
    # Get the next move
    def select_move(self, board2):
        return None
    
    # Do the reinforcement learning update step
    def update(self, move, reward):
        return None
    
    # Changes the board for better intepretation
    # Empty spaces: 0
    # This player moves: 1
    # Opponent moves: 2
    def translate_board(self, board):
        board2 = board.copy()
        board2[(board2 ==' ') | (board2 == self.marker)] == 2   # Change opponent moves to 2
        board2[board2 == self.marker] == 1                      # Change this player moves to 1
        board2[board2 == ' '] == 0                              # Change empty spaces to 0
        return board2