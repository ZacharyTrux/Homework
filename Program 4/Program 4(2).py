import pygame
import Constants

class Entity:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    @property    
    def x(self):
        return self._x
    @x.setter
    def x(self,value):
        self._x = value
        
    @property    
    def y(self):
        return self._y
    @y.setter
    def y(self,value):
        self._y = value
        
class Wizard(Entity, pygame.sprite.Sprite):
    def __init__(self,x,y):
        Entity().__init__(self,x,y)
        pygame.sprite.Sprite().__init__(self)
        self.image = pygame.image.load("Program 4/Images/wizard.png").convert_alpha()
        self.image.set_colorkey((0,0,0), RLEACCEL)
        self.image = pygame.transform.scale(self.image,(150,150))
    