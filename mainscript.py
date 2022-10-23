#!/usr/bin/env python3

import userinput, pygame, sys
from biomes import *
from random_rain import *

pygame.init()
displaysurface = pygame.display.set_mode(size=(1500,800))
pygame.display.set_caption('La Croix')
pygame.display.flip()
gotdata = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if gotdata == False: #this runs once
        inputdict, planetname = userinput.getuserinput() #returns planetname, which is a string, and inputdict, which is a dictionary containing the user input with the following keys: 'globrain', 'numtechplates', 'waterlev', 'globtemp'
        gotdata = True
        pygame.display.set_caption(planetname+' in progress...')

    ### other functions all go here ###
    mainframe = randomize_rain(mainframe) # input is dict of dfs including df with key 'rain' filled with average global rain value
    # tect plates --> elev here
    # elev --> water here
    mainframe = make_biome_df(mainframe) # input is dict of dfs including 'elev' df, 'water' df, 'rain' df, 'temp' df (just global average temp) 
    displaysurface.fill((255,0,0))#loading placeholder
    pygame.display.flip()

