import pygame as pg
import sys
from settings import *

class Game:
    def __init__(self):
        self.win = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()

    def window(self):
        self.win.fill(BLACK)
        self.clock.tick(FPS)
        pg.display.set_caption(f"Motorcycle game {self.clock.get_fps() : .1f} ")

    def events(self):
        for events in pg.event.get():
            if events.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def collision(self):
        pass


    def update(self):
        self.window()
        self.events()
