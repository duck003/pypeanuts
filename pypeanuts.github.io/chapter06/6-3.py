from pycat.core import Sprite, Window, Color 
import random

w = Window()
color0101 = [(225,225,225),(225,0,0),(0,0,225),(0,225,0),(0,0,0)]

class ColorButton(Sprite):

    def on_left_click(self):
        for p in w.get_sprites_with_tag('particle'):
            p.color = self.color


class Particle(Sprite):

    def on_create(self):
        self.add_tag('particle')
        self.color = Color.random_rgb()
        self.goto_random_position()
        self.rotation = random.randint(0,360)
        self.scale = 2  

    def on_update(self, dt):
        self.move_forward(5)
        if self.touching_window_edge():
            self.rotation += 180    

class Button01(Sprite):

    def on_left_click(self):
        
        for i in range (1,100):
            w.create_sprite(Particle)

class Button02(Sprite):
    def on_left_click(self):
        w.delete_sprites_with_tag('particle')
        
color01 = w.create_sprite(ColorButton, x=900, y=100, color=(0,0,255), scale=50) 
color02 = w.create_sprite(ColorButton, x=450, y=100, color=(0,255,0), scale=50) 
botton01 =w.create_sprite(Button01, x=100, y=100, color=(255,0,0), scale=50)
botton02 =w.create_sprite(Button02, x=1200, y=100, color=(255,255,255), scale=50)
w.run()