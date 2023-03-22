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

read = True
write = True
file = 'phc_1.pkl'
epochs = 1
epoch_size = 10


history = []

if read:
    try:
        with open(file, 'rb') as pick:
            l = pickle.load(pick)
            player2.import_learnings(l['q'], l['pi'], l['legal'])
            history = l['history']
            length_history = len(history)
    except:
        print('did not work to read')
        pass

#Run it
for j in range(epochs):
    score = [0,0,0]
    for i in range(epoch_size):
        game = ttt(player1, player2)
        winner = game.play()
        score[winner] += 1
    print(score)
    print(score[1])
    print(sum(score))
    history.append(score[1]/sum(score))
    print(f'Epoch {j+1} win percentage: {history[length_history + j]*100}')

if write:
    with open(file, 'wb') as out:
        q = player2.Q
        pi = player2.pi
        legal = player2.legal
        l = {'q':q, 'pi':pi, 'legal':legal, 'history':history}
        pickle.dump(l, out, pickle.HIGHEST_PROTOCOL)