import random
from pycat.core import Window, Sprite, Color

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
        # self.draw_forward(width)
        # self.rotation += 90
        # self.draw_forward(height)  
        # self.rotation += 90
        # self.draw_forward(width)
        # self.rotation += 90
        # self.draw_forward(height)
        # self.rotation += 90
        w.create_rect(self.x,self.y,width,height,color=Color.random_rgb())
    
t = w.create_sprite(Tur)
# for i in range (360):
#     t.draw_rect(200,200)
#     t.rotation += 1 

class Window01:
    
    def __init__(self,x,y,w,h): 
        self.width  = w
        self.height = h
        self.x = x
        self.y = y
    
    def draw (self,t:Tur):
        t.rotation = 0
        t.x ,t.y = self.x,self.y
        t.draw_rect(self.width,self.height)

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
        for i in range (4):
            ww01 = Window01(self.x + self.width/2,self.height/2,self.width/4,self.height/4)
            ww01.draw(t)
            ww02 = Window01(self.x + self.width/2-self.width/4,self.height/2,self.width/4,self.height/4)
            ww02.draw(t)
            ww03 = Window01(self.x + self.width/2-self.width/4,self.height/2+self.height/4,self.width/4,self.height/4)
            ww03.draw(t)
            ww04 = Window01(self.x + self.width/2,self.height/2+self.height/4,self.width/4,self.height/4)
            ww04.draw(t)

for i in range (21):
    h = random.randint(200,400)
    b = Building(10*i*6+10,40,60 ,h)
    b.draw(t)

w.run()