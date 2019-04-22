import csv

def import_reward_data():
    file_name = "game_data.csv"
    data = list(csv.reader(open(file_name)))

    for x in range(len(data)):
        for y in range(len(data[x])):
            data[x][y] = int(data[x][y])

    return data

reward_data = import_reward_data()

