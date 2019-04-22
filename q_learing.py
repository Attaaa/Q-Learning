import csv
import numpy as np

def import_reward_data():
    file_name = "game_data.csv"
    data = list(csv.reader(open(file_name)))

    for x in range(len(data)):
        for y in range(len(data[x])):
            data[x][y] = int(data[x][y])

    return data

def main():
    # import reward data from csv file
    reward_data = import_reward_data()

    # initialize q-table (set all value to 0(zero))
    q_table = [[0 for i in range(10)]]*10

    

main()