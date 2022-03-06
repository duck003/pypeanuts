from os import waitpid
from types import BuiltinFunctionType
from pycat.window import Window
from pycat.sprite import Sprite
from pyglet import sprite


o = Window()

w = o.create_sprite()
w.image = "forest_background.jpg"
w.scale=1.125
w.x=600
w.y=325



class Wow(Sprite):
    def on_create (self):
        self.image="owl.png"
        self.y=199
    def on_update(self, dt):
        self.x +=4
        if self.x<=600:
            self.scale+=0.0025
        if self.x>=600:
            self.scale-=0.0025
    
    def on_left_click(self):
        print("wow") 

class Wowo(Sprite):
    def on_create (self):
        self.image="owl.gif"
        self.y=399
    def on_update(self, dt):
        self.x +=4
        if self.x<=600:
            self.scale+=0.0025
        if self.x>=600:
            self.scale-=0.0025
    
    def on_left_click(self):
        print("wow") 

class Wowow(Sprite):
    
    def on_create (self):
        self.image="rooster.png"
        self.y=499
    def on_update(self, dt):
        self.x +=4
        if self.x<=600:
            self.scale+=0.0025
        if self.x>=600:
            self.scale-=0.0025
    
    def on_left_click(self):
        print("wow") 



o.create_sprite(Wow)
o.create_sprite(Wowo)
o.create_sprite(Wowow)
o.run()