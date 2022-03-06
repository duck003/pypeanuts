from pycat.base import color
from pycat.core import Color, KeyCode, Scheduler, Sprite, Window, Label, RotationMode
import random, time
w = Window(background_image="wowow.png")
class Player (Sprite):

    def on_create(self):
        self.add_tag("player")
        self.image = ("playc.png")
        self.scale = 0.24
        self.x = 100
        self.y = 300
        self.health = 100
        self.speed = 5
        self.time =  0
        self.bomb = 0  
    def on_update(self, dt):
        self.time += dt
        if w.get_key(KeyCode.UP):
            self.image = ("playc.png")
            self.scale = 0.24
            self.y += self.speed
        elif w.get_key(KeyCode.DOWN):
            self.image = ("playc00.png")
            self.scale = 0.24
            self.y -= self.speed    
        elif w.get_key(KeyCode.RIGHT):
            self.image = ("playc0.png")
            self.scale = 0.24
            self.x += self.speed 
        elif w.get_key(KeyCode.LEFT):
            self.image = ("playc0.png")
            self.scale = 0.24
            self.x -= self.speed
        elif w.get_key(KeyCode.Z):
            self.image = ("playc0.png")
            w.create_sprite(Player)

player01 = w.create_sprite(Player)

w.run()            