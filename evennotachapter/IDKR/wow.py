from pycat.base.event.mouse_event import MouseEvent
from pycat.core import Window, Sprite, Color
import random

WWEIDTH = 690
WHEIGHT = 600
GAP =25

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
        
cguess = []
class Checkb(Sprite):
    a = 0
    b = 0
    def on_create(self):
        self.image = "button.png"
        self.scale = 0.45

        self.x = w.width - self.width/2-GAP
        self.y = 100 

    def make_new(self):
        a=0
        b=0
        for i in range(4):
            gcolor0 = w.create_sprite(Colorguess)
            gcolor0.x += (color0.width + GAP)* i
            cguess.append(gcolor0)
        ccode.clear()        
        for i in range(len(colist)):
            ccode.append(color01)
  
    

    def on_click(self, mouse_event: MouseEvent):
        a=0
        b=0
        for i in range(len(colist)):
            if ccode[i].color == cguess[i].color:
                a += 1
                cguess.remove([i])
                ccode.remove([i])
            
        # for j in range(len(cguess)):
        #     if ccode[j].color == cguess[j].color:
        #         b +=1

            
        print(str(a) + "a")
        print(str(b) + "b")
        
        if a == 4:
            print("You,winR!")     
            w.close()
        self.make_new()
   
        print("---------------------------------")
        


class Colorguess (Sprite):
    basiccolor = None
    
    def on_create(self):
        self.scale = 60
        self.x = 100
        self.y = 140+GAP
        self.color = Color.WHITE
    
    def on_click(self, mouse_event: MouseEvent):
        self.color = ColorChoice.currentcolor

class Colorcode (Sprite):
    def on_create(self):
        self.scale = 60
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

frist = botton.make_new()

w.run()