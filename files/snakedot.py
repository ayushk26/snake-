import pygame
from .distance import distance

pygame.init()

class Snake():

    def __init__(self, screen):
        self.snake_dot = pygame.image.load('./files/assets/dot.png')
        self.screen = screen
        self.speed = 0.8
        self.distance = []
        self.turns = 90
        self.x = 0
        self.y = 0
        self.tapy = 0
        self.tapx = 0
        self.vx = 0
        self.vy = -1 * self.speed

        if self.turns % 360 == 0:
            self.dir = "right"
        if self.turns % 360 == 90:
            self.dir = "up"
        if self.turns % 360 == 180:
            self.dir = "left"
        if self.turns % 360 == 270:
            self.dir = "down"

    def draw(self, x, y):
        self.screen.blit(self.snake_dot, (x, y))

    def follow(self, object):
        self.object = object

        if distance(self.object.tapx, self.object.tapy, self.x, self.y) <= 0.04:
            self.tapx = self.x
            self.tapy = self.y
            # Conditions of turning
            if self.object.turns - self.turns == 90 or self.object.turns - self.turns == -270:
                if self.object.dir == "up":
                    self.vx = 0
                    self.vy = -1 * self.speed
                    self.turns += 90
                    self.turns = self.turns % 360
                if self.object.dir == "left":
                    self.vy = 0
                    self.vx = -1 * self.speed
                    self.turns += 90
                    self.turns = self.turns % 360
                if self.object.dir == "down":
                    self.vx = 0
                    self.vy = self.speed
                    self.turns += 90
                    self.turns = self.turns % 360
                if self.object.dir == "right":
                    self.vy = 0
                    self.vx = self.speed
                    self.turns += -270
                    self.turns = self.turns % 360

            if self.object.turns - self.turns == -90 or self.object.turns - self.turns == 270:

                if self.object.dir == "up":
                    self.vx = 0
                    self.vy = -1 * self.speed
                    self.turns += -90
                    self.turns = self.turns % 360
                if self.object.dir == "left":
                    self.vy = 0
                    self.vx = -1 * self.speed
                    self.turns += -90
                    self.turns = self.turns % 360
                if self.object.dir == "down":
                    self.vx = 0
                    self.vy = self.speed
                    self.turns += 270
                    self.turns = self.turns % 360
                if self.object.dir == "right":
                    self.vy = 0
                    self.vx = self.speed
                    self.turns += -90
                    self.turns = self.turns % 360

    def add(self,object):

        self.object = object
        self.dir = object.dir
        self.vx =self.object.vx
        self.vy =self.object.vy
        self.turns = self.object.turns
        if self.dir =='right':
            self.start_x = self.object.x - 32
            self.start_y = self.object.y
        if self.dir =='left':
            self.start_x = self.object.x + 32
            self.start_y = self.object.y
        if self.dir =='up':
            self.start_y = self.object.y + 32
            self.start_x = self.object.x
        if self.dir =='down':
            self.start_y = self.object.y - 32
            self.start_x = self.object.x
        self.x = self.start_x
        self.y = self.start_y