#!/usr/bin/env python3

import pygame,sys
import pandas as pd

def overlayASCII(planetname, rain_df, elev_df, biome_df, realtemp_df, water_level_df):

    displayx = 1500 #these have to align with Reed's values
    displayy = 800 #these values, with a font size of 28, give a 50x27 grid

    pygame.init()
    displaysurface = pygame.display.set_mode(size=(displayx, displayy))
    pygame.display.set_caption('La Croix')
    basefont = pygame.font.SysFont('applesymbols', 10)
    textfont = pygame.font.SysFont('applesymbols', 28)
    logoimage = pygame.image.load('CodingPlanetsLogo.png')
    logoimage = pygame.transform.scale(logoimage, (300,300))
    biomedisplaydict = {'grassland':'Grassland','rain_forest':'Rainforest','tundra':'Tundra','temp_forest':'Temperate Forest','taiga':'Taiga','polar':'Polar','desert':'Desert','med_water':'Warm Water','cold_water':'Cold Water','frozen_water':'Frozen Water','coast':'Coast'}

    charframe = biome_df.copy()
    posy = 0
    for h in charframe.iloc:
        posx=0
        for val in h:
            if water_level_df.iat[posy, posx] == 0:
                charframe.iat[posy, posx] = '‿'
            elif elev_df.iat[posy, posx] > elev_df.quantile(0.8).mean() and water_level_df.iat[posy, posx] != 0:
                charframe.iat[posy, posx] = '△'
            elif biome_df.iat[posy, posx] == 'grassland':
                charframe.iat[posy, posx] = 'w'
            elif biome_df.iat[posy, posx] == 'rain_forest':
                charframe.iat[posy, posx] = '⟰'
            elif biome_df.iat[posy, posx] == 'tundra':
                charframe.iat[posy, posx] = '='
            elif biome_df.iat[posy, posx] == 'temp_forest':
                charframe.iat[posy, posx] = '⇈'
            elif biome_df.iat[posy, posx] == 'taiga':
                charframe.iat[posy, posx] = '-'
            elif biome_df.iat[posy, posx] == 'polar':
                charframe.iat[posy, posx] = '*'
            elif biome_df.iat[posy, posx] == 'desert':
                charframe.iat[posy, posx] = '∴'
            elif biome_df.iat[posy, posx] == 'coast':
                charframe.iat[posy, posx] = '≈'
            posx+=1
        posy+=1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        displaysurface.fill((175,240,134))

        displayx = 800
        for column in range(int(displayy/8)):
            for row in range(int(displayx/8)):
                    displaysurface.blit(basefont.render(charframe.loc[column].at[row], True, (0,0,0)), ((row*8)+350,column*8))

        mousepos = pygame.mouse.get_pos()
        if mousepos[0] >= 350 and mousepos[0] <= 1150:
            mousex = int((mousepos[0]-350)/8)
            mousey = int((mousepos[1]/8))
            biomeval = biome_df.iat[mousey, mousex]
            biomeval = biomedisplaydict[biomeval]
            displaysurface.blit(textfont.render(f'Your biome is: {biomeval}', True, (0,0,0)), (1150, 300))
            rainval = rain_df.iat[mousey, mousex]
            displaysurface.blit(textfont.render(f'Average annual rainfall: {rainval:.2f} cm', True, (0,0,0)), (1150, 350))
            tempval = realtemp_df.iat[mousey, mousex]
            displaysurface.blit(textfont.render(f'Average annual temp: {tempval:.2f} C', True, (0,0,0)), (1150, 400))
            eleval = elev_df.iat[mousey, mousex]
            if water_level_df.iat[mousey, mousex] != 0:
                eleval = eleval/50
            else:
                eleval = (eleval/100)-1000
            displaysurface.blit(textfont.render(f'Elevation: {eleval:.2f} m', True, (0,0,0)), (1150, 450))
        displaysurface.blit(textfont.render(planetname, True, (0,0,0)), (50, 575))
        displaysurface.blit(logoimage, (25, 250))

        pygame.display.flip()

