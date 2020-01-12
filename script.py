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

# Import team_finder to find the information for each team
import team_finder as teamf

# Headers for each column
headers = {"Team Name", "Wins", "Drives", "Yards", "Start", "Pts/G", "SC", "TO"}

# Take in input for two teams to be compared
team_1 = input("Enter first team name: ")
team_2 = input("Enter second team name: ")

# Print out the two teams for checking
print("Which one of " + team_1 + " or " + team_2 + " will win?")

# with open('nfl19.csv', newline='') as csvfile:
#    reader = csv.reader(csvfile, delimiter=' ')
#    for row in reader:
#        print(', '.join(row))

# Opens the csv file
csv_file = csv.reader(open('nfl19.csv', "r"), delimiter=",")

# Finds the row for team 1
team_1_data = teamf.find_row(team_1, csv_file)
team_2_data = teamf.find_row(team_2, csv_file)
print( team_1_data )
print( team_2_data )


