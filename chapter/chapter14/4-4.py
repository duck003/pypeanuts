import random
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
        w.create_line(x1,y1,self.x,self.y)

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
# for i in range (360):
#     t.draw_rect(200,200)
#     t.rotation += 1 

class Building:


    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.width  = w
        self.height = h
    
    def draw (self,t:Tur):
        t.rotation = 0
        t.x ,t.y = self.x,self.y
        t.draw_rect(self.width,self.height)

b = Building(10,40,60,423)
for i in range (21):
    b.draw(t)
    b.x += 60
    b.height += random.randint(-40,40)

w.run()