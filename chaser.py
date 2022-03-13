from sre_parse import State
from pycat.core import Window, Sprite, Color, KeyCode, Point, Scheduler
from enum import Enum, auto
from math import sqrt


w = Window()
w.set_clear_color(126, 200, 80)

class Player(Sprite):

    def on_create(self):
        self.scale = 0.16
        self.image = "slimee.png"
        self.position = w.center
        self.speed = 9
        self.health = 99
        self.add_tag("player")

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
    miss = 0
    class State(Enum):
        WANDER = auto()
        CHASE = auto()
        FIGHT = auto()
        INSANE = auto()

    def on_create(self):
        self.state = Enemy.State.WANDER
        self.scale = 32
        self.color = Color.RED
        self.goto_random_position()
        self.target = w.create_sprite()
        self.target.scale = 23
        self.target.color = Color.BLUE
        self.target.goto_random_position()
        self.aim = w.create_line(width=6)
        self.a = w.create_arc(radius=120)
        self.b = w.create_arc(radius=200)
        self.labell = w.create_label()
        self.labell.x = self.x-32
        self.labell.y = self.y-32
        self.shoot = 0
        self.state = Enemy.State.WANDER
        self.labell.text = "Wander"
        self.reload = 0
        self.timei = 0

    def distanceb(self):
        return sqrt((self.x - player.x)**2 + (self.y - player.y)**2)
    
    def on_update(self, dt):
        
        if Enemy.miss > 5:
           self.state = Enemy.State.INSANE
           self.timei = 0
           Enemy.miss = 0
        if self.state == Enemy.State.INSANE:
            self.insane(dt)
            self.labell.text = "INSANE"
        
        else:
            if self.state == Enemy.State.CHASE:
                self.chase()
                if self.distanceb() > self.b._radius:
                    self.state = Enemy.State.WANDER
                    self.labell.text = "Wander"
                if self.distanceb() < self.a._radius:
                    self.state = Enemy.State.FIGHT
                    self.labell.text = "Fight"
            
            elif self.state == Enemy.State.FIGHT:
                self.fight(dt)
                if self.distanceb() > self.a._radius:
                    self.state = Enemy.State.CHASE
                    self.labell.text = "Chase"
            
            else:
                self.wander()
                if self.distanceb() < self.b._radius:
                    self.state = Enemy.State.CHASE
                    self.labell.text = "Chase"

        
    def wander(self):
        self.point_toward_sprite(self.target)
        self.move_forward(4)
        self.line(self.position, self.target.position)
        dis = sqrt((self.x - self.target.x)**2 + (self.y - self.target.y)**2)
        if dis < 4:
            self.target.goto_random_position()
    
    def chase(self):
        self.line(self.position, player.position)
        self.point_toward_sprite(player)
        self.move_forward(4)
        
    def shootr(self,x):
        bullet = w.create_sprite(Bullet)
        bullet.position = self.position
        bullet.point_toward_sprite(player)
        bullet.move_forward(x)
        if bullet.is_touching_window_edge():  
            if bullet.state != Enemy.State.INSANE:    
                Enemy.miss += 1
            bullet.delete()
            

    def fight(self,dt):
        self.reload += dt
        self.line(self.position, player.position)
        self.point_toward_sprite(player)
        self.move_forward(4)
        if self.reload > 0.86:
            self.shootr(6)
            self.reload = 0        
    
    def insane(self,dt):
        self.timei += dt
        self.reload += dt
        self.line(self.position, player.position)
        self.point_toward_sprite(player)
        self.move_forward(8)
        self.a._radius = 256
        self.b._radius = 324
        if self.reload > 0.24:
            self.shootr(10)
            self.reload = 0 
        
        if self.timei > 5:
            self.state = Enemy.State.WANDER
            self.labell.text = "Wander"
            self.a._radius = 120
            self.b._radius = 200
            
            

    def line(self,a:Point, b:Point):
        dp: Point = a - b
        dp.normalize()
        self.aim.set_start_end(a,b)
        self.a.position = self.position.as_tuple()
        self.b.position = self.position.as_tuple()
        self.labell.x = self.x-32
        self.labell.y = self.y-32


class Bullet(Sprite):
    
    def on_create(self):
        self.state = Enemy.State.FIGHT
        self.scale = 12
        self.color = Color.YELLOW
    
    def on_update(self, dt):
        self.move_forward(6)
        if self.is_touching_any_sprite_with_tag("player"):
            self.delete()
        
def senemy():
    w.create_sprite(Enemy)

e001:Enemy = senemy()
e002:Enemy = senemy()


player = w.create_sprite(Player)
w.run()