import sys
import script

#teams = " ".join(sys.argv[1:]).split(", ")
# print(teams)
with open ("wildcards.txt") as fp:
    Lines = fp.read().splitlines()
    for line in Lines:
        teams = line.split(", ")
        script.main(teams[0], teams[1])