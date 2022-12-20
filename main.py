import pygame as pg
import sys
from levels import *
from player import *
from settings import *
from world import *
from game import *

game = Game()
world = World(game.win)

if __name__ == "__main__":
    
    while True:
        game.update()
        world.update()
        pg.display.update()
