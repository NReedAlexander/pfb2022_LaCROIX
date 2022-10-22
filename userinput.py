#!/usr/bin/env python3

import pygame, sys

pygame.init()
displaysurface = pygame.display.set_mode(size=(1700, 800))
pygame.display.set_caption('User Input')
displaysurface.fill((255,255,255))
basefont = pygame.font.Font(None, 28)

inputdict = {'globrain':0.0, 'numtechplates':0, 'waterlev':0.0, 'globtemp':0.0}

rainx = 50
techx = 450
waterx = 850
tempx = 1250

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.fill((255,255,255))

    if rainx >400:
        rainx = 400
    elif rainx <50:
        rainx = 50
    rainrect = pygame.Rect(rainx, 400, 30, 30)
    if techx >800:
        techx = 800
    elif techx <450:
        rainx = 450
    techrect = pygame.Rect(techx, 400, 30, 30)
    if waterx >1200:
        waterx = 1200
    elif waterx <850:
        waterx = 850
    waterrect = pygame.Rect(waterx, 400, 30, 30)
    if tempx >1600:
        tempx = 1600
    elif tempx <1250:
        tempx = 1250
    temprect = pygame.Rect(tempx, 400, 30, 30)

    if pygame.mouse.get_pressed()==(True,False,False):
        mousepos = pygame.mouse.get_pos()
        if rainrect.collidepoint(mousepos):
            rainx = mousepos[0]-15
            rainrect.move(rainx, 400)
        if techrect.collidepoint(mousepos):
            techx = mousepos[0]-15
            techrect.move(techx,400)
        if waterrect.collidepoint(mousepos):
            waterx = mousepos[0]-15
            waterrect.move(waterx,400)
        if temprect.collidepoint(mousepos):
            tempx = mousepos[0]-15
            temprect.move(tempx,400)

    pygame.draw.rect(displaysurface, (0,0,0), rainrect)
    pygame.draw.rect(displaysurface, (0,0,0), techrect)
    pygame.draw.rect(displaysurface, (0,0,0), waterrect)
    pygame.draw.rect(displaysurface, (0,0,0), temprect)

    raintext = basefont.render('Enter Average Global Rainfall', True, (0,0,0))
    techtext = basefont.render('Enter Number of Techtonic Plates', True, (0,0,0))
    watertext = basefont.render('Enter Waterlevel', True, (0,0,0))
    temptext = basefont.render('Enter Average Global Temperature', True, (0,0,0))
    displaysurface.blit(raintext, (50,50))
    displaysurface.blit(techtext, (450,50))
    displaysurface.blit(watertext, (850,50))
    displaysurface.blit(temptext, (1250,50))


    pygame.display.flip()


