import re
import sys
import os


'''
Define player class
This class include player's name, bats, hits and runs, all these four numbers would be extracted from the regular expression
However, runs in this module would not be used for further calculation

Function update is used to update every palyer's bats and hits, and calculate their total bats and hits
'''


class Player:
    def __init__(self, name, bats, hits, runs):
        self.name = name
        self.bats = bats
        self.hits = hits
        self.runs = runs
    def calculate(self, bats, hits, runs):
        self.bats += bats
        self.hits += hits
        self.runs += runs
        self.averageBat = round(self.hits/self.bats, 3)


'''
Function extractData is used to extract names, bats, hits and runs from strings through regular expressions
'''


score = re.compile(r"\b([\w]+ [\w]+) batted ([\d]{1,2}) times with ([\d]{1,2}) hits and ([\d]{1,2}) runs\b")
def extractData(string):
    match = score.match(string)
    if match is not None:
        return (match.group(1), float(match.group(2)), float(match.group(3)), float(match.group(4)))
    else:
        return False


'''
When execute this python file, no parameter input(if a command line argument is not present), script will print a usage message
'''


if len(sys.argv) < 2:
    sys.exit("Usage: %s filename" % sys.argv[0])
file = sys.argv[1]
if not os.path.exists(file):
	sys.exit("Error: File '%s' not found" % sys.argv[1])


'''
Extract names, bats, hits and runs from lines in text files
If this player has been added into the array, update bats and hits; if this player is not in the list, append name, bat, hit and run into list
'''

players_list = []
f = open(file)
for line in f:
    if extractData(line):
        noExistName = True
        name, bats, hits, runs = extractData(line)
        for player in players_list:
            if player.name == name:
                player.calculate(bats, hits, runs)
                noExistName = False
        if noExistName:
            players_list.append(Player(name, bats, hits, runs))


'''
Function getAverageBat is used to calcualte the average bats for every player
Sort this players_list, and print the result
'''


def getAverageBat(player):
    return player.averageBat
sorted_players_list = sorted(players_list, key = getAverageBat, reverse = True)
for player in sorted_players_list :
    print ('{}: {:.3f}'.format(player.name, player.averageBat))
