from policy_hill_climbing_agent import phc_agent
from random_agent import random_agent
from human_agent import human_agent
from ttt import ttt
from MiniMax import MiniMax
import pickle

#Select player 1
player1 = random_agent(0)
player4 = random_agent(1)
# player2 = random_agent(1)
# player1 = human_agent(0)
# player2 = human_agent(1)
player2 = phc_agent(1)
player3 = MiniMax(1)


#Run it
score = [0, 0, 0]
for i in range(1000):
    game2 = ttt(player3, player1)
    winner = game2.play()
    score[winner] += 1
    # print(score)

    if i % 10 == 0:
        print("Loading", (i*100)/1000, "%")

print('Final score', score)
