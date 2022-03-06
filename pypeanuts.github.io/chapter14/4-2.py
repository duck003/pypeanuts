from pycat.core import Window, Sprite, Color
import random

w = Window()

class Tur (Sprite):
    
    def on_create(self):
        self.time = 0

    def drawr(self,r):
        A = self.position
        self.move_forward (r)
        B = self.position
        self.rotation += 120
        self.move_forward (r)
        C =self.position
        ab = w.create_line(A.x, A.y, B.x, B.y, color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        bc = w.create_line(B.x, B.y, C.x, C.y, color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        ca = w.create_line(C.x, C.y, A.x, A.y, color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    
    def on_update(self, dt):
        w.clear_drawables()
        self.time += 50*dt
        for i in range(40) :
            self.drawr(240+i)
            self.position = w.mouse_position
            self.rotation += self.time
        


t:Tur = w.create_sprite(Tur)
t.position = w.center
t.position = (t.x , t.y - 90)

 
w.run()