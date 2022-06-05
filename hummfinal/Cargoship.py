from imp import reload
from pycat.core import Window, Sprite, Color, Label, Scheduler, KeyCode
from pycat.experimental.movement import FourWayMovementController as Controller
from typing import List
from enum import Enum, auto
from os import path 


w = Window(width=512,height=1024, background_image="Level_0.png", enforce_window_limits=False, is_sharp_pixel_scaling=True)

class States(Enum):
    start = auto()
    game = auto()
    win = auto()
    lose = auto()

Gstate = States.start

class ScrollableLevel:
    def __init__(self, backgrounds: List[str]):
        self.backgrounds = [w.create_sprite(image=b) for b in backgrounds]
        for i, s in enumerate(self.backgrounds):
            s.x = w.center.x
            s.y = w.center.y + i*w.height

    def on_update(self):
        for background in self.backgrounds:
            if background.y <= -w.height / 2:
                background.y += len(self.backgrounds)*w.height
            background.y -= 3


level = ScrollableLevel(["Level_0.png","Level_0.png"])

class Playbo(Sprite):

    def on_create(self):
        self.image = "start.png"
        self.scale = 2
        self.layer  = 10
        self.position = w.center
        self.y = self.y - 48

    def on_update(self, dt):
        if Gstate == States.start:
            self.is_visible = True
        if Gstate != States.start:
            self.is_visible = False
    
    def on_left_click(self):
        global Gstate
        if Gstate is States.start:
            Gstate = States.game
        if Gstate == States.game:
            Scheduler.update(level.on_update)

class Player(Sprite): 

    def on_create(self):
        self.movement_controller = Controller(w, speed_factor=25)
        self.image = "ship_0000.png"
        self.layer = 9
        self.scale = 3.2
        self.position = w.center
        self.y = self.y - 200
        self.is_visible = False
        self.btime = 0
        self.reload = 1.36

    def on_update(self, dt):
        if Gstate == States.game:
            self.btime += dt
            self.is_visible = True
            self.position += self.movement_controller.get_movement_delta(dt)
        if self.btime > self.reload:
            w.create_sprite(Bullet)
            pbullet = w.create_sprite(Bullet)
            pbullet.position = self.position
            self.btime = 0

class Helper(Sprite): 

    def on_create(self):
        self.movement_controller = Controller(w, speed_factor=25)
        self.image = "ship_0002.png"
        self.layer = 9
        self.scale = 1.6
        self.y = player.y
        self.is_visible = False

    def on_update(self, dt):
        if Gstate == States.game:
            self.is_visible = True
            self.position += self.movement_controller.get_movement_delta(dt)
        if player.btime > player.reload:
            hbullet = w.create_sprite(Bullet)
            hbullet.position = self.position

class Bullet(Sprite):

    def on_create(self):
        self.image = "tile_0000.png"
        self.layer = 9
        self.scale = 3.2
        self.speed = 10

    def on_update(self, dt):
        if Gstate == States.game:
            self.y += self.speed
        if self.y > w.height:
            self.delete()    

class Boss(Sprite): 

    def on_create(self):
        self.movement_controller = Controller(w, speed_factor=25)
        self.image = "ship_0003.png"
        self.layer = 10
        self.scale = 6.8
        self.rotation = 180
        self.position = w.center
        self.y = self.y + 324
        self.is_visible = False
        self.stime = 0
    
    def on_update(self, dt):
        self.stime += dt 
        if Gstate == States.game:
            self.is_visible = True
        
        


class Return(Sprite):

    def on_create(self):
        self.image = "return.png"
        self.scale = 0.49
        self.layer = 10
        self.x = w.width - 64
        self.y = 64
        self.la = w.create_label()
        self.la.x = w.width/2
        self.la.x = self.la.x - self.la.content_width/2
        self.la.y = w.height - 64
        self.la.font_size = 64 
        self.la.is_visible = False
        

    def on_update(self, dt):
        if Gstate is States.win:
            self.is_visible = True
            self.la.text = "Win"
            self.la.x = w.width/2
            self.la.x = self.la.x - self.la.content_width/2
            self.la.y = w.height - 64
            self.la.is_visible = True
        if Gstate is States.lose:
            self.is_visible = True
            self.la.text = "Lose"
            self.la.x = w.width/2
            self.la.x = self.la.x - self.la.content_width/2
            self.la.y = w.height - 64
            self.la.is_visible = True
        if Gstate is States.start:
            self.is_visible = False
            self.la.is_visible = False
    
    def on_left_click(self):
        global Gstate
        if Gstate == States.win:
            Gstate = States.start
        if Gstate == States.lose:
            Gstate = States.start
           
class Scoreboard(Label):

    def on_create(self):
        self.color = Color.CYAN
        self.text = "wiwiwiwiwiw"
        self.x = rbotton.la.x
        self.x = self.x - self.content_width*1.25
        self.y = rbotton.la.y - 64
        self.font_size = 48
        self.is_visible = False
    
    def on_update(self, dt):
        if Gstate is States.win:
            self.is_visible = True
        if Gstate is States.lose:
            self.is_visible = True
        if Gstate is States.start:
            self.is_visible = False
    
boss = w.create_sprite(Boss)
player = w.create_sprite(Player)
helper01 = w.create_sprite(Helper)
helper01.x = player.x - 128
helper02 = w.create_sprite(Helper)
helper02.x = player.x + 128
pbotton = w.create_sprite(Playbo)
rbotton = w.create_sprite(Return)
scoreboard = w.create_label(Scoreboard)
w.run()