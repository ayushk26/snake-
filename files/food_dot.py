import pygame
from .distance import distance

class Food():

    def __init__(self,screen,x,y):
        self.screen =screen
        self.food_dot =pygame.image.load('./files/assets/dot.png')
        self.food_state = "active"
        self.x =x
        self.y =y
        self.state = 'not_eaten'
    def draw(self):
        if self.food_state == "active":
            self.screen.blit(self.food_dot, (self.x, self.y))

    def eaten(self,object,dot):
        self.dot =dot
        self.object =object
        if distance(self.dot.x,self.dot.y,self.x,self.y) <= 30:
            self.x =10000
            self.y =10000
            self.state = 'eaten'