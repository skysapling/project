# --------------- SETUP ---------------


# Importing necessary modules
import pygame
import math
import random


# --------------- DISPLAY ---------------


# Variables for the display
trans = (1, 1, 1)
red = (200, 0, 0)
green = (0, 200, 0)
sky = (180, 200, 255)
grass = (100, 155, 75)
black = (0, 0, 0)
white = (255, 255, 255)
clock = pygame.time.Clock()
fps = 25
(width, height) = (800, 500)
title = "tankGame"


# Setting up the display
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)


# --------------- GLOBALS ---------------


# Variables for calculations
gravity = 10
(angle, power) = (0, 10)
(angleChange, powerChange) = (0, 0)
(maxAngle, maxPower) = (90, 100)


# Variables for tank
increments = {'angle': 5,'power': 2}
movementSpeed = 5
(tankWidth, tankHeight) = (20, 10)
barrelHeight = 2
(tankX, tankY) = (100, 400)
tankChangeX = 0
bulletSpeed = 4


"""
# Variables for target
(targetWidth, targetHeight) = (25, random.randint(50, 200))
(targetX, targetY) = (random.randint(600, 750), random.randint(25, (height / 2) - 25))
"""

# Variables for text
font = pygame.font.SysFont("Arial", 15)
showAngleText = font.render("angle  =", True, black)
showPowerText = font.render("power =", True, black)


# --------------- FUNCTIONS ---------------


# Blitting the text
def blitText(angle, power):
    controlA = font.render("ARROW keys to move and adjust angle", True, black)
    controlB = font.render("KP+ and KP- to adjust power", True, black)
    controlC = font.render("SPACE to shoot", True, black)
    screen.blit(controlA, [5, tankY + tankHeight + 5])
    screen.blit(controlB, [5, tankY + tankHeight + 20])
    screen.blit(controlC, [5, tankY + tankHeight + 35])
    showAngle = font.render(str(angle), True, black)
    showPower = font.render(str(power), True, black)
    screen.blit(showAngleText, [2, 0])      # Blitting 'angle =' to the screen
    screen.blit(showPowerText, [2, 15])     # Blitting 'power =' to the screen
    screen.blit(showAngle, [60, 0])         # Blitting the value of angle
    screen.blit(showPower, [60, 15])        # Blitting the value of power


# Drawing the tank model
def drawTank():
    pygame.draw.rect(screen, green, [tankX, tankY, tankWidth, tankHeight])          # Draws the main body
    pygame.draw.rect(screen, black, [tankX, tankY + 8, tankWidth, barrelHeight])    # Draws the wheels


