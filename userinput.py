#!/usr/bin/env python3

import pygame, sys

def getuserinput():
    pygame.init()
    displaysurface = pygame.display.set_mode(size=(1500, 800))
    pygame.display.set_caption('La Croix')
    displaysurface.fill((255,255,255))
    basefont = pygame.font.Font(None, 28)

    inputdict = {'globrain':0.0, 'numtechplates':0, 'waterlev':0.0, 'globtemp':0.0}
    planetname = ''
    nameactive = False

    rainx = 100
    techx = 450
    waterx = 800
    tempx = 1150

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inputdict['globrain'] = (rainx-100)*(8/5)
                    inputdict['numtechplates'] = int(((techx-450)*0.1)+5)
                    inputdict['waterlev'] = (waterx-800)/250
                    inputdict['globtemp'] = (tempx-1150)*(4/5)-100
                    return [inputdict, planetname] #trigger movement to next step here
                elif nameactive:
                    if event.key == pygame.K_BACKSPACE:
                        planetname = planetname[:-1]
                    else:
                        planetname += event.unicode

        displaysurface.fill((255,255,255))

        namerect = pygame.Rect(300, 700, 500, 30)
        pygame.draw.rect(displaysurface, (200,200,200), namerect)
        displaysurface.blit(basefont.render(planetname, True, (0,0,0)), (305, 705))
        displaysurface.blit(basefont.render('Enter planet name:', True, (0,0,0)), (100, 705))

        if rainx >350:
            rainx = 350
        elif rainx <100:
            rainx = 100
        rainrect = pygame.Rect(rainx, 500, 30, 30)
        if techx >700:
            techx = 700
        elif techx <450:
            techx = 450
        techrect = pygame.Rect(techx, 500, 30, 30)
        if waterx >1050:
            waterx = 1050
        elif waterx <800:
            waterx = 800
        waterrect = pygame.Rect(waterx, 500, 30, 30)
        if tempx >1400:
            tempx = 1400
        elif tempx <1150:
            tempx = 1150
        temprect = pygame.Rect(tempx, 500, 30, 30)

        if pygame.mouse.get_pressed()==(True,False,False):
            mousepos = pygame.mouse.get_pos()
            if rainrect.collidepoint(mousepos):
                rainx = mousepos[0]-15
                rainrect.move(rainx, 500)
            if techrect.collidepoint(mousepos):
                techx = mousepos[0]-15
                techrect.move(techx,500)
            if waterrect.collidepoint(mousepos):
                waterx = mousepos[0]-15
                waterrect.move(waterx,500)
            if temprect.collidepoint(mousepos):
                tempx = mousepos[0]-15
                temprect.move(tempx,500)
            if namerect.collidepoint(mousepos):
                nameactive = True
            else:
                nameactive = False

        pygame.draw.rect(displaysurface, (100,100,100), pygame.Rect(100,510,280,10))
        pygame.draw.rect(displaysurface, (100,100,100), pygame.Rect(450,510,280,10))
        pygame.draw.rect(displaysurface, (100,100,100), pygame.Rect(800,510,280,10))
        pygame.draw.rect(displaysurface, (100,100,100), pygame.Rect(1150,510,280,10))

        pygame.draw.rect(displaysurface, (0,0,0), rainrect)
        pygame.draw.rect(displaysurface, (0,0,0), techrect)
        pygame.draw.rect(displaysurface, (0,0,0), waterrect)
        pygame.draw.rect(displaysurface, (0,0,0), temprect)

        raintext = basefont.render('Enter Average Global Rainfall', True, (0,0,0))
        rainval = basefont.render(f'{(rainx-100)*(8/5):.2f} cm', True, (0,0,0))
        techtext = basefont.render('Enter Number of Tectonic Plates', True, (0,0,0))
        techval = basefont.render(f'{int((((techx-450)*0.1)+5))} plates', True, (0,0,0))
        watertext = basefont.render('Enter Waterlevel', True, (0,0,0))
        waterval = basefont.render(f'{(waterx-800)/250:.2f}', True, (0,0,0))
        temptext = basefont.render('Enter Average Global Temperature', True, (0,0,0))
        tempval = basefont.render(f'{(tempx-1150)*(4/5)-100:.2f} C', True, (0,0,0))
        entmess = basefont.render('Hit return to proceed', True, (0,0,0))
        displaysurface.blit(raintext, (100,150))
        displaysurface.blit(rainval, (150,300))
        displaysurface.blit(techtext, (450,150))
        displaysurface.blit(techval, (500,300))
        displaysurface.blit(watertext, (850,150))
        displaysurface.blit(waterval, (850,300))
        displaysurface.blit(temptext, (1150,150))
        displaysurface.blit(tempval, (1250,300))
        displaysurface.blit(entmess, (950, 700))
        welcometext = pygame.font.Font(None,40).render('Welcome to La Croix!', True, (0,0,0))
        displaysurface.blit(welcometext, (600,50))

        pygame.display.flip()

