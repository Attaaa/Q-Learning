import numpy as np
import operator
import matplotlib.pyplot as plt
from copy import copy

def get_possible_action(state):
    possible_action = []
    if (state[0] > 0):
        possible_action.append(0)
    if (state[1] < 14):
        possible_action.append(1)
    if (state[0] < 14):
        possible_action.append(2)
    if (state[1] > 0):
        possible_action.append(3)
    return possible_action

def next_state(state, action):
    if (action == 0):
        state[0] -= 1
    elif (action == 1):
        state[1] += 1
    elif (action == 2):
        state[0] += 1
    elif (action == 3):
        state[1] -= 1 
    return state

def plot_result(visitedState, rewardData):
    fig, ax = plt.subplots()
    im = ax.imshow(visitedState)
    for i in range(15):
        for j in range(15):
            text = ax.text(j, i, rewardData[i][j], ha="center", va="center", color="w")
    plt.xlabel("state_x")
    plt.ylabel("state_y")
    plt.show()

reward_data = np.genfromtxt('reward.txt', dtype=int)

init_exploration_rate = 1
alpha = 0.5
gamma = 0.9
num_episodes = 100
exploration_rate = init_exploration_rate
init_state = [14,0]
q_table = np.zeros((15,15,4))

visitedState = np.zeros((15,15))
visitedState[init_state[0]][init_state[1]] = 1

for i in range(1,num_episodes):
    state = copy(init_state)
    reward = 0
    random_number = np.random.rand()
    num_iteration = 0
    while ((state[0] != 0 or state[1] != 14) and num_iteration < 5000):
        from_state = copy(state)
        possible_action = get_possible_action(state)
        action = -1
        if (random_number <= exploration_rate and i != num_episodes-1):
            # get random action
            action = np.random.choice(possible_action)
        else:
            # get best action, action that have max q value
            temp = {}
            for act in possible_action:
                temp[act] = copy(q_table[state[0]][state[1]][act])
            action = max(temp.items(), key=operator.itemgetter(1))[0]

        state = next_state(state, action)

        old_q = copy(q_table[from_state[0]][from_state[1]][action])
        next_q = np.max(q_table[state[0]][state[1]])
        action_reward = reward_data[state[0]][state[1]]
        reward += action_reward

        q_table[from_state[0]][from_state[1]][action] = (1-alpha) * old_q + alpha*(action_reward + gamma * next_q)

        if (i == num_episodes-1):
            visitedState[state[0]][state[1]] = 1
            print("from state = {},{}".format(from_state[0],from_state[1]))
            print("action = {}".format(action))
            print("to state = {},{}".format(state[0],state[1]))
            print("Reward: {}".format(reward))
        
        num_iteration += 1

    exploration_rate = init_exploration_rate * np.exp( -0.005*i )

plot_result(visitedState, reward_data)
print(q_table)
