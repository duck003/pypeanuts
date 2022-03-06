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
        self.go_up = True
        self.xy = 0
    def on_update(self, dt):
        
        self.xy += dt
        if self.go_up:
            self.y += 1
            self.hitbox.y += 1
            if self.xy > 1:
                self.go_up = False
                self.xy = 0 
        else:
            self.y -= 1
            self.hitbox.y -= 1
            if self.xy > 1:
                self.go_up = True
                self.xy = 0 
        
    
    def add_hitbox(self):
        self.hitbox = w.create_sprite(position=self.position )
        self.hitbox.height = self.height
        self.hitbox.width = self.width *0.96
        self.hitbox.color = 255,0,0
        self.hitbox.opacity = 0

pf = [
    w.create_sprite(PF, x=220, y=140),
    w.create_sprite(PF, x=520, y=330),  
    w.create_sprite(PF, x=800, y=60 )
]

for f in pf:
    f.add_hitbox()

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
        if self.state == PYstate.WAITING:
            for i in pf:
                if self.is_touching_sprite(i.hitbox):
                    self.y = i.hitbox.height/2 + self.height/2 + i.hitbox.y
                else:
                    self.y -= 1 
        
        if self.state == PYstate.JUMPING:
            pre_y = self.y
            pre_x = self.y

            self.x += self.x_speed
            self.y += self.y_speed

            self.y_speed -= 1
        
            for p in pf:
                if self.is_touching_sprite(p.hitbox):
                    top_y = p.hitbox.height/2 + self.height/2 + p.hitbox.y 
                    left_x = p.hitbox.y - p.hitbox.width/2 - self.width 
                    right_x = p.hitbox.y + p.hitbox.width/2 + self.width 
                    if pre_y > top_y :
                        self.y = top_y
                        self.state = PYstate.WAITING
                    
                    if pre_x < left_x :
                        self.x = left_x
                        self.state = PYstate.WAITING

                    if pre_x > right_x :
                        self.x = right_x
                        self.state = PYstate.WAITING
             
            if self.is_touching_window_edge():
                self.x_speed = 0
                self.y_speed = 0
                
                self.state = PYstate.RESTTING
        

            if self.is_touching_any_sprite_with_tag ("EY"):
                self.x_speed = 0
                self.y_speed = 0
                
                self.state = PYstate.RESTTING

        if self.state == PYstate.RESTTING:
            self.rotation +=5
            self.scale *= 0.98  
            if self.rotation > 270:
                self.reset()


    def on_click_anywhere(self, mouse_event: MouseEvent):
        if self.state == PYstate.WAITING:
            self.xdict = mouse_event.position.x - self.x
            self.ydict = mouse_event.position.y - self.y
        
            self.x_speed = self.xdict * 0.05
            self.y_speed = self.ydict * 0.09
        
            self.state = PYstate.JUMPING


class EY(Sprite):

    def on_create(self):
        self.image = "EY.png"
        self.add_tag("EY")
    def on_update(self, dt):
        pass


py = w.create_sprite(PY)

ey = w.create_sprite(EY, x=1140, y=w.height/2)



w.run()
