from enum import Enum
from pycat.base.event.mouse_event import MouseEvent
from pycat.core import Window, Sprite, Color, Scheduler
from random import choice, randint, random

w = Window(background_image = "beach0.png", enforce_window_limits=False)

element = ["cyclone", "Heat", "light", "water"]
animals = ["Hopper", "Shark", "bird", "tiger"]
weapons = ["Blade","Shotgun","Bow","Sword"]

ccword = element + animals + weapons

class State(Enum):
    ELEMENT = 0
    ANIMSLS = 1
    WEAPONS = 2

state = [State.ELEMENT,State.ANIMSLS,State.WEAPONS]
nstate = State.ELEMENT

def cstate():
    global nstate
    n = choice(state)
    nstate = n
    lstate.text = (str(nstate))

Scheduler.update(cstate, delay = 4)



class Tword(Sprite):
    
    score = 0

    def on_create(self):
        self.lw = w.create_label()
        self.lw.color = Color.random_rgb()
        self.lw.font_size = 40
        self.lw.font = "Comic Sans MS"
        self.color = Color.random_rgb()
        self.score = 0

    def sposition(self, text, x, y):
        self.lw.text = text
        self.width = self.lw.content_width
        self.height = self.lw.content_height
        self.lw.x = x
        self.lw.y = y
        self.x = x + self.width/2
        self.y = y - self.height/2
        if self.x + self.width/2 > w.width:
            self.x -= self.width/2
            self.lw.x -= self.width/2
        if self.x - self.width/2 < 0:
            self.x += self.width/2
            self.lw.x += self.width/2
        
    
    def on_update(self, dt):
        self.y -= 6
        self.lw.y -= 6
        if self.y < 0 - self.height/2:
            self.delete()
            self.lw.delete()

    def on_left_click(self):
        if nstate == State.ELEMENT and self.lw.text in element:
            self.delete()
            self.lw.delete()
            Tword.score += 1
            score.text = ("Catched Word : " + str(Tword.score))
        elif nstate == State.ANIMSLS and self.lw.text in animals:
            self.delete()
            self.lw.delete()
            Tword.score += 1
            score.text = ("Catched Word : " + str(Tword.score))
        elif nstate == State.WEAPONS and self.lw.text in weapons:
            self.delete()
            self.lw.delete()
            Tword.score += 1
            score.text = ("Catched Word : " + str(Tword.score))
        else:
            self.delete()
            self.lw.delete()
            Tword.score -= 1
            score.text = ("Catched Word : " + str(Tword.score))


def wordr():
    word = w.create_sprite(Tword)
    word.sposition(choice(ccword),randint(100,1200),w.height)

Scheduler.update(wordr, delay=0.9)

score = w.create_label()
score.text = ("Catched Word : " + str(0))
score.color = Color.BLACK

lstate = w.create_label()
lstate.text = (str(nstate))
lstate.y = score.y - score.content_height 
lstate.color = Color.BLACK

w.run()