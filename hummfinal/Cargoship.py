from pycat.core import Window, Sprite, Color, Label
from enum import Enum, auto


w = Window(width=512,height=1024)

class States(Enum):
    start = auto()
    game = auto()
    win = auto()
    lose = auto()

Gstate = States.start

class Playbo(Sprite):

    def on_create(self):
        self.color = Color.CYAN
        self.scale = 64
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
            Gstate = States.lose

class Return(Sprite):

    def on_create(self):
        self.color = Color.CYAN
        self.scale = 64
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
    


pbotton = w.create_sprite(Playbo)
rbotton = w.create_sprite(Return)
scoreboard = w.create_label(Scoreboard)
w.run()