#!/usr/bin/env python3

import userinput, pygame, sys
from biomes import *
from random_rain import *
from tectonic_generator import * 
from sea_level_function import *

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
    rain_df = randomize_rain(inputdict['globrain'])
    
    # tect plates --> elev here ( eg elev_df = get_elevation(inputdict['numtechplates']) )
	elev_df = elevation_generator(int(inputdict['numtechplates'])

	# elev --> water here ( eg water_df = where_water(elev_df, inputdict['waterlev']) )
    water_df = sea_level(elev_df, inputdict['waterlev'])

    biome_df = make_biome_df(elev_df, water_df, rain_df, inputdict['globtemp']) 
    displaysurface.fill((255,0,0))#loading placeholder
    pygame.display.flip()

