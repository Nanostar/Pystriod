import pygame
from circleshape import *


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        velocity = (0,0)
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        self.position += (self.velocity * dt) 
        