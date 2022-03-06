from pycat.window import Window
from pycat.sprite import Sprite, RotationMode
from pycat.keyboard import KeyCode
from pycat.scheduler import Scheduler
from pycat.collision import is_aabb_collision
from pycat.label import Label
import random

w = Window(background_image="forest_04.png", draw_sprite_rects=True)

cL_sprite = []              

class Card (Sprite):

    def on_create(self):
        self.is_visible = False
        

    def on_left_click(self):
        if self in cL_sprite:
            pass
        else:
            if len(cL_sprite) < 2 :
                self.is_visible = True
                cL_sprite.append(self)

score = 0

class Button(Sprite):

    def on_create(self):
        self.image = "button.png"
        self.scale = float(0.66)
        self.x = 1100
        self.y = 300
    def on_left_click(self):
        if len(cL_sprite) == 2:
            sprite1:Sprite = cL_sprite[0]
            sprite2:Sprite = cL_sprite[1]
            if sprite1.image == sprite2.image: 
                sprite1.delete()
                sprite2.delete()
                button.score += 1
                score_label.text = 'BEST MATCH: '+str(button.score)
            else:
                sprite1.is_visible = False              
                sprite2.is_visible = False
            cL_sprite.clear()

button = w.create_sprite(Button)
button.score = 0

score_label = Label("BEST MATCH: 0",x=1000,y=400)
w.add_label(score_label)

p1 = w.create_sprite(Card, x = 200,y = 100, image = "avatar_01.png", scale = float(1.6))
p2 = w.create_sprite(Card, x = 200,y = 220, image = "avatar_02.png", scale = float(1.6))
p3 = w.create_sprite(Card, x = 200,y = 340, image = "avatar_03.png", scale = float(1.6))
p4 = w.create_sprite(Card, x = 200,y = 460, image = "avatar_04.png", scale = float(1.6))
p5 = w.create_sprite(Card, x = 400,y = 100, image = "avatar_01.png", scale = float(1.6))
p6 = w.create_sprite(Card, x = 400,y = 220, image = "avatar_02.png", scale = float(1.6))
p7 = w.create_sprite(Card, x = 400,y = 340, image = "avatar_03.png", scale = float(1.6))
p8 = w.create_sprite(Card, x = 400,y = 460, image = "avatar_04.png", scale = float(1.6))
p08 = w.create_sprite(Card, x = 600,y = 100, image = "avatar_01.png", scale = float(1.6))
p07 = w.create_sprite(Card, x = 600,y = 220, image = "avatar_02.png", scale = float(1.6))
p06 = w.create_sprite(Card, x = 600,y = 340, image = "avatar_03.png", scale = float(1.6))
p05 = w.create_sprite(Card, x = 600,y = 460, image = "avatar_04.png", scale = float(1.6))
p04 = w.create_sprite(Card, x = 800,y = 100, image = "avatar_01.png", scale = float(1.6))
p03 = w.create_sprite(Card, x = 800,y = 220, image = "avatar_02.png", scale = float(1.6))
p02 = w.create_sprite(Card, x = 800,y = 340, image = "avatar_03.png", scale = float(1.6))
p01 = w.create_sprite(Card, x = 800,y = 460, image = "avatar_04.png", scale = float(1.6))

w.run()