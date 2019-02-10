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
    def calcualte(self, bats, hits, runs):
        self.bats += bats
        self.hits += hits
        self.runs += runs
        self.averageBat = round(self.hits/self.bats, 3)


'''
Function extractData is used to extract names, bats, hits and runs for strings through regular expressions
'''


score = re.compile(r"\b([\w]+ [\w]+) batted ([\d]{1,2}) times with ([\d]{1,2}) hits and ([\d]{1,2}) runs\b")
def extractData(string):
    match = score.match(string)
    if match is not None:
        return (match.group(1), float(match.group(2)), float(match.group(3)), float(match.group(4)))
    else:
        return False


'''
Extract names, bats, hits and runs from lines in text files
If this player has been added into the array, update bats and hits; if this player is not in the list, append name, bat, hit and run into list
Execute this process for all text files in file list

Function getAverageBat is used to calcualte the average bats for every player
Sort this players_list, and print the result

Extract year number from text file name, and output the year number and the statistic numbers for all players in that season
'''

def getAverageBat(player):
    return player.averageBat

files = {"cardinals-1930.txt","cardinals-1940.txt","cardinals-1941.txt","cardinals-1942.txt","cardinals-1943.txt","cardinals-1944.txt"}
for file in files:
    players_list = []
    f = open(file)
    for line in f:
        if extractData(line) :
            noExistName = True
            name, bats, hits, runs = extractData(line)
            for player in players_list :
                if player.name == name :
                    noExistName = False
                    player.calcualte(bats, hits, runs)
            if noExistName :
                players_list.append(Player(name, bats, hits, runs))

    sorted_players_list = sorted(players_list, key = getAverageBat, reverse = True)

    filename = file.split('.')[0]
    year = filename.split('-')[1]
    print ('The output for the {} season is:'.format(year))
    for player in sorted_players_list :
            print ('{}: {:.3f}'.format(player.name, player.averageBat))
    print ('\n')
