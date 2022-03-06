from pycat.core import Window, Sprite, Color, Label

import random

w = Window()

list01 = []

for i in range (20):     
    list01.append([random.randint(0,255) for j in range(49)] )

class Cell(Sprite):

    def on_create(self):
        self.width = 21
        self.height = 21
        
    
    def llabel(self, value, min , max):
        r = random.randint(0,255)
        cell0 =  w.create_label()
        cell0.x = self.x
        cell0.y = self.y
        cell0.color = Color.CYAN
        cell0.font_size = 4
        cell0.text = str(value)
        cc = 255*(value - min)/(max - min)
        # ld = [[r-cc,r-cc,r-cc],[r-cc,r-cc,cc],[r-cc,cc,r-cc],[],[]]
        self.color = (r-cc, cc, r -cc)      


        
min_v = max_v = list01[0][0]

for i in range(len(list01)):
    for j in range(len(list01[i])):
        v = list01[i][j]
        if v < min_v :
            min_v = v
        if v > max_v :
            max_v = v  


for i in range(len(list01)):
    for j in range(len(list01[i])):
        cell01 = w.create_sprite(Cell)
        cell01.x = 100 + j*(cell01.width+ 1)
        cell01.y = 600 - i*(cell01.height+ 1)
        cell01.llabel(list01[i][j], min_v, max_v)


w.run()