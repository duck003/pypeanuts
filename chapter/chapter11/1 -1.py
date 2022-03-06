from pycat.base.event.key_event import KeyCode
from pycat.base.event.mouse_event import MouseEvent
from pycat.core import Window, Sprite
from enum import Enum, auto


w = Window(background_image= "BG.png")

class PYstate (Enum):
    WAITING = auto()
    JUMPING = auto()
    RESTTING = auto()

class PF(Sprite):

    def on_create(self):
        self.image = "PF.PNG"
        self.add_tag("Pf")
        self.scale = 0.84


class PY(Sprite):

    def on_create(self):
        self.image = 'PYS.png'
        self.reset()
    
    def reset (self):
        self.y = w.height/2
        self.x = 100
        self.scale = 0.25
        self.x_speed = 0
        self.y_speed = 0
        self.state =PYstate.JUMPING
        self.rotation = 0

    def on_update(self, dt):
        if w.is_key_pressed(KeyCode.LEFT):
            self.x -= 10
        
        if w.is_key_pressed(KeyCode.RIGHT):
            self.x += 10
        
        # if w.is_key_down(KeyCode.UP):
        #     self.state = PYstate.JUMPING
        #     for i in range (self.y, self.y + dt,dt):
        #        if dt

        if self.state == PYstate.JUMPING:
            pre_y = self.y

            self.x += self.x_speed
            self.y += self.y_speed

            self.y_speed -= 1
        
            for p in pf:
                if self.is_touching_sprite(p):
                    top_y = p.height/2 + self.height/2 + p.y 
                    if pre_y > top_y :
                        self.y = top_y
                        self.state = PYstate.WAITING
            
            if self.is_touching_window_edge():
                self.x_speed = 0
                self.y_speed = 0
                
                self.state = PYstate.RESTTING
            
            
            elif self.is_touching_window_edge():
                self.x_speed = 0
                self.y_speed = 0
            
                self.state = PYstate.RESTTING
            elif self.is_touching_any_sprite_with_tag ("EY"):
                self.x_speed = 0
                self.y_speed = 0
            
                self.state = PYstate.RESTTING

        if self.state == PYstate.RESTTING:
            self.rotation +=5
            self.scale *= 0.98  
            if self.rotation > 270:
                self.reset()



class EY(Sprite):

    def on_create(self):
        self.image = "EY.png"
        self.add_tag("EY")
    def on_update(self, dt):
        pass


pf = [
    w.create_sprite(PF, x=220, y=140),
    w.create_sprite(PF, x=520, y=330),  
    w.create_sprite(PF, x=800, y=60 )
]

py = w.create_sprite(PY)

ey = w.create_sprite(EY, x=1140, y=w.height/2)



w.run()
