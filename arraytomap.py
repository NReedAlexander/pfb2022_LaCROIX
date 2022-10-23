#!/usr/bin/env python3
import numpy as np
import pygame
import sys

def draw_map(input_array):

    col, row, chanels = input_array.shape
    map_surface = pygame.surfarray.make_surface(input_array)
    return(map_surface)

def main():

    screen_size = (1500, 800)
    bg_col = (14,0,200)
    screen = pygame.display.set_mode((screen_size))
    screen.fill(bg_col)
    running = True
    pixels2 = np.array([
        [(0,0,255),(0,0,255)],
        [(0,0,255),(0,0,255)],
        [(0,0,255),(0,0,255)]
        ])
    
    map_surface = draw_map(pixels2)
    display = pygame.display.set_mode(screen_size)
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(map_surface, (750,400))        
        pygame.display.flip()

if __name__ == "__main__":
    main()
