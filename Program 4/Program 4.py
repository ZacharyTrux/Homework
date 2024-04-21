import pygame
from Constants import *

class Entity:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
        self.lives = 3
        
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,value):
        if(value > WIDTH): 
            self._x = WIDTH
        elif(value < 0):
            self._x = 0
        else:
            self._x = value
            
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,value):
        if(value > HEIGHT):
            self._y = HEIGHT
        elif(value < 0):
            self._y = 0
        else:
            self._y = value
            
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,value):
        if(value >= 1):
            self._size = value 
        else:
            pass
'''
class Spider(Entity):
    def __init__(self):
        #set initial x to be on left side of screen
        #have the spider always above the player
        super().__init__(self,x=0,y=200)
        self.surf = pygame.image.load("Program 4/Images/spider.png").convert()
        
        
    def setRandomPosition(self):
        #have spider go from random position 
        self.y = randint(200, HEIGHT)
    
    def move(self):
        self.x += 3
        if(self.x == WIDTH):
            self.x = 0
            self.lives -= 1
'''
class Bullet(Entity):
    def __init__(self):
        super().__init__(self,x=600,y=0)
            
    def shoot(self):
        pass
        

class Wizard(Entity,Bullet):
    def __init__(self):
        super().__init__(self,x=600,y=0)
        self.surf = pygame.image.load("Program 4/Images/wizard.png").convert()
        
    def goLeft(self,value=1):
        self.x -= value
    def goRight(self,value=1):
        self.x += value
        
    def get_position(self):
        Left_x = self.x - self.size/2
        Left_y = self.y - self.size/2
        return Left_x, Left_y
    
    def update(self, pressedKeys):
        if pressedKeys[K_RIGHT]:
            self.goRight()
        if pressedKeys[K_LEFT]:
            self.goLeft()
        if pressedKeys[K_SPACE]:
            self.shoot()

class StartGame:
    def get_position(self):
        Left_x = self.x - self.size/2
        Left_y = self.y - self.size/2
        return Left_x, Left_y
    

################## MAIN ########################
# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a person object
w = Wizard()
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

    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()
    
    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.
    w.update(pressedKeys)

    # fill the screen with a color
    screen.fill(WHITE)
    # then transfer the person to the screen
    screen.blit(p.surf, p.getPosition())
    pygame.display.flip()

