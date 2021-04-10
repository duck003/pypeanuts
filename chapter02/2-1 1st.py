from pycat.window import Window
from pycat.sprite import Sprite
from pycat.keyboard import KeyCode
from pycat.scheduler import Scheduler
from pycat.collision import is_aabb_collision
import random

w = Window(background_image="beach_03.png")

class Cat(Sprite):

    def on_create(self):
        self.image="cat.png"
        self.y=60
        self.x=60
        self.point = 0
    def on_update(self, dt):
        
        if w.get_key (KeyCode.UP):
            self.scale_x = 1
            self.rotation=90
            self.move_forward(10)
        if w.get_key (KeyCode.DOWN):
            self.scale_x = 1
            self.rotation=270
            self.move_forward(10)
        if w.get_key (KeyCode.LEFT):
            self.rotation=0
            self.scale_x = -1
            self.move_forward(-10)
        if w.get_key (KeyCode.RIGHT):
            self.rotation=0
            self.scale_x = 1
            self.move_forward(10)    

player = w.create_sprite(Cat)

class Gem(Sprite):

    def on_create(self):
        self.image = random.choice(["gem_shiny01.png","gem_shiny02.png","gem_shiny03.png","gem_shiny04.png","gem_shiny05.png"])
        self.scale=float(0.34)
        self.goto_random_position()
        self.y=600

    def on_update(self, dt):
        self.y -= 5
        if is_aabb_collision(self,player):
            self.delete()
            player.point += 1
            print(player.point)
        elif self.y <=0 :
            self.delete()
            player.point -= 1
            print(player.point)

def wow(dt):
    w.create_sprite(Gem)       

Scheduler.update(wow, delay=1)
    
w.run()

