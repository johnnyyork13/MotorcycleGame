import pygame as pg
from levels import *
import random
from settings import *
from obstacle import *

class World:
    def __init__(self, win):
        self.win = win
        self.obstacle_num = 0
        self.obstacle_list = []

    def spawn_obstacle(self):
        random_x = random.randint(1000, 2000)
        random_y = random.randint(1,3)

        if random_y == 1:
            random_y = SCREEN_HEIGHT - 200
        elif random_y == 2:
            random_y = SCREEN_HEIGHT - 150
        elif random_y == 3:
            random_y = SCREEN_HEIGHT - 100

        obstacle = Obstacle(self.win, random_x, random_y)

        self.obstacle_list.append(obstacle)
    
    def move_obstacles(self, obstacle_list):
        for obstacles in obstacle_list:
            obstacles.x -= OBSTACLE_VEL
            obstacles.update()  

    def delete_obstacle(self):
        for obstacle_id, obstacles in enumerate(self.obstacle_list):
            if obstacles.x < 0 - OBSTACLE_WIDTH:
                self.obstacle_list.pop(obstacle_id)

    def obstacle_update(self):
        if len(self.obstacle_list) < 2:
            self.spawn_obstacle()

        self.move_obstacles(self.obstacle_list)
        self.delete_obstacle()


    def move_background(self):
        pass

    def draw(self):
        pass

    def update(self):
        self.obstacle_update()

