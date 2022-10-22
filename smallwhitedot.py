#!/usr/bin/env python3

import numpy as np
import pygame

pygame.init()

screen_size = (120, 80)
map_size = (2, 2)
#clock = pygame.time.Clock()

running = True

display = pygame.display.set_mode(screen_size)

pixels = np.array([
   [(255,241,232),(255,241,232)],
   [(255,241,232),(255,241,232)]
])

bg_col = (14,0,200)

screen = pygame.display.set_mode((screen_size))
screen.fill(bg_col)

map_surface = pygame.surfarray.make_surface(pixels)

#map_surface = pygame.Surface(map_size)
#planet_map = pygame.surfarray.blit_aray(map_surface, pixels) 


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(map_surface, (60,40))        
    pygame.display.flip()

    



