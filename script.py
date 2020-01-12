# Filename: script.py
# Authors: Kenny Yu, Alan Tsui
# Date: 01/11/20
# Description: Takes in input and calculates the which nfl
#     team will win the a playoff game based on regular season
#     stats.

# Imports CSV to manipulate CSV files
import csv

# Import os to check file for emptiness
import os

# Headers for each column
headers = {"Team Name", "Wins", "Drives", "Yards", "Start", "Pts/G", "SC", "TO"}

# Take in input for two teams to be compared
team_1 = raw_input("Enter first team name: ")
team_2 = raw_input("Enter second team name: ")

# Print out the two teams for checking
print("Which one of " + team_1 + " or " + team_2 + " will win?")

# with open('nfl19.csv', newline='') as csvfile:
#    reader = csv.reader(csvfile, delimiter=' ')
#    for row in reader:
#        print(', '.join(row))
