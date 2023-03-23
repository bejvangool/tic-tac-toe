# Refrence: https://www.geeksforgeeks.org/finding-optimal-move-in-tic-tac-toe-using-minimax-algorithm-in-game-theory/
import random
import numpy as np

def check_winner(board, player):
    """Check if the specified player has won the game."""
    # Check rows
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
    # Check columns
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    """Check if the game has ended in a draw."""
    return all(board[i][j] != ' ' for i in range(3) for j in range(3)) and not check_winner(board,'X') and not check_winner(
        board, 'O')

# This is the player/agent class
# The only method that MUST be implemented is move
# The only variable that MUST be present is marker
# Everything else can be modified
class MiniMax:

    def __init__(self,id):
        self.id = id
        # Variables
        self.marker = ''

    # Return a tuple of coordinates where the player chooses to play
    # Sample output: (0,2) or (1,1)
    def move(self, board):

        # Find the move
        move = self.select_move(board)

        # Do the move
        board[move[0], move[1]] = self.marker

        return board

    def select_move(self, board):
        """Choose the best move for the AI player using the minimax algorithm."""
        player = self.marker
        opponent = 'x'
        if player == 'x': opponent = 'o'
        best_move = None
        best_score = -np.Inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    score = self.minimax(board, False, player, opponent)
                    board[i][j] = ' '
                    if score is not None and score > best_score:
                        best_score = score
                        best_move = (i, j)

        return best_move

    def minimax(self, board, is_maximizing, player, opponent):
        """Recursively search the game tree using minimax."""
        if check_winner(board, player):
            return 1
        elif check_winner(board, opponent):
            return -1
        elif check_draw(board):
            return 0

        if is_maximizing:
            best_score = -np.Inf
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = player
                        score = self.minimax(board, False, player, opponent)
                        board[i][j] = ' '
                        best_score = max(best_score, score)
        else:
            best_score = +np.Inf
            for z in range(3):
                for k in range(3):
                    if board[z][k] == ' ':
                        board[z][k] = player
                        score = self.minimax(board, False, player, opponent)
                        board[z][k] = ' '
                        best_score = min(best_score, score)

        return best_score