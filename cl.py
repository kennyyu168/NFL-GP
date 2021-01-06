import sys
import script

teams = " ".join(sys.argv[1:]).split(", ")
# print(teams)
script.main(teams[0], teams[1])