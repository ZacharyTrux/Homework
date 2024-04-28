import pygame
from Constants import *

#create a domain expansion ability (gojoat abilities)
#make the spider sukana 
#profit 



#set the frame rate of the screen to 60 (helps with smoothness of game)
clock = pygame.time.Clock()
FPS = 60
        
        
class Spider(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Program 4/Images/spider.png").convert_alpha()
        # sets the size of the image 
        self.image = pygame.transform.scale(self.image,(150,150))
        # makes the image a rectangle, making it easy to use x and y coordinates and changing them
        self.rect = self.image.get_rect()
        # sets the x and y positions for the spider when the game starts
        self.setRandomPosition()
        
    def setRandomPosition(self):
        # have spider go to a random position in a range above the player
        self.rect.center = (0,randint(0,HEIGHT-300))
    
    # handles all of the movement with the spider including changing the lives counter when it reaches a section of the screen
    def update(self):
        global lives
        
        self.rect.x += 10
        if(self.rect.right > WIDTH):
            # reset spider and change lives count
            self.setRandomPosition()
            lives -= 1
            

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("Program 4/Images/Bolt.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        # sets the coordinates of the rectangle to be the same as the wizard when spawned in
        self.rect.center = (x,y)
    
    def update(self):
        self.rect.y -= 10
        
        if self.rect.bottom < 0:
            # gets rid of the bullet from the sprite group
            self.kill()
        

class Wizard(pygame.sprite.Sprite):
    # interval of shots being spaced out between each other
    cooldown = 30
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Program 4/Images/wizard.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(150,150))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT - 100)
        
    def goLeft(self):
        # changes players x coordinates to a set speed
        self.rect.move_ip(-5,0)
        if(self.rect.centerx < 0):
            # stops the player if it reaches the left side of the screen 
            self.rect.centerx = 0 

    def goRight(self):
        self.rect.move_ip(5,0)
        if(self.rect.centerx > WIDTH):
            # stops the player if it reaches the right side of the screen 
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
    
    # attempts to shoot, not doing shoot function if cooldown hasn't reached 0
    def try_shooting(self):
        if(self.cooldown == 0):
            self.shoot()
            self.cooldown = 30
    
    # creates a bullet and adds it to the bullets sprite group (taking in x and y cordinates from wizard)
    def shoot(self):
        bullet = Bullet(self.rect.centerx,self.rect.top)
        bullets.add(bullet)
        
        



    

################## MAIN ########################
# Initialize pygame library and display
################################################

# set up screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# creates the wizard sprite group and adds the player into it
player_sprites = pygame.sprite.Group()
wizard = Wizard()
player_sprites.add(wizard)

# creates the enemies group which the spider will be added into
enemies = pygame.sprite.Group()
spiders = Spider()           
enemies.add(spiders)

# creates the bullets sprite group which will add bullets when the player shoots 
bullets = pygame.sprite.Group()

global scores
score = 0

global lives
lives = 3

def collided(enemies,bullets):
    global score
    
    # accounts for when the bullet and spider sprite make contact
    collisions = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for enemy, bullet_list in collisions.items():
        # gets the spider out of the group
        enemy.kill()
        # create new spider to run across screen
        spiders = Spider()
        enemies.add(spiders)
        
        # gets rid of the bullet which collided in the list 
        for bullet in bullet_list:
            bullet.kill()
        
        score+= 1

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
            
    # sets the FPS in game      
    clock.tick(FPS)
    
    # Otherwise, collect the list/dictionary of all the keys that were pressed
    pressedKeys = pygame.key.get_pressed()
    

    # create the texts needed for the display on screen
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    Over_font = pygame.font.SysFont('Comic Sans MS', 100)
    lives_display = my_font.render(f"Health: {lives}",False,(0,0,0))
    death_display = my_font.render(f"Health: {0}",False,(0,0,0))
    scores_display = my_font.render(f"Score: {score}",False, (0,0,0))
    gOver_display = Over_font.render(f"GAME OVER!!!",False,(0,0,0))
    
    # fill the screen with a color
    screen.fill(WHITE)
    
    # loops game if player still has lives 
    if(lives > 0):
        #player_sprites.update(pressedKeys)
        wizard.update(pressedKeys)
        bullets.update()
        enemies.update()
        
        
        # put sprites on the screen
        player_sprites.draw(screen)
        enemies.draw(screen)
        bullets.draw(screen)
        
        # account for sprites colliding
        collided(enemies,bullets)

    # inform player they lost
    elif(lives == 0):
        # put sprites on the screen
        player_sprites.draw(screen)
        enemies.draw(screen)
        bullets.draw(screen)
        
        screen.blit(gOver_display, (200, HEIGHT-500))  
    
    # puts the health and score onto the screen
    screen.blit(lives_display, (0,HEIGHT-750))
    screen.blit(scores_display, (0,HEIGHT-790))
    
    # updates the screen
    pygame.display.flip()

