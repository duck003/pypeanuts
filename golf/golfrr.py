from pycat.core import Window, Sprite, Point,Color
from pycat.base.event import MouseEvent
from math import sqrt

from sqlalchemy import false
from tables import NoSuchNodeError

w = Window()

class Golf(Sprite):

    def on_create(self):
        self.aim = w.create_line(width=6) 
        self.scale = 26
        self.color = Color.BLUE
        self.position = (100,100)   
        self.speed = 0
        self.aiming = True
        self.l = NoSuchNodeError

    def on_update(self, dt):
        if self.aiming:
            self.l = w.mouse_position - self.position
            if self.l.x == 0 and self.l.y == 0:
                self.aim.set_start_end(self.position,self.position)
            else:
                self.l.normalize()
                self.aim.set_start_end(self.position,self.position + 100*l)
        
        else:
            self.position += self.l
            
        
    def on_click_anywhere(self, mouse_event: MouseEvent):
        if self.aiming == True:
            self.aiming = False
        else:
            self.aiming = True

golf = w.create_sprite(Golf)
w.run()