import csv
import numpy as np
import copy

def import_reward_data():
    file_name = "game_data.csv"
    data = list(csv.reader(open(file_name)))

    for x in range(len(data)):
        for y in range(len(data[x])):
            data[x][y] = int(data[x][y])

    return data

def update_qval(alpha, q_old, next_reward, gamma, next_q_max):
    return (1 - alpha) * q_old + alpha * (next_reward + gamma * next_q_max)

def select_random_action(state_x, state_y):
    action = -1
    actIsValid = False
    temp_state_x = copy.copy(state_x)
    temp_state_y = copy.copy(state_y)
    while not(actIsValid):
        state_x = temp_state_x
        state_y = temp_state_y
        action = np.random.randint(0,4)
        if (action == 0):
            state_y -= 1
        elif (action == 1):
            state_x += 1
        elif (action == 2):
            state_y += 1
        elif (action == 3):
            state_x -= 1
        
        if ((state_x >= 0 and state_x <= 14) or (state_y >= 0 and state_y <= 14)):
            actIsValid = True

    return state_x, state_y, action

def select_best_action(q_table, state_x, state_y):
    action = -1
    actIsValid = False
    while not(actIsValid):
        np.argmax(q_table[state_x][state_y])
        if (action == 0):
            state_y -= 1
        elif (action == 1):
            state_x += 1
        elif (action == 2):
            state_y += 1
        elif (action == 3):
            state_x -= 1
        
        if ((state_x >= 0 and state_x <= 14) or (state_y >= 0 and state_y <= 14)):
            actIsValid = True

    return state_x, state_y, action

def exploration_rate_decay(old_exploration_rate, iteration):
    return old_exploration_rate * np.exp(-0.1 / iteration)

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
    exploration_rate = 1
    exploration_rate_treshold = np.random.rand()
    num_episodes = 1
    
    # initial state
    state_x = 0
    state_y = 14

    # loop for each episodes
    for i in range(1):
        alpha = 0.6
        gamma = 0.5
        epsilon = 1
        reward = 0
        for j in range(10):
            # if exploration rate treshold lest than or equal than exploration rate 
            # choose random action to explore
            next_state_x, next_state_y = 0, 0
            action = 0
            if (exploration_rate_treshold <= exploration_rate):  
                # select random action
                next_state_x, next_state_y, action = select_random_action(state_x, state_y)
            else:
                next_state_x, next_state_y, action = select_best_action(q_table, state_x, state_y)

            q_old = q_table[state_x][state_y][action]
            q_max = np.max(q_table[next_state_x][next_state_y])
            action_reward = reward_data[next_state_x][next_state_y]
            # update q table
            q_table[state_x][state_y][action] = update_qval(alpha, q_old, action_reward, gamma, q_max)

            state_x = next_state_x
            state_y = next_state_y

        # exploration_rate = exploration_rate_decay(exploration_rate, i)

    print(q_table[0][14])

main()