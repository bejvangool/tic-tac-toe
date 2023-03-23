from policy_hill_climbing_agent import phc_agent
from policy_hill_climbing_agent_greedy import phc_agent_greedy
from random_agent import random_agent
from human_agent import human_agent
from ttt import ttt
import pickle
import time


#Select player 1
# player1 = random_agent(0)
# player2 = random_agent(1)
# player1 = human_agent(0)
# player2 = human_agent(1)
# player1 = phc_agent_greedy(0)
TEACH_P1 = True
# player2 = phc_agent_greedy(1)
player1 = phc_agent(0)
TEACH_P1 = True
player2 = phc_agent(1)

read = False
write = True
file_r = 'phc_bart_scratch.pkl'
file_w = 'phc_bart_scratch.pkl'
epochs = 100

epoch_size = 10000


win_hist = []
tie_hist = []
loss_hist = []
length_history = len(win_hist)

if read:
    try:
        with open(file_r, 'rb') as pick:
            l = pickle.load(pick)
            player2.import_learnings(l['q'], l['pi'], l['legal'])
            win_hist = l['win_hist']
            tie_hist = l['tie_hist']
            loss_hist = l['loss_hist']
            length_history = len(win_hist)
            if TEACH_P1:
                player1.import_learnings(l['q'], l['pi'], l['legal'])
    except:
        length_history = 0
        print('did not work to read')
        pass

#Run it
for j in range(epochs):
    score = [0,0,0]
    tic = time.perf_counter()
    for i in range(epoch_size):
        game = ttt(player1, player2)
        winner = game.play()
        score[winner] += 1
    #print(f"Downloaded the tutorial in {time.perf_counter() - tic:0.4f} seconds")

    win_hist.append(score[1]/sum(score))
    tie_hist.append(score[2]/sum(score))
    loss_hist.append(score[0]/sum(score))

    print(f'Epoch {length_history + j+1} W percentage: {win_hist[length_history + j]*100}')
    print(f'Epoch {length_history + j+1} T percentage: {tie_hist[length_history + j]*100}')
    print(f'Epoch {length_history + j+1} L percentage: {loss_hist[length_history + j]*100}')
    print()

if write:
    with open(file_w, 'wb') as out:
        q = player2.Q
        pi = player2.pi
        legal = player2.legal
        l = {'q': q, 'pi': pi, 'legal': legal, 'win_hist': win_hist, 'tie_hist': tie_hist, 'loss_hist': loss_hist}
        pickle.dump(l, out, pickle.HIGHEST_PROTOCOL)