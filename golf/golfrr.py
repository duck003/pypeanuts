from pycat.core import Window, Sprite, Point,Color
from math import sqrt

w = Window()

class Golf(Sprite):

    def on_create(self):
        self.aim = w.create_line(width=6) 
        self.scale = 26
        self.color = Color.BLUE
        self.position = (100,100)   
        self.speed = 0

    def on_update(self, dt):
        l = w.mouse_position - self.position
        if l.x == 0 and l.y == 0:
            self.aim.set_start_end(self.position,self.position)
        else:
            l.normalize()
            self.aim.set_start_end(self.position,self.position + 100*l)

golf = w.create_sprite(Golf)
w.run()