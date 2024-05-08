import pygame
import random
import math
LEFT = 0
RIGHT = 1
DOWN = 2
UP = 3
SPACE = 4
W = 5

class npc:
    def __init__(self):
        self.xpos = 100
        self.ypos = 500
        self.direction = RIGHT
        self.isAlive = True
        
    def draw(self, screen):
        if self.isAlive == True:
            #change color (to differentiate from enemy)
            pygame.draw.circle(screen, (0,0,250), (self.xpos, self.ypos), 20) #eventually swap with a sprite
            
    def move(self, ticker):
        #randomly wander:
        if ticker % 40 == 0: #mess with this number to make him change direction more or less often!
            num = random.randrange(0, 4)
            if num == 0:
                self. direction = RIGHT
            elif num == 1:
                self.direction = LEFT
            elif num == 2:
                self.direction = DOWN
            elif num == 3:
                self.direction = UP
                
        #check if player is direct line of sight
        if abs(int(py/50) - int(self.ypos/50))<2: #check that player and enmy are in same row
            if px < self.xpos: #check that player is to the left of enemy
                self.xpos-=5
                self.direction = LEFT
            else:
                self.xpos+=5
                self.direction = RIGHT
            
        if abs(int(py/50) - int(self.xpos/50))<2: #check that player and enmy are in same row
            if px < self.xpos: #check that player is to the left of enemy
                self.ypos+=5
                self.direction = DOWN
            else:
                self.ypos-=5
                self.direction = UP