# Drawing the target
class target(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([tankWidth, tankHeight])
        self.image.fill(red)
        self.rect = self.image.get_rect()

          
# Defining the shell
class shell(pygame.sprite.Sprite):              # Creates the shell() class
    def __init__(self):                             # Defines an initiation fuction for this class
        super().__init__()                              # Call the parent class constructor
        self.image = pygame.Surface([2, 2])             # Defines the bullet as a 2x4 surface
        self.image.fill(black)                          # Paints the bullet black
        self.rect = self.image.get_rect()               # Gets the area size of the bullet

    def update(self):                               # Defines a function as update for this class
        (bulletChangeX, bulletChangeY) = (((maxAngle - angle) / maxAngle) * bulletSpeed, (angle / maxAngle) * bulletSpeed)
        self.rect.y -= bulletChangeY                    # Moves the bullet in the y axis
        self.rect.x += bulletChangeX                    # Moves the bullet in the x axis


# --------------- GROUPS ---------------


bulletList = pygame.sprite.Group()              # Defines bulletList as a pygame group


# --------------- MAIN LOOP ---------------

"""
target = target()
target.rect.x = targetX
target.rect.y = targetY
"""

# Running the program
running = True
acceptInput = True
while running:                                                          # Starts the loop
    if acceptInput == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                                           # Checks if the user has closed/exited PyGame
                running = False                                                         # Breaks the loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:                                      # Checks for left key pressed
                    tankChangeX = -movementSpeed                                        # Moves the tank left
                if event.key == pygame.K_RIGHT:                                     # Checks for right key pressed                    
                    tankChangeX = movementSpeed                                         # Moves the tank right
                keyDown = pygame.key.get_pressed()
                if keyDown[pygame.K_UP]:                                            # Checks for up key pressed
                    angleChange = increments['angle']                                   # Changes the angle by the set increment
                if keyDown[pygame.K_DOWN]:                                          # Checks for down key pressed
                    angleChange = -increments['angle']                                  # Changes the angle by the set increment
                if keyDown[pygame.K_KP_PLUS]:                                       # Checks for KP+ pressed
                    powerChange = increments['power']                                   # Changes the power by the set increment
                if keyDown[pygame.K_KP_MINUS]:                                      # Checks for KP- pressed
                    powerChange = -increments['power']                                  # Changes the power by the set increment
                if event.key == pygame.K_SPACE:                                     # Checks for SPACE key pressed
                    bullet = shell()                                                    # Calls the shell class
                    bullet.rect.x = barrelX                                             # Sets bullet's x to barrelX
                    bullet.rect.y = barrelY                                             # Sets bullet's y to barrelY
                    bulletList.add(bullet)                                              # Adds bullet to the bullet sprite list
                    acceptInput = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:       # Checks if the left or right keys are no longer pressed
                    tankChangeX = 0                                                     # Stops the tank moving
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:          # Checks if the up or down keys are no longer pressed
                    angleChange = 0                                                     # Stops the angle from changing
                if event.key == pygame.K_KP_PLUS or event.key == pygame.K_KP_MINUS: # Checks if the KP+ or KP- keys are no longer pressed
                    powerChange = 0                                                     # Stops the power from changing


    # Updating the sprite lists
    bulletList.update()                             # Calls the update function for every bullet

    
    # Limiting the angle and power variables (tried as function - not working)
    angle += angleChange        
    if angle > maxAngle:            # Checks if the angle is above its limit
        angle = maxAngle                # Sets the angle to its maximum
    elif angle < 0:                 # Checks if the angle is below its limit
        angle = 0                       # Sets the angle to its minimum
    power += powerChange
    if power > maxPower:            # Checks if the power is above its limit
        power = maxPower                # Sets the power to its maximum
    elif power < 10:                # Checks if the power is below its limit
        power = 10                      # Sets the power to its minimum

    
    # Calculating positions
    if tankX <= 0:                                  # Checks if the tank is at the left edge of the screen
        tankChangeX = movementSpeed                    # Bounces the tank back
    if tankX >= width - tankWidth:                  # Checks if the tank is at the right edge of the screen
        tankChangeX = -movementSpeed                     # Bounces the tank back
    tankX += tankChangeX                            # Moves the tank in the X direction
    barrelX = tankX + (tankWidth / 2)                 # Places the barrel at the tank
    barrelY = tankY - barrelHeight                  # Places the barrel at the tank

    
    # Preparing to rotate the barrel
    barrel = pygame.Surface([tankWidth * 2, barrelHeight])                      # Creates a surface as the barrel
    barrel.fill(green)                                                          # Colours the barrel green
    barrel.set_colorkey(trans)                                                  # Sets the transparent colour to trans
    
    cut = pygame.Rect(0, 0, tankWidth - 1, barrelHeight)                        # Defines a rectangle
    pygame.draw.rect(barrel, trans, cut)                                        # Makes one end of the barrel surface transparent

    blitBarrel = screen.blit(barrel, (tankX - (tankWidth / 2), barrelY))        # Blits the surface to where the tank is
    center = blitBarrel.center                                                  # Sets the center to the blitted surface's center
    
    screen.fill(sky)                                                            # Fills the screen to hide the blitted surface

        
    # Drawing
    screen.fill(sky)                                                            # Fills the background with the colour 'sky'
    bulletList.draw(screen)                                                     # Draws all bullets from bulletList
    pygame.draw.rect(screen, grass, [0, tankY + tankHeight, width, tankY])      # Draws a 'grass' rectangle from the tank to the bottom of the screen
    drawTank()
    blitText(angle, power)


    # Rotating the barrel
    rotatedBarrel = pygame.transform.rotate(barrel, angle)              # Sets the angle of the barrel to the angle variable
    rotBarrel = rotatedBarrel.get_rect()                                # Defines rotBarrel as the area of the rotated barrel
    rotBarrel.center = center                                           # Sets the center of rotBarrel to the center of the blitted surface

    screen.blit(rotatedBarrel, rotBarrel)                               # Blits the rotated barrel to the point of rotBarrel


    for bullet in bulletList:
        """targetHit = pygame.sprite.spritecollide(bullet, target, True)
        for target in targetHit:
            bulletList.remove(bullet)"""
        if bullet.rect.y < -2 or bullet.rect.x > width + 2:             # Checks if the bullet is above the screen
            bulletList.remove(bullet)                                       # Removes the bullet
            acceptInput = True


    # Displaying
    pygame.display.flip()                                                   # Updates the display
    clock.tick(fps)                                                         # At the rate of fps


# --------------- EXIT ---------------

    
# Exits PyGame and Python
pygame.quit()
quit()