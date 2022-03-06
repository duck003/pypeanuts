from pycat.core import Window, Sprite, Color
from random import randint , choice


w = Window(width = 1200 , height = 600)

class Jdot (Sprite):

    def on_create(self):
        self.goto_random_position()
        self.color = Color.random_rgb()
        self.scale = randint(20,160) 

    def on_update(self, dt):
        self.y -= 10

for i in range (60):
    dot = w.create_sprite(Jdot)

w.run()