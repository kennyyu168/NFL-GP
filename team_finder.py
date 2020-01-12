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


