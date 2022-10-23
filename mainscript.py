#!/usr/bin/env python3

import userinput, pygame, sys

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

    if gotdata == False:
        inputdict, planetname = userinput.getuserinput()
        print(planetname)
        print(inputdict)
        gotdata = True
        pygame.display.set_caption(planetname+' in progress...')

    #other functions all go here
    displaysurface.fill((255,0,0))#loading placeholder
    pygame.display.flip()

