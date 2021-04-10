from pycat.window import Window
from pycat.sprite import Sprite
from pycat.keyboard import KeyCode



o=Window(background_image="forest_background.jpg")



class Wow(Sprite):
    def on_create (self):
        self.image="owl.png"
        self.x=50
        self.y=600
    def on_update(self, dt):
        
        if o.get_key (KeyCode.W):
            self.rotation=90
            self.move_forward(10)
        if o.get_key (KeyCode.S):
            self.rotation=270
            self.move_forward(10)
        if o.get_key (KeyCode.A):
            self.rotation=0
            self.move_forward(-10)
        if o.get_key (KeyCode.D):
            self.rotation=0
            self.move_forward(10)
        if self.touching_any_sprite():
            print('Oh no!') 
            o.exit()
    

class Wowow(Sprite):
    
    def on_create (self):
        self.image="rooster.png"
        self.x=1160
        self.y=50
    def on_update(self, dt):
        if o.get_key (KeyCode.I):
            self.rotation=90
            self.move_forward(10)
        if o.get_key (KeyCode.K):
            self.rotation=270
            self.move_forward(10)
        if o.get_key (KeyCode.J):
            self.rotation=180
            self.move_forward(10)
        if o.get_key (KeyCode.L):
            self.rotation=0
            self.move_forward(10)
        if self.touching_any_sprite():
            print('Oh Yeah!') 
            o.exit()








oh = o.create_sprite(Wow)

ohma= o.create_sprite(Wowow)



o.run()
