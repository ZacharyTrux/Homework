import pygame
from Constants import *


clock = pygame.time.Clock()
FPS = 60
        
class Spider(pygame.sprite.Sprite):
    
    def __init__(self):
        #set initial x to be on left side of screen
        #have the spider always above the player
        super().__init__()
        self.image = pygame.image.load("Program 4/Images/spider.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(150,150))
        self.rect = self.image.get_rect()
        self.setRandomPosition()
        
    def setRandomPosition(self):
        #have spider go from random position 
        self.rect.center = (0,randint(0,HEIGHT-300))
    
    def update(self):
        global lives
        self.rect.x += 10
        if(self.rect.right > WIDTH):
            self.setRandomPosition()
            lives -= 1
            

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("Program 4/Images/Bolt.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(150,150))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()
        

class Wizard(pygame.sprite.Sprite):
    cooldown = 30
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Program 4/Images/wizard.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(150,150))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT - 100)
        
    def goLeft(self):
        self.rect.move_ip(-5,0)
        if(self.rect.centerx < 0):
            self.rect.centerx = 0 

    def goRight(self):
        self.rect.move_ip(5,0)
        if(self.rect.centerx > WIDTH):
            self.rect.centerx = WIDTH
    
    def update(self, pressedKeys):
        if pressedKeys[K_RIGHT]:
            self.goRight()
        if pressedKeys[K_LEFT]:
            self.goLeft()
        if pressedKeys[K_SPACE]:
            self.try_shooting()
            
        if(self.cooldown > 0):
            self.cooldown -= 1
    
    def try_shooting(self):
        if(self.cooldown == 0):
            self.shoot()
            self.cooldown = 30
    
    def shoot(self):
        bullet = Bullet(self.rect.centerx,self.rect.top)
        bullets.add(bullet)
        
        



    

################## MAIN ########################
# Initialize pygame library and display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player_sprites = pygame.sprite.Group()
wizard = Wizard()
player_sprites.add(wizard)

enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
spiders = Spider()           
enemies.add(spiders)

global scores
scores = 0

global lives
lives = 3

def collided(enemies,bullets):
    global scores
    collisions = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for enemy, bullet_list in collisions.items():
        # get the spider out of the group
        enemy.kill()
        # create new spider to run across screen
        spiders = Spider()
        enemies.add(spiders)
        
        # gets rid of the bullet which collided in the list 
        for bullet in bullet_list:
            bullet.kill()
            
        scores += 1

RUNNING = True  # A variable to determine whether to get out of the
                # infinite game loop

while (RUNNING):
    pygame.font.init()
    
    # Look through all the events that happened in the last frame to see
    # if the user tried to exit.
    for event in pygame.event.get():
        if (event.type == KEYDOWN and event.key == K_ESCAPE):
            RUNNING = False
        elif (event.type == QUIT):
            RUNNING = False
            
    clock.tick(FPS)
    # Otherwise, collect the list/dictionary of all the keys that were
    # pressed
    pressedKeys = pygame.key.get_pressed()
    
    # and then send that dictionary to the Person object for them to
    # update themselves accordingly.

    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    Over_font = pygame.font.SysFont('Comic Sans MS', 100)
    lives_display = my_font.render(f"Health: {lives}",False,(0,0,0))
    scores_display = my_font.render(f"Score: {scores}",False, (0,0,0))
    gOver_display = Over_font.render(f"GAME OVER!!!",False,(0,0,0))
    
    if(lives > 0):
        #player_sprites.update(pressedKeys)
        wizard.update(pressedKeys)
        bullets.update()
        enemies.update()
        
        # fill the screen with a color
        screen.fill(WHITE)
        player_sprites.draw(screen)
        enemies.draw(screen)
        bullets.draw(screen)
        collided(enemies,bullets)

    else:
        screen.blit(gOver_display, (200, HEIGHT-500))
        
    
    screen.blit(lives_display, (0,HEIGHT-750))
    screen.blit(scores_display, (0,HEIGHT-790))
    pygame.display.flip()

