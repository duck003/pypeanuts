import random
from pycat.base.color import Color
from pycat.core import Window, Sprite

w = Window()

rest = 0

class Tur(Sprite):

    global rest
    def on_create(self):
        self.position = w.center
        # self.x -= 100
        # self.y -= 100
    def on_update(self, dt):
        pass

    def draw_forward(self,res):
        rest = res
        x1 = self.x
        y1 = self.y
        self.move_forward(rest)
        w.create_line(x1,y1,self.x,self.y,color=Color.random_rgb())

    def draw_rect(self,width,height):
        self.draw_forward(width)
        self.rotation += 90
        self.draw_forward(height)  
        self.rotation += 90
        self.draw_forward(width)
        self.rotation += 90
        self.draw_forward(height)
        self.rotation += 90
    
t = w.create_sprite(Tur)
for i in range (360):
    t.draw_rect(200,200)
    t.rotation += 1 

w.run()