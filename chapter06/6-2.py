from pycat.core import Sprite, Window
import random

w = Window()

class ColorButton(Sprite):

    def on_left_click(self):
        for p in w.get_sprites_with_tag('particle'):
            p.color = self.color


class Particle(Sprite):

    def on_create(self):
        self.add_tag('particle')
        self.color = (0,0,255)
        self.goto_random_position()
        self.rotation = random.randint(0, 360)
        self.scale = 2  

    def on_update(self, dt):
        self.move_forward(5)
        if self.touching_window_edge():
            self.rotation += 180    

for i in range(100):
    w.create_sprite(Particle)

color01 = w.create_sprite(ColorButton, x=100 , y=100, color=(0,0,255), scale=100) 
color02 = w.create_sprite(ColorButton, x=1200, y=100, color=(0,255,0), scale=100) 

w.run()
