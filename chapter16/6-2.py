from ctypes import c_wchar
from pycat.base.event.mouse_event import MouseEvent
from pycat.core import Window, Sprite, Color
import random

WWEIDTH = 800
WHEIGHT = 900
GAP =25

w = Window(width=WWEIDTH,height=WHEIGHT)

class ColorChoice (Sprite):
    currentcolor = None

    def on_create(self):
        self.scale = 100
        self.x = 100
        self.y = 100 
    
    def on_click(self, mouse_event: MouseEvent):  
        ColorChoice.currentcolor = self.color

colist = [Color.RED, Color.BLUE, Color.YELLOW, Color.GREEN]

class Checkb(Sprite):

    def on_create(self):
        self.image = "button.png"
        self.scale = 0.5
        self.x = w.width - self.width/2-GAP
        self.y = 100 

    def on_click(self, mouse_event: MouseEvent):
        for i in range(len(colist)):
            if ccode[i].color == cguess[i]:
                print("yeah~~~")
        print("---------------------------------")

class Colorguess (Sprite):
    basiccolor = None
    
    def on_create(self):
        self.scale = 100
        self.x = 100
        self.y = 200+GAP
        self.color = Color.WHITE
    
    def on_click(self, mouse_event: MouseEvent):
        self.color = ColorChoice.currentcolor

class Colorcode (Sprite):
    def on_create(self):
        self.scale = 100
        self.x = 100
        self.y = w.height - 100       

botton = w.create_sprite(Checkb) 

colist = [Color.RED, Color.BLUE, Color.YELLOW, Color.GREEN]


for i in range(len(colist)):
    color0 = w.create_sprite(ColorChoice)
    color0.color = colist[i] 
    color0.x += (color0.width + GAP)* i

ccode = []
for i in range(len(colist)):
    color01 = w.create_sprite(Colorcode)
    color01.color = random.choice(colist)  
    color01.x += (color01.width + GAP)* i
    ccode.append(color01)
        
cguess = []
for i in range(4):
    gcolor0 = w.create_sprite(Colorguess)
    gcolor0.x += (color0.width + GAP)* i
    cguess.append(gcolor0)  


w.run()