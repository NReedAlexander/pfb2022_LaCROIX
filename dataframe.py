#!/usr/bin/env python3

import pandas as pd
import random as rand

width = 4
height = 4
longitude = []

dictofdefaults = {'Fault':False, 'Elevation':0.0, 'Underwater':False, 'Temp':0.0, 'Rainfall':0.0, 'Biome':'None'}

mainframe = dictofdefaults.copy()

for w in range(width):
    longitude.append(w)

for default in dictofdefaults:
    subframe = pd.DataFrame(columns=longitude)
    for h in range(height):
        longlist = []
        for w in range(width):
            longlist.append(dictofdefaults[default])
        subframe.loc[len(subframe)] = longlist
    mainframe[default] = subframe

print(mainframe)


#randomizer for testing purposes, comment out if you don't want
randdict = {'Fault':[False,True], 'Elevation':[-1.0,0.0,1.0], 'Underwater':[False,True], 'Temp':[-1.0,0.0,1.0], 'Rainfall':[-1.0,0.0,1.0], 'Biome':['None','Forest','Desert']}
for element in mainframe:
    for h in range(height):
        for w in range(width):
            mainframe[element].loc[h].at[w]  = rand.choice(randdict[element])

print(mainframe)


