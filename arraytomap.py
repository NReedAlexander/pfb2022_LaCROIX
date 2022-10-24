#!/usr/bin/env python3
import numpy as np
import pygame
import sys

def draw_map(input_array):

#    col, row, chanels = input_array.shape
    input_array = np.array(input_array)
    map_surface = pygame.surfarray.make_surface(input_array)
    return(map_surface)

def main():

    screen_size = (1500, 800)
    bg_col = (14,0,200)
    screen = pygame.display.set_mode((screen_size))
    screen.fill(bg_col)
    running = True
    #pixels2 = np.array([
    #    [(0,0,255),(0,0,255)],
    #    [(0,0,255),(0,0,255)],
    #    [(0,0,255),(0,0,255)]
    #    ])
    
    #pixels2 = [[(233,233,233) (233,233,233) (244,344,344)]
           # [(233,34,56) (67,22,88) (56,36,99)]]
    pixels4 = np.array([[(255, 215, 0), (0, 0, 255), (244, 255, 255), (154, 205, 50)],
       [(34, 139, 34), (85, 107, 47), (189, 183, 107), (218, 165, 32)],
       [(135, 206, 250), (250, 250, 250), (218, 165, 32), (34, 139, 34)]])
    #print(pixels2)
    #pixels3 = np.array(pixels2)

    map_surface = draw_map(pixels4)
    display = pygame.display.set_mode(screen_size)
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(map_surface, (750,400))        
        pygame.display.flip()

if __name__ == "__main__":
    main()
