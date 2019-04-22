import csv
import numpy as np

def import_reward_data():
    file_name = "game_data.csv"
    data = list(csv.reader(open(file_name)))

    for x in range(len(data)):
        for y in range(len(data[x])):
            data[x][y] = int(data[x][y])

    return data

def init_q_table():
    table = []
    for x in range(10):
        row = []
        for y in range(10):
            row.append(0)
        table.append(row)
    print(table)

def main():
    reward_data = import_reward_data()
    q_table = []
    init_q_table()

