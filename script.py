# Filename: script.py
# Authors: Kenny Yu, Alan Tsui
# Date: 01/11/20
# Description: Takes in input and calculates the which nfl
#     team will win the a playoff game based on regular season
#     stats.

# Imports CSV to manipulate CSV files
import csv

# Import os to check file for emptiness
import os, random

def find_row(team, file_read):
    for row in file_read:
        if (team == row[0]):
            return row

def main(team1, team2):
    # Headers for each column
    headers = ["Team Name", "Wins", "Drives", "Yards", "Start", "Pts/G", "SC", "TO"]

    # Take in input for two teams to be compared
    team_1 = team1
    team_2 = team2

    # with open('nfl19.csv', newline='') as csvfile:
    #    reader = csv.reader(csvfile, delimiter=' ')
    #    for row in reader:
    #        print(', '.join(row))

    # Opens the csv file
    csv_file = csv.reader(open('nfl19.csv', "r"), delimiter=",")
    csv_file2 = csv.reader(open('nfl20.csv', "r"), delimiter=",")

    # Finds the row for team 1
    team1_data = find_row(team_1, csv_file)
    team2_data = find_row(team_2, csv_file2)

    # populate dictionaries
    dict_team1 = {}
    dict_team2 = {}

    length = len(headers)

    for num in range(0, length):
        dict_team1[headers[num]] = team1_data[num]
    for num in range(0, length):
        dict_team2[headers[num]] = team2_data[num]

    print(dict_team1)
    print(dict_team2)

    team1_wp = 0
    team2_wp = 0

    team1_pos = 100 - (float(dict_team1["Yards"]) + float(dict_team1["Start"]))
    team2_pos = 100 - (float(dict_team2["Yards"]) + float(dict_team2["Start"]))
    team1_ppd = float(dict_team1["Pts/G"]) * 16 / float(dict_team1["Drives"])
    team2_ppd = float(dict_team2["Pts/G"]) * 16 / float(dict_team2["Drives"])
    team1_dpg = float(dict_team1["Drives"]) / 16
    team2_dpg = float(dict_team2["Drives"]) / 16

    # theoretical team ppg
    team1_f = team1_dpg * team1_ppd * (100-float(dict_team1["TO"]))/100
    team2_f = team2_dpg * team2_ppd * (100-float(dict_team2["TO"]))/100

    # choke factor
    rand = random.random()
    if (team1_f > team2_f):
        if (rand >= .80):
            team1_f = team1_f * .80
    else:
        if (rand >= .80):
            team2_f = team2_f * .80

    # inconsistency factor
    team1_f = team1_f + random.randrange(-5*int((float(dict_team1["Pts/G"])-team1_f)), 5*int((float(dict_team1["Pts/G"])-team1_f)))
    team2_f = team2_f + random.randrange(-5*int((float(dict_team2["Pts/G"])-team2_f)), 5*int((float(dict_team2["Pts/G"])-team2_f)))

    team1_final = dict_team1["Team Name"] + ": " + str(team1_f)
    team2_final = dict_team2["Team Name"] + ": " + str(team2_f)
    
    win = 0
    if team1_f > team2_f:
        win = 1;
    else:
        win = 2;

    f_list = [team1_final, team2_final, win]
    return f_list
