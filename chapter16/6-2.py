from ctypes import c_wchar
from pycat.base.event.mouse_event import MouseEvent
from pycat.core import Window, Sprite, Color
import random

WWEIDTH = 800
WHEIGHT = 960
GAP = 25
ccode = []
cguess = []

w = Window(width=WWEIDTH,height=WHEIGHT)

class ColorChoice (Sprite):
    currentcolor = None

    def on_create(self):
        self.scale = 60
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
        self.gtimes = 0
        self.a = 0
        self.b = 0
    
    def on_click(self, mouse_event: MouseEvent):
        self.count_ab()
        
        draw_a(self.gtimes,self.a)
        draw_b(self.gtimes,self.b)
        
        self.gtimes += 1
        if self.gtimes >= 8 :
            print("You loseR!")
            w.close()
        elif self.a < 4:
            make_a_new_row(self.gtimes)
        else:
            print("You WinR!")
        print("---------------------------------")
        self.a = 0
        self.b = 0  
   
    def  count_ab(self):
        mwcode = []
        mwguess = []
        for i in range(len(colist)):
            if ccode[i].color == cguess[i].color:
                self.a += 1
            else:
                mwcode.append(ccode[i].color)
                mwguess.append(cguess[i].color)
        for color in mwguess:
            if color in mwcode:
                self.b += 1
                mwcode.remove(color)
        print (str(self.a) + "a")
        print (str(self.b) + "b")
        
def draw_a(times,ar):
    for i in range(ar):
        s = w.create_sprite()
        s.scale = 25
        s.color = Color.RED
        s.x = botton.x - 100 + i*GAP*2
        s.y = 200 + times*80 +18

def draw_b(times,ar):
    for i in range(ar):
        s = w.create_sprite()
        s.scale = 25
        s.color = Color.WHITE
        s.x = botton.x - 100 + i*GAP*2
        s.y = 200 + times*80 -18


def make_a_new_row(times): 
    cguess.clear()
    for i in range(4):
        gcolor0 = w.create_sprite(Colorguess)
        gcolor0.x += (color0.width + GAP)* i
        gcolor0.y += times*80
        cguess.append(gcolor0)  
    

class Colorguess (Sprite):
    basiccolor = None
    
    def on_create(self):
        self.scale = 60
        self.x = 100
        self.y = 200
        self.color = Color.WHITE
    
    def on_click(self, mouse_event: MouseEvent):
        self.color = ColorChoice.currentcolor

class Colorcode (Sprite):
    def on_create(self):
        self.scale = 60
        self.x = 100
        self.y = w.height - 100  

class Blank (Sprite):
    def on_create(self):
        self.scale = 60
        self.x = 100
        self.y = w.height - 100      
        self.color = Color.WHITE
        
botton = w.create_sprite(Checkb) 

colist = [Color.RED, Color.BLUE, Color.YELLOW, Color.GREEN]


for i in range(len(colist)):
    color0 = w.create_sprite(ColorChoice)
    color0.color = colist[i] 
    color0.x += (color0.width + GAP)* i


for i in range(len(colist)):
    color01 = w.create_sprite(Colorcode)
    color01.color = random.choice(colist)  
    color01.x += (color01.width + GAP)* i
    ccode.append(color01)

def not_show_answer():
    for i in range(4):
        ncolor01 = w.create_sprite(Blank)
        ncolor01.color = Color.WHITE  
        ncolor01.x += (ncolor01.width + GAP)* i
        
start = make_a_new_row(0)

strat = not_show_answer()

w.run()