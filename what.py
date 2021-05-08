from pycat.core import Window
from random import randint
import random, time


w = Window(width = 1200 , height = 600)

from pycat.core import Window, Sprite, Color
from random import randint , choice


w = Window(width = 1200 , height = 600)

class Jdot (Sprite):

    def on_create(self):
        self.goto_random_position()
        self.color = Color.random_rgb()
        self.scale = randint(20,160) 
        self.po = 0
    def on_update(self, dt):
        ww = 1
        self.po += randint(1, 2)
        if self.po == 1 :
            for i in range(99):
                self.y += 10
                time.sleep(ww)
        if self.po == 2 :
            for i in range(99):
                self.x -= 1 
                time.sleep(ww)

for i in range (60):
    dot = w.create_sprite(Jdot)


w.run()