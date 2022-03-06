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
        self.y=300
    def on_update(self, dt):
        self.x +=1
        if self.x<=600:
            self.scale+=0.0025
        if self.x>=600:
            self.scale-=0.0025
    
    def on_left_click(self):
        print("wow") 
        
Wow=o.create_sprite(Wow)
o.run()