import pygame
from Constants import *
<<<<<<< HEAD

class Entity:
    def __init__(self):
        pass
       
    
    def goLeft(self,value=1):
        self.x -= value
    def goRight(self,value=1):
        self.x += value
    def goUp(self,value=1):
        self.y -= value
    
    
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
        self._size = value 
        
'''
class Spider(Entity):
=======
import time
        
class Spider(pygame.sprite.Sprite):
>>>>>>> 1285bb15f429ab853d6a94371ca8426c654d22f8
    def __init__(self):
        #set initial x to be on left side of screen
        #have the spider always above the player
        super().__init__()
        self.image = pygame.image.load("Program 4/Images/spider.png").convert()
        self.rect = self.image.get_rect()
        self.setRandomPosition()
        
    def setRandomPosition(self):
        #have spider go from random position 
<<<<<<< HEAD
        self.y = randint(200, HEIGHT)
    
    def move(self):
        self.x += 3
        if(self.x == WIDTH):
            self.x = 0
            self.lives -= 1
'''
class Bullet(Entity):
    def __init__(self,x,y):
        self.surf = pygame.Surface((2,1))
        self.surf.fill(BLACK)
        self.y = y
        self.x = x
    
    def update(self):
        self.goUp()
        

class Wizard(Entity):
    lives = 3
=======
        self.rect.left = 0
        self.rect.centery = randint(100,HEIGHT)
    
    def update(self):
        self.rect.x += 3
        if(self.rect.right > WIDTH):
            self.setRandomPosition()
            

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((1,2))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def update(self):
        self.rect.y -= 1
        if self.rect.bottom < 0:
            self.kill()
        

class Wizard(pygame.sprite.Sprite):
    lives = 3
    
>>>>>>> 1285bb15f429ab853d6a94371ca8426c654d22f8
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Program 4/Images/wizard.png").convert_alpha()
        self.image.set_colorkey((0,0,0), RLEACCEL)
        self.image = pygame.transform.scale(self.image,(150,150))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT - self.image.get_size()[1])
        
    def goLeft(self,value=1):
        if(value>0):
            self.rect.x -= value
    def goRight(self,value=1):
        if(value<WIDTH):
            self.rect.x += value
    
    def update(self, pressedKeys):
        if pressedKeys[K_RIGHT]:
            self.goRight()
        if pressedKeys[K_LEFT]:
            self.goLeft()
        if pressedKeys[K_SPACE]:
            self.shoot()
    
    def shoot(self):
        bullet = Bullet(self.rect.centerx,self.rect.top)
        other_sprites.add(bullet)



    

################## MAIN ########################
# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player_sprites = pygame.sprite.Group()
w = Wizard()
player_sprites.add(w)

other_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
spiders = pygame.sprite.Group()
other_sprites.add(spiders)
other_sprites.add(bullets)


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
    player_sprites.update(pressedKeys)
    other_sprites.update()
    bullets.update()

    # fill the screen with a color
    screen.fill(WHITE)
<<<<<<< HEAD
    # then transfer the person to the screen
    screen.blit(w.image, w.getPosition())
    #Spider.draw(screen)
=======
    player_sprites.draw(screen)
    other_sprites.draw(screen)
    spiders.draw(screen)
>>>>>>> 1285bb15f429ab853d6a94371ca8426c654d22f8
    pygame.display.flip()
    # then transfer the person to the screen
    #screen.blit(w.image, w.getPosition())

