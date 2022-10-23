#!/usr/bin/env python3

import pygame,sys,dataframe
import pandas as pd

testframe = dataframe.initdataframe()

def overlayASCII(testframe):

    displayx = 1500 #these have to align with Reed's values
    displayy = 800 #these values, with a font size of 28, give a 50x27 grid

    pygame.init()
    displaysurface = pygame.display.set_mode(size=(displayx, displayy))
    pygame.display.set_caption('Planet Name')
    displaysurface.fill((255,255,255))
    basefont = pygame.font.SysFont('applesymbols', 28)

    testframe = dataframe.initdataframe()
    charframe = testframe['Underwater'].copy()
    posy = 0
    for h in charframe.iloc:
        posx=0
        for val in h:
            if val == True:
                charframe.iat[posy, posx] = '‿'
            elif testframe['Elevation'].iat[posy, posx] >= 4.0:
                charframe.iat[posy, posx] = '△'
            elif testframe['Biome'].iat[posy, posx] == 'Grassland':
                charframe.iat[posy, posx] = 'w'
            elif testframe['Biome'].iat[posy, posx] == 'Rainforest':
                charframe.iat[posy, posx] = '⟰'
            elif testframe['Biome'].iat[posy, posx] == 'Tundra':
                charframe.iat[posy, posx] = '='
            elif testframe['Biome'].iat[posy, posx] == 'Tundra Forest':
                charframe.iat[posy, posx] = '⇈'
            elif testframe['Biome'].iat[posy, posx] == 'Taiga':
                charframe.iat[posy, posx] = '-'
            elif testframe['Biome'].iat[posy, posx] == 'Polar':
                charframe.iat[posy, posx] = '*'
            else:
                charframe.iat[posy, posx] = '∴'
            posx+=1
        posy+=1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        displaysurface.fill((255,255,255))

        displayx = 800
        for column in range(int(displayy/30)+1):
            for row in range(int(displayx/30)):
                    displaysurface.blit(basefont.render(charframe.loc[column].at[row], True, (0,0,0)), ((row*30)+350,column*30))

        mousepos = pygame.mouse.get_pos()
        if mousepos[0] >= 350 and mousepos[0] <= 1150:
            mousex = int((mousepos[0]-350)/30)
            mousey = int((mousepos[1]/30))
            biomeval = testframe['Biome'].iat[mousey, mousex]
            if testframe['Elevation'].iat[mousey, mousex] == 4.0:
                biomeval = 'Mountain'
            if testframe['Underwater'].iat[mousey, mousex] == True:
                biomeval = 'Water'
            displaysurface.blit(basefont.render('Your biome is: '+biomeval, True, (0,0,0)), (1150, 100))
            rainval = testframe['Rainfall'].iat[mousey, mousex]
            displaysurface.blit(basefont.render(f'Average annual rainfall: {rainval} cm', True, (0,0,0)), (1150, 150))
            tempval = testframe['Temp'].iat[mousey, mousex]
            displaysurface.blit(basefont.render(f'Average annual temp: {tempval} C', True, (0,0,0)), (1150, 200))
            eleval = testframe['Elevation'].iat[mousey, mousex]
            displaysurface.blit(basefont.render(f'Elevation: {eleval} m', True, (0,0,0)), (1150, 250))
        displaysurface.blit(basefont.render('Planet Name', True, (0,0,0)), (50, 600))

        pygame.display.flip()

overlayASCII(testframe)
