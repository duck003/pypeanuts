from pycat.window import Window
from pycat.sprite import Sprite
from pycat.keyboard import KeyCode



o = Window(background_image="forest_background.jpg")



class Wow(Sprite):
    def on_create (self):
        self.image="owl.png"
        self.x=1160
        self.y=100
        self.health=50
    def on_update(self, dt):
        
        if o.get_key (KeyCode.UP):
            self.rotation=90
            self.move_forward(10)
        if o.get_key (KeyCode.DOWN):
            self.rotation=270
            self.move_forward(10)
        if o.get_key (KeyCode.LEFT):
            self.rotation=0
            self.move_forward(-10)
        if o.get_key (KeyCode.RIGHT):
            self.rotation=0
            self.move_forward(10)
        if self.touching_any_sprite():
            self.health-=1
            print(self.health)
        if self.health < 1 :   
            print('Oh no!')
            o.exit()
            
class Wowo(Sprite):
    
    def on_create (self):
        self.image="owl.gif"
        self.x=600
        self.y=300
        self.scale=(float(0.5))

ohma=o.create_sprite(Wowo)

class Wowow(Sprite):
    
    def on_create (self):
        self.image="rooster.png"
        self.x=200
        self.y=50
        self.health=100
    def on_update(self, dt):
        self.point_toward_sprite(oh)
        self.move_forward(float(2.5))    
        
        if self.touching_any_sprite():
            self.health-=1
            print(self.health)
        
        if self.health < 1 :   
            print('Oh Yeah!')
            o.exit()

ohm=o.create_sprite(Wowow)



oh=o.create_sprite(Wow)
o.run()

