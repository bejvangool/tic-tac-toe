import numpy as np
import random

PRINT = True

class ttt:
    
    def __init__(self, player1, player2):
        # Initialize empty board
        self.board = np.full([3,3], ' ')
        self.print_board()
        
        # X starts
        self.turn = 0

        # Randomly assign who starts (who is x)
        self.players = self.assign_x_and_o(player1, player2)

        # Completeness
        self.complete = False

        # Variable for the eventual winner
        self.winner = None

    # Simulate the steps of the game
    def play(self):
        while(self.complete == False):
            # Do the next move
            self.move()
            
            # Check for completed game state
            self.check_complete()

            # Switch turn
            self.turn = 1 - self.turn
        
        if PRINT:
            if self.winner == 'tie':
                print('It\'s a tie!')
            else:
                winner = self.players[1-self.turn].marker
                print(f'{winner}\'s win!')

    
    # Complete one move
    def move(self):
        # Pick player who's turn it is
        player = self.players[self.turn]

        # Move is a tuple with the coordinates
        self.board = player.move(self.board)

        if PRINT:
            self.print_board()

    # Randomly assign x and o to two players
    def assign_x_and_o(self, player1, player2):
        rand = random.randint(0,1)              
        if rand == 0:
            player1.marker = 'x'
            player2.marker = 'o'
            return [player1, player2]
        else:
            player2.marker = 'x'
            player1.marker = 'o'
            return [player2, player1]
    

    # Checks board to see if someone has won
    def check_complete(self):

        # Check rows
        self.compare_three(self.board[0,0], self.board[0,1], self.board[0,2])
        self.compare_three(self.board[1,0], self.board[1,1], self.board[1,2])
        self.compare_three(self.board[2,0], self.board[2,1], self.board[2,2])

        # Check columns
        self.compare_three(self.board[0,0], self.board[1,0], self.board[2,0])
        self.compare_three(self.board[0,1], self.board[1,1], self.board[2,1])
        self.compare_three(self.board[0,1], self.board[1,1], self.board[2,1])

        # Ceck diagonals
        self.compare_three(self.board[0,0], self.board[1,1], self.board[2,2])
        self.compare_three(self.board[0,2], self.board[1,1], self.board[2,0])

        # In case of a tie
        if self.complete == False:
            if ' ' not in self.board:
                self.complete = True
                self.winner = 'tie'
        
    # Checks to see if three values are all x or all o
    def compare_three(self, one, two, three):
        if one == 'x' or one == 'o':
            if one == two:
                if two == three:
                    self.complete = True

    # Print the board nicely
    def print_board(self):
        board = self.board
        print(f'[{board[0,0]}][{board[0,1]}][{board[0,2]}]')
        print(f'[{board[1,0]}][{board[1,1]}][{board[1,2]}]')
        print(f'[{board[2,0]}][{board[2,1]}][{board[2,2]}]')
        print('--------------------')    
