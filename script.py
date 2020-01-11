import csv

with open('nfl19.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        print(', '.join(row))
