from pycat.core import Window, Sprite, Color
from random import randint

w = Window(width = 1200 , height = 600)

class Jdot (Sprite):

    def on_create(self):
        self.goto_random_position()
        self.color = Color.random_rgb()
        self.scale = randint(20,160) 
        self.po = randint(1, 4)

    def on_update(self, dt):
        if self.po == 1 :
            self.y -= 10
        if self.po == 2 :
            self.x -= 10
        if self.po == 3 :
            self.y += 10
        if self.po == 4 :
            self.x += 10

for i in range (60):
    w.create_sprite(Jdot)


w.run()