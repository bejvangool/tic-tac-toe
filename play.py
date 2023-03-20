from random_agent import random_agent
from human_agent import human_agent
from ttt import ttt

#Select player 1
player1 = random_agent()
player2 = random_agent()
# player1 = human_agent()
# player2 = human_agent()

#Initialize game
game = ttt(player1, player2)

#Run it
game.play()