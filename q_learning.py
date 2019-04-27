# Q learning 
# Author Muh. Hatta Eka Putra

import csv
import numpy as np
import copy
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def import_reward_data():
    file_name = "world_grid.csv"
    data = list(csv.reader(open(file_name)))

    for x in range(len(data)):
        for y in range(len(data[x])):
            data[x][y] = int(data[x][y])

    return data

def update_qval(alpha, q_old, next_reward, gamma, next_q_max):
    return (1 - alpha) * q_old + alpha * (next_reward + gamma * next_q_max)

def get_possible_action(state_x, state_y):
    action_choices = []
    # select action choices
    # if state y is more than zero(0) then action up is possible
    # if state y is less than 14 then action down is possible
    # if state x is more than zero(0) then action right is possible
    # if state x is less than 14 then action left is possible
    if (state_y > 0):
        action_choices.append(0)
    if (state_x > 0):
        action_choices.append(3)
    if (state_x < 14):
        action_choices.append(1)
    if (state_y < 14):
        action_choices.append(2)

    return action_choices

def next_state_from(state_x, state_y, action):
    if (action == 0):
        state_y -= 1
    elif (action == 1):
        state_x += 1
    elif (action == 2):
        state_y += 1
    elif (action == 3):
        state_x -= 1

    return state_x, state_y

def select_random_action(state_x, state_y):
    action_choices = get_possible_action(state_x, state_y)
    
    # get random action from possible action
    action = np.random.choice(action_choices)

    state_x, state_y = next_state_from(state_x, state_y, action)

    return state_x, state_y, action

def select_best_action(state_x, state_y, q_table):
    action_choices = get_possible_action(state_x, state_y)
 
    maks = -999
    action = 0
    current_q_table = q_table[state_y][state_x]

    # get best action based on action choices from max value q_table
    for i in action_choices:
        if (maks < current_q_table[i]):
            maks = current_q_table[i]
            action = i
    
    # get next state from action
    state_x, state_y = next_state_from(state_x, state_y, action)

    return state_x, state_y, action

def exploration_rate_decay(old_exploration_rate, iteration):
    return old_exploration_rate * np.exp(-0.9 / iteration)

def main():
    # import reward data from csv file
    reward_data = import_reward_data()

    # initialize q-table (set all value to 0(zero))
    # action north(up) = 0
    # action east(right) = 1
    # action south(down) = 2
    # action west(left) = 3
    q_table = np.zeros((15,15,4))

    # initialize q learning 
    init_exploration_rate = 1
    alpha = 0.4
    gamma = 0.9
    num_episodes = 1000
    exploration_rate = init_exploration_rate

    # loop for each episodes
    for i in range(1, num_episodes):
        # initial state
        state_x = 0
        state_y = 14
        reward = 0
        exploration_rate_treshold = np.random.rand()*0.4
        while True:
            # if exploration rate treshold lest than or equal than exploration rate 
            # choose random action to explore
            next_state_x, next_state_y = 0, 0
            action = 0

            if (exploration_rate_treshold <= exploration_rate):  
                # select random action
                next_state_x, next_state_y, action = select_random_action(state_x, state_y)
            else:
                # select best action
                next_state_x, next_state_y, action = select_best_action(state_x, state_y, q_table)

            q_old = q_table[state_y][state_x][action]
            next_q_max = np.max(q_table[next_state_y][next_state_x])
            action_reward = reward_data[next_state_y][next_state_x]
            reward += action_reward

            # update q table
            q_table[state_y][state_x][action] = update_qval(alpha, q_old, action_reward, gamma, next_q_max)

            state_x = next_state_x
            state_y = next_state_y

            # end the episodes if reward less than -20000 or more than 400
            if (reward < -20000 or reward > 400):
                break

        exploration_rate = exploration_rate_decay(exploration_rate, i)

    # print optimal result from q table
    state_x = 0
    state_y = 14
    visitedState = np.zeros((15,15))
    next_state_x, next_state_y = 0, 0
    action = 0
    reward = 0
    visitedState[state_y][state_x] = 1
    while (state_x != 14 or state_y != 0):
        state_x, state_y, action = select_best_action(state_x, state_y, q_table)
        reward += reward_data[state_y][state_x]
        visitedState[state_y][state_x] = 1
        if reward < -1000:
            break
    print(visitedState)
    print(reward)
    
    # plot result
    fig, ax = plt.subplots()
    im = ax.imshow(visitedState)
    for i in range(15):
        for j in range(15):
            if (i == 14 and j == 0):
                text = ax.text(j, i, "start", ha="center", va="center", color="w")
            else:
                text = ax.text(j, i, reward_data[i][j], ha="center", va="center", color="w")
    plt.xlabel("state_x")
    plt.ylabel("state_y")
    fig.tight_layout()
    plt.show()

main()