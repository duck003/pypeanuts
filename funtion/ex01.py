from pycat.core import Window, Sprite, KeyCode, Color
from sympy import Point
from player_contorl import Control2D

w = Window()

class Player01(Sprite):

    def on_create(self):
        self.scale = 72
        self.color = Color.CYAN
        self.position = w.center
        self.control = Control2D(KeyCode.UP, KeyCode.DOWN, KeyCode.LEFT, KeyCode.RIGHT, Point(0,1), Point(-1,0), self)
    
    def on_update(self, dt):
        self.control.update()

class Player02(Sprite):

    def on_create(self):
        self.scale = 72
        self.color = Color.RED
        self.position = w.center
        self.control = Control2D(KeyCode.W, KeyCode.S, KeyCode.A, KeyCode.D, Point(0,1), Point(-1,0), self)
    
    def on_update(self, dt):
        self.control.update()

w.create_sprite(Player01) 
w.create_sprite(Player02)          
w.run()