#!/usr/bin/env python3

import pygame,sys
import pandas as pd

def overlayASCII(planetname, rain_df, elev_df, biome_df, realtemp_df, water_level_df):

    displayx = 1500 #these have to align with Reed's values
    displayy = 800 #these values, with a font size of 28, give a 50x27 grid

    pygame.init()
    displaysurface = pygame.display.set_mode(size=(displayx, displayy))
    pygame.display.set_caption('La Croix')
    displaysurface.fill((255,255,255))
    basefont = pygame.font.SysFont('applesymbols', 6)
    logoimage = pygame.image.load('CodingPlanetsLogo.png')

    charframe = biome_df.copy()
    posy = 0
    for h in charframe.iloc:
        posx=0
        for val in h:
            if TESTING WATER:
                charframe.iat[posy, posx] = '‿'
            elif elev_df.iat[posy, posx] in elev_df.quantile(q=0.8, method='table'):
                charframe.iat[posy, posx] = '△'
            elif biome_df.iat[posy, posx] == 'Grassland':
                charframe.iat[posy, posx] = 'w'
            elif biome_df.iat[posy, posx] == 'Rainforest':
                charframe.iat[posy, posx] = '⟰'
            elif biome_df.iat[posy, posx] == 'Tundra':
                charframe.iat[posy, posx] = '='
            elif biome_df.iat[posy, posx] == 'Tundra Forest':
                charframe.iat[posy, posx] = '⇈'
            elif biome_df.iat[posy, posx] == 'Taiga':
                charframe.iat[posy, posx] = '-'
            elif biome_df.iat[posy, posx] == 'Polar':
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
        for column in range(int(displayy/100)+1):
            for row in range(int(displayx/100)):
                    displaysurface.blit(basefont.render(charframe.loc[column].at[row], True, (0,0,0)), ((row*30)+350,column*30))

        mousepos = pygame.mouse.get_pos()
        if mousepos[0] >= 350 and mousepos[0] <= 1150:
            mousex = int((mousepos[0]-350)/100)
            mousey = int((mousepos[1]/100))
            biomeval = biome_df.iat[mousey, mousex]
            if elev_df.iat[mousey, mousex] in elev_df.quantile(q=0.8, method='table'):
                biomeval = 'Mountain'
            if water_level_df.iat[mousey, mousex] == 0:
                biomeval = 'Water'
            displaysurface.blit(basefont.render('Your biome is: '+biomeval, True, (0,0,0)), (1150, 100))
            rainval = rain_df.iat[mousey, mousex]
            displaysurface.blit(basefont.render(f'Average annual rainfall: {rainval} cm', True, (0,0,0)), (1150, 150))
            tempval = realtemp_df.iat[mousey, mousex]
            displaysurface.blit(basefont.render(f'Average annual temp: {tempval} C', True, (0,0,0)), (1150, 200))
            eleval = elev_df.iat[mousey, mousex]
            displaysurface.blit(basefont.render(f'Elevation: {eleval} m', True, (0,0,0)), (1150, 250))
        displaysurface.blit(basefont.render(planetname, True, (0,0,0)), (50, 600))
#        displaysurface.blit(logoimage, (50, 200))

        pygame.display.flip()

