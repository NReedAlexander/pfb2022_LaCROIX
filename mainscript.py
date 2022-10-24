#!/usr/bin/env python3

import userinput, pygame, sys
from biomes import *
from random_rain import *
from tectonic_generator import * 
from sea_level_function import *
from biome_to_color import *
from map_resizer import *
from arraytomap import *

pygame.init()
displaysurface = pygame.display.set_mode(size=(1500,800))
pygame.display.set_caption('La Croix')
pygame.display.flip()
gotdata = False
gotrain = False
gotelev = False
gotwater = False
gotbiomes = False
gotcolors = False 
gotresize = False 
gotmapsurf = False 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if gotdata == False: #this runs once
        inputdict, planetname = userinput.getuserinput() #returns planetname, which is a string, and inputdict, which is a dictionary containing the user input with the following keys: 'globrain', 'numtechplates', 'waterlev', 'globtemp'
        gotdata = True
        pygame.display.set_caption(planetname+' in progress...')
        displaysurface.fill((255,0,0))#loading placeholder

    ### other functions all go here ###
    if gotrain == False:
        rain_df = randomize_rain(inputdict['globrain'])
        gotrain = True
    
    # tect plates --> elev here ( eg elev_df = get_elevation(inputdict['numtechplates']) )
    if gotelev == False:
    	elev_df = elevation_generator(int(inputdict['numtechplates'])
        gotelev = True

	# elev --> water here ( eg water_df = where_water(elev_df, inputdict['waterlev']) )
    if gotwater == False:
        water_df = sea_level(elev_df, inputdict['waterlev'])
        gotwater = True

    if gotbiomes == False:
        biome_df, temp_df = make_biome_df(elev_df, water_df, rain_df, inputdict['globtemp']) 
        gotbiomes = True

		if gotcolors = False: 
				pixel_map = biome_colors(biome_df) 
				gotcolors = True 

		if gotresize = False: 
				larger_map = resize_map(pixel_map) 
				gotresize = True 

		if gotmapsurf = False:
				map_surface = draw_map(larger_map) 
				gotmapsurf = True 
				displaysurface.blit(map_surface, (750, 400))
    pygame.display.flip()

