from policy_hill_climbing_agent import phc_agent
from random_agent import random_agent
from human_agent import human_agent
from ttt import ttt
import pickle

#Select player 1
player1 = random_agent(0)
# player2 = random_agent(1)
# player1 = human_agent(0)
# player2 = human_agent(1)
player2 = phc_agent(1)



#Run it
score = [0,0,0]
for i in range(1000000):
    game = ttt(player1, player2)
    winner = game.play()
    score[winner] += 1
    print(score)
print('Final score', score)