import pygame
import math
#CONSTANTS
LEFT = 0
RIGHT = 1
DOWN = 2
UP = 3
SPACE = 4
W = 5

class fireball:
    def __init__(self):
        self.xpos = -10 #draw offscreen when not in use
        self.ypos = -10
        self.isAlive = False
        self.direction = RIGHT
        
    def shoot(self, x, y, dir):
        self.xpos = x + 20 #start fireball at center of player
        self.ypos = y + 20
        self.isAlive = True
        self.direction = dir
        
    def move(self):
        if self.direction == RIGHT:
            self.xpos+=20
        elif self.direction == LEFT:
            self.xpos-=20
        if self.direction == DOWN:
            self.ypos+=20
        elif self.direction == UP:
            self.ypos-=20
        
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.xpos, self.ypos), 10)
        pygame.draw.circle(screen, (250, 250, 0), (self.xpos, self.ypos), 5)
        
    def collide(self, x, y):
        #distance formula for circular collision
        if math.sqrt((self.xpos - x) ** 2 + (self.ypos - y) ** 2) < 25:
            print("collision!")
            return True
        else:
            return False
        