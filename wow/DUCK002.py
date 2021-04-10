from pycat.base import color
from pycat.core import Color, KeyCode, Scheduler, Sprite, Window, Label, RotationMode
import random, time

from pyglet.image import TextureRegion

w = Window(background_image="wowo.png")

class Gm(Sprite):
    start0 = 1
    game0 = 0
    win0 = 2
    lose0 =3
    def on_create(self):
        self.state = Gm.start0

    def on_update(self, dt):
        pass

gm01: Gm = w.create_sprite(Gm) 

class Start(Sprite):

    def on_create(self):
        self.image = "start.png"
        self.is_visible = True
        self.x = 600
        self.y = 300
    
    def on_update(self, dt):
        if gm01.state == Gm.start0:
            self.is_visible = True

    def on_left_click(self):
        self.is_visible = False
        gm01.state = Gm.game0
         
class Return0(Sprite):

    def on_create(self):
        self.image = "return.png"
        self.is_visible = False
        self.scale = 0.5
        self.x = 1100
        self.y = 125
    
    def on_update(self, dt):
        if gm01.state == Gm.win0:
            self.is_visible = True
        elif gm01.state == Gm.lose0:
            self.is_visible = True
        elif gm01.state == Gm.start0:
            self.is_visible = False
    
    def on_left_click(self):
        self.is_visible = False
        player01.health = 100
        score_label.text = "HERO'S HEALTH : " +str(player01.health)
        enemy01.health = 100
        score_label01.text = "ENEMY'S HEALTH : " +str(enemy01.health)
        gm01.state = Gm.start0

class Win(Sprite):

    def on_create(self):
        self.image = "win.png"
        self.is_visible = False
        self.scale = 2.4
        self.x = 640
        self.y = 300
    def on_update(self, dt):
        if enemy01.health == 0:
            gm01.state = Gm.win0
        if gm01.state == Gm.win0:
            self.is_visible = True
        else:
            self.is_visible = False

class Lose(Sprite):

    def on_create(self):
        self.image = "lose.png"
        self.is_visible = True
        self.scale = 2.4
        self.x = 640
        self.y = 300
    def on_update(self, dt):
        if player01.health == 0:
            gm01.state = Gm.lose0
        if gm01.state == Gm.lose0:
            self.is_visible = True
        else:
            self.is_visible = False

class Player (Sprite):

    def on_create(self):
        self.add_tag("player")
        self.image = ("playc.png")
        self.scale = 0.24
        self.x = 100
        self.y = 300
        self.health = 100
        self.speed = 5
        self.time =  0
        self.bomb = 0 
        
    def on_update(self, dt):
        if gm01.state == Gm.game0:
            self.is_visible = True
        else:
            self.is_visible =False    
        self.time += dt
        if w.get_key(KeyCode.UP):
            self.image = ("playc.png")
            self.scale = 0.24
            self.y += self.speed
        elif w.get_key(KeyCode.DOWN):
            self.image = ("playc00.png")
            self.scale = 0.24
            self.y -= self.speed    
        elif w.get_key(KeyCode.Z):
            self.image = ("playc0.png")
            if self.time > 0.8:
                w.create_sprite(Bullet) 
                self.time = 0    
        elif w.get_key(KeyCode.X):
            self.image = ("playc0.png")
            if self.bomb < 1:
                w.create_sprite(Bomb) 
                self.bomb += 1
        
class Bullet(Sprite):

    def on_create(self):
        self.add_tag('pb')
        self.scale = 0.2
        self.image = ('pb.png')
        self.x = player01.x + 80
        self.y = player01.y
        self.speed = 10
    def on_update(self, dt):
        if gm01.state == Gm.game0:
            self.is_visible = True
        else:
            self.is_visible =False
        self.x += self.speed
        if self.touching_any_sprite_with_tag("enemy"):
            self.delete ()
            enemy01.health -= 1
            score_label01.text = "ENEMY'S HEALTH : " +str(enemy01.health)
        if self.touching_any_sprite_with_tag("eb"):
            self.delete ()
        elif self.x >= 1180:    
            self.delete ()
            enemy01.health -= 1
            score_label01.text = "ENEMY'S HEALTH : " +str(enemy01.health)
        elif self.touching_any_sprite_with_tag("eb"):
            self.delete()
wow = 3

class Bomb(Sprite):
    global wow
    def on_create(self):
        self.image = ("bomb.png")
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.add_tag("bb")
        self.scale = 0.24
        self.x = player01.x + 60
        self.y = player01.y
        self.speed = 20
        self.etime = 0
    def on_update(self, dt):
        if gm01.state == Gm.game0:
            self.is_visible = True
        else:
            self.is_visible =False
        global wow
        if wow == 0 :             
            self.delete()
            player01.bomb -= 1
            wow = 3
        if w.get_key(KeyCode.RIGHT):
            self.rotation = 0
            self.x += self.speed
        if w.get_key(KeyCode.LEFT):
            self.rotation = 180
            self.x -= self.speed
        if w.get_key(KeyCode.C):
            self.image = ("bombe.png")
            for i in range (0,3,1):
                self.etime += dt
            if self.etime > 1 :    
                if self.touching_any_sprite_with_tag('enemy'):             
                    enemy01.health -= 5
                    self.delete()
                    score_label01.text = "ENEMY'S HEALTH : " +str(enemy01.health)
                    player01.bomb -= 1 
                else:
                    self.delete()    
                    player01.bomb -= 1
                self.etime = 0    

class Enemy(Sprite):

    def on_create(self):
        self.add_tag("enemy")
        self.scale = 0.4
        self.health = 100
        self.image = ("enemy.png")
        self.x = 1180
        self.y = 300
        self.rotation_mode = RotationMode.NO_ROTATION
        self.rotation = 90
        self.speed = 5 
    def on_update(self, dt):           
        if gm01.state == Gm.game0:
            self.is_visible = True
        else:
            self.is_visible =False
        self.move_forward(self.speed)
        # time.sleep(1)
        if self.touching_window_edge():
            self.rotation += 180

class Ebullet01(Sprite):
    def on_create(self):
        self.add_tag('eb')
        self.scale = 0.16
        self.image = 'eb.png'
        self.x = enemy01.x - 80
        self.y = enemy01.y
        self.speed = 10
        
    def on_update(self,dt):    
        if gm01.state == Gm.game0:
            self.is_visible = True
        else:
            self.is_visible =False
        global wow
        self.x -= self.speed
        if self.touching_any_sprite_with_tag("player"):
            self.delete ()
            player01.health -= 1
            score_label.text = "HERO'S HEALTH : " +str(player01.health)
        elif self.x <= 100:    
            self.delete ()
            player01.health -= 1
            score_label.text = "HERO'S HEALTH : " +str(player01.health)
        elif self.touching_any_sprite_with_tag("pb"):
            self.delete()
        elif self.touching_any_sprite_with_tag("bb"):
            wow -= 1
            self.delete()
        
score_label = Label("HERO'S HEALTH : 100",x=100,y=600, )
w.add_label(score_label)
score_label01 = Label("ENEMY'S HEALTH : 100",x=900,y=600,)
w.add_label(score_label01)

def spawn_enemy():
    if gm01.state == Gm.game0:
       w.create_sprite(Ebullet01)
    else:
       pass      
Scheduler.update(spawn_enemy, delay=0.86)


start01 = w.create_sprite(Start)
win01 = w.create_sprite(Win)
lose01 = w.create_sprite(Lose)
player01:Player = w.create_sprite(Player)
enemy01:Enemy = w.create_sprite(Enemy)
return01 = w.create_sprite(Return0)

w.run()