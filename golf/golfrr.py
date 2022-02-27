from cv2 import rotate
from pycat.core import Window, Sprite, Point, Color
from pycat.base.event import MouseEvent
from typing import List
from math import sqrt

from pyrsistent import s
from sympy import rotations

w = Window()
w.set_clear_color(126, 200, 80)
hole = w.create_circle(1100, 500, 32, color = Color.BLACK)

S = 0.05
FRICTION = 0.98

def dot(u:Point,v:Point):
    return u.x*v.x + u.y*v.y

def project(u:Point,v:Point):
    return dot(u,v)* v/ dot(v,v)

def reflect(u:Point,v:Point):
    return u - 2*project(u,v)

class Golf(Sprite):

    def on_create(self):
        self.aim = w.create_line(width=6) 
        self.aim.visible = True
        self.layer = 1
        self.scale = 0.05
        self.image = "golfball.png"
        self.position = (200,200)   
        self.speed = 0
        self.aiming = True
        self.l = None

    def on_update(self, dt):
        if self.aiming:
            self.aim.visible = True
            dp = w.mouse_position - self.position
            self.speed = dp*S
            if dp.x == 0 and dp.y == 0:
                self.aim.set_start_end(self.position,self.position)
            else:
                dp.normalize()
                self.aim.set_start_end(self.position,self.position + 100*dp)
        
        else: 
            self.position += self.speed 
            self.speed *= FRICTION
            d = (self.position - Point(hole.x, hole.y)).magnitude()
            if d < hole.radius:
                w.close()
            self.bounce()
            if self.speed.magnitude() < 1:
                self.aiming = True
                    
    def on_click_anywhere(self, mouse_event: MouseEvent):
        if self.aiming:
            dp = w.mouse_position - self.position
            self.speed = dp*S
            self.aim.visible = False
            self.aiming = False
    
    def bounce(self):
        walls: List[Wall] = self.get_touching_sprites_with_tag("wall")
        if walls:
            wa =  walls[0]
            self.speed = reflect(self.speed, wa.n)

class Wall(Sprite):
    
    def on_create(self):
        self.position = w.center
        self.rotation = 180
        self.scale_x = 100
        self.scale_y = 400
        self.color = Color.CYAN
        self.add_tag("wall")

    def normal_line(self):
        p1 = self.position
        self.move_forward(1)
        p2 = self.position
        self.move_forward(-1)
        self.n = p2-p1
        p3 = p1 +100*self.n 
        li = w.create_line(p1.x, p1.y, p3.x, p3.y, width=6)       

def cwall(x, y, r):
    wall = w.create_sprite(Wall, x=x, y=y, rotation=r)
    wall.normal_line()

cwall(75,100,45)
cwall(350,50,90)
cwall(750,50,90)
cwall(1150,50,90)
cwall(350,600,270)
cwall(750,600,270)
cwall(1150,600,270)
cwall(50,300,0)
cwall(75,500,315)
cwall(600,100,45)
cwall(600,100,45)
cwall(600,100,45)
cwall(600,100,45)



golf = w.create_sprite(Golf)
w.run()