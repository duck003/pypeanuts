from pycat.sound import Sound
from pycat.window import Window
from pycat.sprite import Sprite, RotationMode
from pycat.keyboard import KeyCode
from pycat.scheduler import Scheduler
from pycat.collision import is_aabb_collision
from pycat.label import Label
from pycat.core import Player, AudioLoop 
import random


w = Window(background_image="forest_04.png", draw_sprite_rects=True)

sound01 = Player('hit.wav')
masound = Player('point.wav')
nomasound = Player('laugh.wav')

audio_loop = AudioLoop('LoopLivi.wav', volume=0.2)
audio_loop.play()

class Card (Sprite):

    def on_create(self):
        self.is_visible = False
        self.is_rotated = False

    def on_left_click(self):
        sound01.play()
        if self in cL_sprite:
            pass
        else:
            if len(cL_sprite) < 2 :
                self.is_visible = True
                cL_sprite.append(self)

    def on_update(self, dt):
        if self.is_rotated == True:
            self.rotation += 2
            self.scale -= 0.043
            if self.scale < 0:
                self.delete()

class Button(Sprite):

    def on_create(self):
        self.image = "button.png"
        self.scale = float(0.44)
        self.x = 1100
        self.y = 300
        
    def on_left_click(self):
        if len(cL_sprite) == 2:
            sprite1:Card = cL_sprite[0]
            sprite2:Card = cL_sprite[1]
            if sprite1.image == sprite2.image: 
                masound.play()
                button.score += 1
                score_label.text = 'BEST MATCH: '+str(button.score)
                sprite1.is_rotated =  True
                sprite2.is_rotated =  True
            else:
                nomasound.play()
                sprite1.is_visible = False              
                sprite2.is_visible = False
                button.health += 1
                score_label01.text = "WORST MATCH: " +str(button.health)
            cL_sprite.clear()
    def on_update(self, dt):
        self.rotation += 1
        
button = w.create_sprite(Button)
button.score = 0
button.health = 0

score_label = Label("BEST MATCH: 0",x=1000,y=400)
w.add_label(score_label)
score_label01 = Label("WORST MATCH: 0",x=1000,y=160)
w.add_label(score_label01)

# score_label0 = Label("YOU WIN!")
# w.add_label(score_label0)
# score_label00 = Label("YOU LOSE!")
# w.add_label(score_label00)

cL_sprite = 4 * [ "avatar_01.png", "avatar_02.png", "avatar_03.png", "avatar_04.png"]              
random.shuffle(cL_sprite)

for x in range (200,801,200):
    for y in range (100,461,120):
        p = w.create_sprite(Card, x = x,y = y, image = cL_sprite.pop(), scale = float(1.6))


w.run()