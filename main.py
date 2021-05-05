# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame
import sys
import math
import random

pygame.init()

def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))



class Snake():

    def __init__(self, screen):
        self.snake_dot = pygame.image.load('dot.png')
        self.screen = screen
        self.speed = 1
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

        if distance(self.object.tapx, self.object.tapy, self.x, self.y) <= 0.01:
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



class Food():

    def __init__(self,screen,x,y):
        self.screen =screen
        self.food_dot =pygame.image.load('dot.png')
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








def run_game():
    screen = pygame.display.set_mode((1000,700))
    pygame.display.set_caption("Snake")
    back_color = (255, 255, 255)
    score = 0
    snake1 = Snake(screen)
    number = 5
    dot = []
    for i in range(0, number):
        dot.append(i + 1)

    for i in range(0, number):
        dot[i] = Snake(screen)
    food= Food(screen,random.randint(30,960),random.randint(30,664))
    snakex = 250
    snakey = 250
    for i in range(0, number):
        dot[i].x = snakex
        dot[i].y = snakey + (i + 1) * 32

    state = "rest"
    font = pygame.font.Font('freesansbold.ttf', 64)
    fontf = pygame.font.Font('freesansbold.ttf', 32)
    fontf2 = pygame.font.Font('freesansbold.ttf', 40)
    score_font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('GAME OVER ', True, (0,0,0),(255,255,255))
    text1 = fontf.render('Press Space to Restart ', True, (0,0,0),(255,255,255))
    score_text = 'Score : '+str(score)
    scores = score_font.render(score_text, True, (0,0,0),(255,255,255))
    start_texts ='Controls: Left( < Key) Right( > Key) ,to start forward (^ Key)'
    start_text1 = fontf.render( start_texts, True, (0,0,0),(255,255,255))
    start_texts1 = 'Stay away from the Borders'
    start_text = fontf.render(start_texts1, True, (0, 0, 0), (255, 255, 255))
    start_texts2 = 'GET READY FOR A RIDE!!!'
    start_text2 = fontf2.render(start_texts2, True, (255, 0, 0), (255, 255, 255))


    running = True
    while running:

        screen.fill(back_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if distance(dot[0].x, dot[0].y, dot[0].tapx, dot[0].tapy) >= 32:
                        dot[0].tapx = dot[0].x
                        dot[0].tapy = dot[0].y

                        if dot[0].turns == 90:
                            dot[0].vx = -1 * dot[0].speed
                            dot[0].vy = 0
                        if dot[0].turns == 0:
                            dot[0].vy = -1 * dot[0].speed
                            dot[0].vx = 0
                        if dot[0].turns == 180:
                            dot[0].vy = 1 * dot[0].speed
                            dot[0].vx = 0
                        if dot[0].turns == 270:
                            dot[0].vx = 1 * dot[0].speed
                            dot[0].vy = 0
                        dot[0].turns += 90
                        dot[0].turns = dot[0].turns % 360
                        flag = "left"
                        state = "motion"

                if event.key == pygame.K_RIGHT:
                    if distance(dot[0].x, dot[0].y, dot[0].tapx, dot[0].tapy) >= 32:
                        snake1.tapx = snakex
                        snake1.tapy = snakey
                        dot[0].tapx = dot[0].x
                        dot[0].tapy = dot[0].y

                        if dot[0].turns == 90:
                            dot[0].vx = 1 * dot[0].speed
                            dot[0].vy = 0
                        if dot[0].turns == 0:
                            dot[0].vy = 1 * dot[0].speed
                            dot[0].vx = 0
                        if dot[0].turns == 180:
                            dot[0].vy = -1 * dot[0].speed
                            dot[0].vx = 0
                        if dot[0].turns == 270:
                            dot[0].vx = -1 * dot[0].speed
                            dot[0].vy = 0
                        dot[0].turns += 270
                        dot[0].turns = dot[0].turns % 360
                        flag = "right"
                        state = "motion"
                if event.key == pygame.K_UP:
                    state = "motion"

        if state == "rest":
            for i in range(0, number):
                dot[i].draw(snakex, snakey + (i + 1) * 32)
            screen.blit(start_text1, (25, 160))
            screen.blit(start_text, (25, 200))
            screen.blit(start_text2, (350, 250))

        if state == "motion":
            # moving condition
            for i in range(0, number):
                dot[i].x += dot[i].vx
                dot[i].y += dot[i].vy
                dot[i].draw(dot[i].x, dot[i].y)

                if dot[i].turns % 360 == 0:
                    dot[i].dir = "right"
                if dot[i].turns % 360 == 90:
                    dot[i].dir = "up"
                if dot[i].turns % 360 == 180:
                    dot[i].dir = "left"
                if dot[i].turns % 360 == 270:
                    dot[i].dir = "down"

            for i in range(1, number):
                dot[i].follow(dot[i -1])

            # food eaten condition
            if food.state != 'eaten':
                food.draw()
            food.eaten(food,dot[0])
            if food.state == 'eaten':
                food = Food(screen,random.randint(30,960),random.randint(30,664))
                dot.append(number)
                dot[number] = Snake(screen)
                dot[number].add(dot[number-1])
                dot[number].follow(dot[number-1])
                number +=1
                score += 1
                for i in range(0,number):
                    dot[number-i-1].speed += 0.0001



        # Boundary hitting condition
        if dot[0].x <= 0 or dot[0].x >= 970 or dot[0].y <=0 or dot[0].y>= 670:
            while (True):
                screen.blit(text, (325, 300))
                screen.blit(scores, (600, 30))
                #screen.blit(text1,(330,360))
                pygame.display.flip()
                for i in range (0,number):
                    dot[i].speed = 0
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running =False
                        sys.exit()
                        break

        score_text = 'Score : ' + str(score)
        scores = score_font.render(score_text, True, (0, 0, 0), (255, 255, 255))
        screen.blit(scores,(600,30))
        pygame.display.flip()
        for i in range(1, number):
            if distance(dot[i].x, dot[i].y, dot[0].x, dot[0].y) <= 12:
                score += -1*int((number-i)*0.7)
                number =i
                break


run_game()
