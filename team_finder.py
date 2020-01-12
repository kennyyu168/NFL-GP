# Filename: team_finder.py
# Authors: Kenny Yu
# Date: 01/11/20
# Description: Finds the team in the file and returns their information in a row

# Imports CSV to manipulate CSV files
import csv

# Function Name: find_row()
# Function Prototype: find_row(team, file_read)
# Description: Finds the row of the team passed in
# Parameters: team - team name
#             file_read - file to be searched
# Return Value: Array of values from that row
def find_row(team, file_read):
	for row in file_read:
		if team == row[0]:
			return row

# Function Name: win_lose()
# Function Prototype: win_lose(team1, team2)
# Description: Calculates based on each subsequent parameter which team will
#     win or lose
# Parameters: team1 - the data of the first team passed in
#             team2 - the data of the second team passed in
# Return Value: Either 1 or 2 depending on which team will win
	

# Function Name: weight()
# Function Prototype: weight(data)
# Description: Calculates weight of each category on each parameter of the 
#              team data
# Parameter: data - the team of one team
# Return Value: Returns a percentage based on the each category
def weight(data):
	# Categorize each data point



