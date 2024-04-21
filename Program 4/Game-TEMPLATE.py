#####################################################################
# author: Zachary Truxillo
# date: 4/6/2024   
# description: First utilization of Pygame, uses Item class which was 
# made last week. Makes a square (player) on the screen that can change 
# colors and size as well as move around the screen
#####################################################################
import pygame
from random import randint, choice
from Item import *
from Constants import *


class Person(Item, pygame.sprite.Sprite):
    def __init__(self):
        super(Person,self).__init__()
        # set initial color to Black and intitialize the surface
        self.color = BLACK
        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill(self.color)
    
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,value):
        self._color = value 
           
    @property
    def surf(self):
        return self._surf
    @surf.setter
    def surf(self,value):
        self._surf = value
        
    # randomly selects the value to be stored in the color instance
    # variable, and then changes the color of the surf to match that color
    def setColor(self):
        # Chooses from a list of different colors 
        # found in the Constants class 
        self.color = choice(COLORS) 
        self.surf.fill(self.color)

    # hanges the size of the Person/Item to a random value between
    # 10 and 100, and then changes the size of the surf to match that size
    def setSize(self):
        # set the size to be a random number between 10,100 
        # adjusting the surface size when done 
        self.size = randint(10, 100)
        self.surf = pygame.Surface((self.size, self.size))

    # receives as an argument a dictionary containing all the key 
    # pressed events and then updates the state of the Person 
    # based on what was pressed
    # Takes the goRight() and others from the Item class
    def update(self, pressedKeys):
        if pressedKeys[K_RIGHT]:
            self.goRight()
        if pressedKeys[K_LEFT]:
            self.goLeft()
        if pressedKeys[K_UP]:
            self.goUp()
        if pressedKeys[K_DOWN]:
            self.goDown()
        # Goes through the functions found above to change 
        # the size and color when space bar is pressed 
        if pressedKeys[K_SPACE]:
            self.setSize()
            self.setColor()
            
    # updates the Person’s x and y coordinates to a randomly selected
    # value within the appropriate range i.e. HEIGHT and WIDTH
    def setRandomPosition(self):
        self.x = randint(0, WIDTH)
        self.y = randint(0, HEIGHT)

    # calculates and returns the coordinates of the top 
    # left corner of the rectangle representing the Person. 
    # finding the top left corner of the surface
    def getPosition(self):
        Left_x = self.x - self.size/2
        Left_y = self.y - self.size/2
        return Left_x, Left_y

    #dds the value of the color to the String representation of an Item
    def __str__(self):
        return Item.__str__(self) + f",\tcolor = {self.color}"

########################### main game################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#####################################################################

# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a person object
p = Person()
RUNNING = True  # A variable to determine whether to get out of the
                # infinite game loop

while (RUNNING):
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
        elif (event.type == KEYDOWN and event.key == K_SPACE):
            print(p)

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()
    
    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    p.update(pressedKeys)

    # fill the screen with a color
    screen.fill(WHITE)
    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()

