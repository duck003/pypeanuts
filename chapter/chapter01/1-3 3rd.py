from pycat.window import Window
from pycat.sprite import Sprite
from pycat.keyboard import KeyCode
from pycat.collision import is_aabb_collision
from pycat.scheduler import Scheduler
from pyglet import window

o = Window()
s = Scheduler()


w = o.create_sprite()
w.image = "forest_background.jpg"
w.scale=1.125
w.x=600
w.y=325



class Wow(Sprite):
    def on_create (self):
        self.image="owl.png"
        self.x=50
        self.y=600
    def on_update(self, dt):
        if o.get_key (KeyCode.W):
            self.y+=10
        if o.get_key (KeyCode.S):
            self.y-=10
        if o.get_key (KeyCode.A):
            self.x-=10
        if o.get_key (KeyCode.D):
            self.x+=10
            

    

class Wowow(Sprite):
    
    def on_create (self):
        self.image="rooster.png"
        self.x=50
        self.y=400

w = window.create_sprite()
w.image = "forest_background.jpg"
w.scale=1.125
w.x=600
w.y=325




oh = o.create_sprite(Wow)

ohma= o.create_sprite(Wowow)

def my_update():
    if is_aabb_collision(oh, ohma):
        print("Owl:Go away.")
        print("Rooster:No. For my dinner")
        window.quit

s.update(my_update)
o.run()
