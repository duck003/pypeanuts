from pycat.core import Window, Sprite, Color, KeyCode, Point, Label
from enum import Enum, auto
from math import sqrt


w = Window()
w.set_clear_color(126, 200, 80)

class Health(Label):
    
    def on_create(self):
        self.health = 99
        self.font_size = 40
        self.color = Color.RED
        self.x = 36
        self.y = 628
    
    def on_update(self, dt: float):
        self.text = ("Health:" + str(self.health))

playerhp = w.create_label(Health) 

class Player(Sprite):

    def on_create(self):
        self.scale = 0.24
        self.image = "slimee.png"
        self.position = w.center
        self.speed = 9
        self.add_tag("player")

    def on_update(self, dt):
        
        if w.is_key_pressed(KeyCode.W):
            self.y += self.speed
        if w.is_key_pressed(KeyCode.S):
            self.y -= self.speed
        if w.is_key_pressed(KeyCode.D):
            self.x += self.speed
        if w.is_key_pressed(KeyCode.A):
            self.x -= self.speed

class Enemy(Sprite):
    miss = 0
    class State(Enum):
        WANDER = auto()
        CHASE = auto()
        FIGHT = auto()
        INSANE = auto()
        STUCK = auto()

    def on_create(self):
        self.state = Enemy.State.WANDER
        self.scale = 0.24
        self.rotation_mode.NO_ROTATION
        self.add_tag("enemy")
        self.image = "slimee.jpg"
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
        self.times = 0

    def distanceb(self):
        return sqrt((self.x - player.x)**2 + (self.y - player.y)**2)

   
    def check_insane(self,dt):
        if Enemy.miss > 5:
           self.state = Enemy.State.INSANE
           self.timei = 0
           self.labell.text = "INSANE"
    
    def check_stuck(self,dt):
        if self.is_touching_any_sprite_with_tag("bullet"):
           self.state = Enemy.State.STUCK
           self.times = 0
           self.labell.text = "STUCK"
    

    def on_update(self, dt):
        
        if self.state is Enemy.State.CHASE:
            self.chase()
            self.check_insane(dt) 
            self.check_stuck(dt) 
            if self.distanceb() > self.b._radius:
                self.state = Enemy.State.WANDER
                self.labell.text = "Wander"
            if self.distanceb() < self.a._radius:
                self.state = Enemy.State.FIGHT
                self.labell.text = "Fight"
        
        elif self.state is Enemy.State.FIGHT:
            self.fight(dt)
            self.check_insane(dt)
            self.check_stuck(dt)  
            if self.distanceb() > self.a._radius:
                self.state = Enemy.State.CHASE
                self.labell.text = "Chase"
        
        elif self.state is Enemy.State.INSANE:
            self.insane(dt)
            self.timei += dt
            if self.timei > 5:
                self.state = Enemy.State.WANDER
                self.labell.text = "Wander"
                self.a._radius = 120
                self.b._radius = 200
                Enemy.miss = 0
                self.timei = 0    
        
        elif self.state is Enemy.State.STUCK:
            self.stuck()
            self.times += dt
            if self.times > 6:
                self.state = Enemy.State.WANDER
                self.labell.text = "Wander"
                self.a._radius = 120
                self.b._radius = 200
                self.times = 0
   
        elif self.state is Enemy.State.WANDER:
            self.wander()
            self.time = 0
            self.check_insane(dt)
            self.check_stuck(dt)  
            if self.distanceb() < self.b._radius:
                self.state = Enemy.State.CHASE
                self.labell.text = "Chase"

        
        bu = self.get_touching_sprites_with_tag("bullet")
        for b in bu:
            b.delete()

        
    def wander(self):
        self.point_toward_sprite(self.target)
        self.a._radius = 120
        self.b._radius = 200
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

    def fight(self,dt):
        self.reload += dt
        self.line(self.position, player.position)
        self.point_toward_sprite(player)
        self.move_forward(4)
        if self.reload > 0.86:
            self.shootr(6)
            self.reload = 0        
    
    def insane(self,dt):
        self.reload += dt
        self.line(self.position, player.position)
        self.point_toward_sprite(player)
        self.move_forward(8)
        self.a._radius = 256
        self.b._radius = 324
        if self.reload > 0.24:
            self.shootr(10)
            self.reload = 0 
    
    def stuck(self):
        self.a._radius = 0
        self.b._radius = 0
        
            
            
    def line(self,a:Point, b:Point):
        dp: Point = a - b
        dp.normalize()
        self.aim.set_start_end(a,b)
        self.aim.color = Color.YELLOW
        self.a.position = self.position.as_tuple()
        self.b.position = self.position.as_tuple()
        self.labell.x = self.x-32
        self.labell.y = self.y-32

class Gun (Sprite):
    
    class State(Enum):
        LEFT = auto()
        PICKED = auto()

    def on_create(self):
        self.goto_random_position()
        self.image = "lazergun.png"
        self.state = Gun.State.LEFT
        self.layer = 2
        self.scale = 0.1
        self.dtt = 0

    def on_update(self,dt):
        if self.is_touching_any_sprite_with_tag("player"):
            self.state = Gun.State.PICKED
        if self.state == Gun.State.PICKED:
            self.picked()
        self.dtt += dt
    
    def on_left_click_anywhere(self):
        # if self.dtt > 10:
        self.shootmr()
        self.dtt = 0

    def picked(self):
        self.x = player.x
        self.y = player.y-25 
        self.point_toward_mouse_cursor()

    def shootmr(self,):
        bulletm = w.create_sprite(Bulletm)
        bulletm.position = self.position
        bulletm.move_forward(6)
          

gun = w.create_sprite(Gun)

class Bulletm(Sprite):
    
    def on_create(self):
        self.state = Enemy.State.FIGHT
        self.add_tag("bullet")
        self.scale = 12
        self.color = Color.CYAN
        self.rotation = gun.rotation
    
    def on_update(self, dt):
        self.move_forward(6)
        # if self.is_touching_any_sprite_with_tag("enemy"):
        #     self.delete()
        if self.is_touching_window_edge():  
            self.delete()

class Bullet(Sprite):
    
    def on_create(self):
        self.state = Enemy.State.FIGHT
        self.scale = 12
        self.color = Color.YELLOW
    
    def on_update(self, dt):
        self.move_forward(6)
        if self.is_touching_any_sprite_with_tag("player"):
            self.delete()
            playerhp.health -= 1
        if self.is_touching_window_edge():  
            if self.state != Enemy.State.INSANE:
                Enemy.miss += 1
                self.delete()
            if Enemy.miss > 5:
                self.state = Enemy.State.INSANE
            if Enemy.miss < 5:
                self.state = Enemy.State.FIGHT
            
            

def senemy():
    w.create_sprite(Enemy)

e001:Enemy = senemy()
e002:Enemy = senemy()

player = w.create_sprite(Player)
w.run()