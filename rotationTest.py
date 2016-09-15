import pygame

#necessary pygame initializing
pygame.init()

#create a surface that will be seen by the user
screen =  pygame.display.set_mode((400, 400))

#create a varible for degrees of rotation
degree = 0
while True:
    
    #change the degree of rotation
    degree += 5
    if degree >= 360:
        degree = 0

    #create new surface with white BG
    surf =  pygame.Surface((40, 2))
    surf.fill((0, 200, 0))
    #set a color key for blitting
    surf.set_colorkey((255, 0, 0))

    #create shapes so you can tell rotation is happenning
    side = pygame.Rect(0, 0, 20, 2)

    #draw those shapes to that surface
    pygame.draw.rect(surf, (255, 0, 0), side)

    #draw surf to screen and catch the rect that blit returns
    blittedRect = screen.blit(surf, (150, 150))

    ##ROTATED
    #get center of surf for later
    oldCenter = blittedRect.center

    #clear screen to hide blittedRect
    screen.fill((40, 40, 40))

    #rotate surf by DEGREE amount degrees
    rotatedSurf =  pygame.transform.rotate(surf, degree)

    #get the rect of the rotated surf and set it's center to the oldCenter
    rotRect = rotatedSurf.get_rect()
    rotRect.center = oldCenter

    #draw rotatedSurf with the corrected rect so it gets put in the proper spot
    screen.blit(rotatedSurf, rotRect)


    #show the screen surface
    pygame.display.flip()

    #wait 60 ms until loop restart
    pygame.time.wait(60)