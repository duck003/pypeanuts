from http.client import OK
from turtle import position
from pycat.core import Window, Sprite, Color, KeyCode
from enum import Enum, auto
from math import sqrt

w = Window()
w.set_clear_color(126, 200, 80)

class Player(Sprite):

    def on_create(self):
        self.scale = 0.32
        self.image = "slimee.png"
        self.position = w.center
        self.speed = 6

    def on_update(self, dt):
        
        if w.is_key_pressed(KeyCode.UP):
            self.y += self.speed
        if w.is_key_pressed(KeyCode.DOWN):
            self.y -= self.speed
        if w.is_key_pressed(KeyCode.RIGHT):
            self.x += self.speed
        if w.is_key_pressed(KeyCode.LEFT):
            self.x -= self.speed

class Enemy(Sprite):
    
    class State(Enum):
        WANDER = auto()
        CHASE = auto()
        FIGHT = auto()

    def on_create(self):
        self.state = Enemy.State.WANDER
        self.scale = 64
        self.color = Color.RED
        self.goto_random_position()
        self.target = w.create_sprite()
        self.target.scale = 23
        self.target.color = Color.BLUE
        self.target.goto_random_position()
        self.aim = w.create_line(width=6)
        self.a = w.create_arc(radius=80)
        self.b = w.create_arc(radius=200)
        self.labell = w.create_label()
        self.labell.x = self.x-32
        self.labell.y = self.y-32
    
    def on_update(self, dt):
        disa = sqrt((self.x - player.x)**2 + (self.y - player.y)**2)
        if disa < self.b._radius:
            self.state = Enemy.State.CHASE
            self.labell.text = "Chase"
            if disa < self.a._radius:
                self.state = Enemy.State.FIGHT
                self.labell.text = "Fight"
        else:
            self.state = Enemy.State.WANDER
            self.labell.text = "Wander"

        if self.state == Enemy.State.CHASE:
            self.line(self.position, player.position)
            self.point_toward_sprite(player)
            self.move_forward(4)
        elif self.state == Enemy.State.FIGHT:
            self.line(self.position, player.position)
            self.point_toward_sprite(player)
            self.move_forward(4)
        else:
            self.point_toward_sprite(self.target)
            self.move_forward(4)
            self.line(self.position, self.target.position)
            dis = sqrt((self.x - self.target.x)**2 + (self.y - self.target.y)**2)
            if dis < 4:
                self.target.goto_random_position()
            

    def line(self,a:position, b:position):
        dp = a - b
        dp.normalize()
        self.aim.set_start_end(a,b)
        self.a.position = self.position.as_tuple()
        self.b.position = self.position.as_tuple()
        self.labell.x = self.x-32
        self.labell.y = self.y-32

    def roam(self):
        pass

def senemy():
    w.create_sprite(Enemy)

e001 = senemy()
e002 = senemy()

player = w.create_sprite(Player)
w.run()