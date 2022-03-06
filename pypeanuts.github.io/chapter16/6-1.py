from pycat.base.event.mouse_event import MouseEvent
from pycat.core import Window, Sprite, Color
import random

WWEIDTH = 800
WHEIGHT = 900
GAP =25

w = Window(width=WWEIDTH,height=WHEIGHT)

class ColorChoice (Sprite):
    
    def on_create(self):
        self.scale = 100
        self.x = 100
        self.y = 100 
    
    def on_click(self, mouse_event: MouseEvent):
        print("wow")


class Checkb(Sprite):

    def on_create(self):
        self.image = "button.png"
        self.scale = 0.5
        self.x = w.width - self.width/2-GAP
        self.y = 100 

class Colorguess (Sprite):
    
    def on_create(self):
        self.scale = 100
        self.x = 100
        self.y = 200+GAP
    
    def on_click(self, mouse_event: MouseEvent):
        pass


botton = w.create_sprite(Checkb) 

colist = [Color.RED, Color.BLUE, Color.YELLOW, Color.GREEN]
for i in range(len(colist)):
    color0 = w.create_sprite(ColorChoice)
    color0.color = colist[i] 
    color0.x += (color0.width + GAP)* i
        

for i in range(4):
    golor0 = w.create_sprite(Colorguess)
    color0.color = colist[i] 
    golor0.x += (color0.width + GAP)* i

w.run()