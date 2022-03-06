from pycat.window import Window
from pycat.sprite import Sprite, RotationMode
from pycat.keyboard import KeyCode
from pycat.scheduler import Scheduler
from pycat.collision import is_aabb_collision
from pycat.label import Label
import random

from pyglet.text.layout import ScrollableTextLayout
from pyglet.window.key import UP

w = Window(background_image="underwater_04.png")

class Ship(Sprite):

    def on_create(self):
        self.image='saucer.png'
        self.y = 490
        self.scale = float(0.25)
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.add_tag("spaceship")
        self.score = 0
    def on_update(self, dt):
        self.move_forward(4)
        if self.touching_window_edge():
            self.rotation += 180

ship = w.create_sprite(Ship)

score = Label("How many Alien have been saved?", x=600 , y=600)

class Alien(Sprite):

    def on_create(self):
        self.image = random.choice(["1.png","2.png","3.png","5.png"])
        self.scale = float(0.25) 
        self.goto_random_position()
        self.y = 46
        self.is_moving_up = False

    def on_update(self, dt):
        if self.is_moving_up :
            self.y += 66
            if self.touching_any_sprite_with_tag("spaceship"):
                self.delete()
                ship.score +=1
                print(ship.score)
                
            
            if self.touching_window_edge():
                ship.score -= 1
                print(ship.score)
                self.delete()
        
        if w.get_key (KeyCode.UP):
            self.is_moving_up = True

def Alen(dt):
    w.create_sprite(Alien)


Scheduler.update(Alen, delay=0.001)

w.run()