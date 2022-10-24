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
    basefont = pygame.font.SysFont('applesymbols', 10)
    textfont = pygame.font.SysFont('applesymbols', 28)
    logoimage = pygame.image.load('CodingPlanetsLogo.png')

    charframe = biome_df.copy()
    posy = 0
    for h in charframe.iloc:
        posx=0
        for val in h:
            if water_level_df.iat[posy, posx] == 0:
                charframe.iat[posy, posx] = '‿'
            elif elev_df.iat[posy, posx] > elev_df.quantile(0.8).mean():
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
        for column in range(int(displayy/8)):
            for row in range(int(displayx/8)):
                    displaysurface.blit(basefont.render(charframe.loc[column].at[row], True, (0,0,0)), ((row*8)+350,column*8))

        mousepos = pygame.mouse.get_pos()
        if mousepos[0] >= 350 and mousepos[0] <= 1150:
            mousex = int((mousepos[0]-350)/8)
            mousey = int((mousepos[1]/8))
            biomeval = biome_df.iat[mousey, mousex]
            if elev_df.iat[mousey, mousex] > elev_df.quantile(0.8).mean():
                biomeval = 'Mountain'
            if water_level_df.iat[mousey, mousex] == 0:
                biomeval = 'Water'
            displaysurface.blit(textfont.render(f'Your biome is: {biomeval}', True, (0,0,0)), (1150, 100))
            rainval = rain_df.iat[mousey, mousex]
            displaysurface.blit(textfont.render(f'Average annual rainfall: {rainval} cm', True, (0,0,0)), (1150, 150))
            tempval = realtemp_df.iat[mousey, mousex]
            displaysurface.blit(textfont.render(f'Average annual temp: {tempval} C', True, (0,0,0)), (1150, 200))
            eleval = elev_df.iat[mousey, mousex]
            displaysurface.blit(textfont.render(f'Elevation: {eleval} m', True, (0,0,0)), (1150, 250))
        displaysurface.blit(textfont.render(planetname, True, (0,0,0)), (50, 600))
#        displaysurface.blit(logoimage, (50, 200))

        pygame.display.flip()

