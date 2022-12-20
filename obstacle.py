import pygame as pg
from settings import *

class Obstacle:
    def __init__(self, win, x, y):
        self.win = win
        self.x = x
        self.y = y
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT
        self.vel = OBSTACLE_VEL

    def draw(self):
        #pg.draw.rect(self.win, WHITE, (50,50,50,50))
        print(self.x, self.y)
        pg.draw.rect(self.win, RED, (self.x, self.y, self.width, self.height))

    def update(self):
        self.draw()