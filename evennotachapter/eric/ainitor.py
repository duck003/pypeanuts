from pycat.core import Window, Sprite, KeyCode
from pycat.experimental.animation import Animator
from pycat.experimental.spritesheet import SpriteSheet

w = Window(is_sharp_pixel_scaling= True)
a = Animator()



class Notcat(Sprite):
    def on_create(self):
        self.position = w.center
        self.scale = 4
        self.name = "death"
        sheet = SpriteSheet("animation_data/fire_worm/Death.png",180,180)
        self.textures = [sheet.get_texture(i,0) for i in range(8)]
        self.animator = Animator({self.name :self.textures})
        self.animator.play("death")
        self.texture = self.animator.tick(0)

    def on_update(self, dt):
        self.texture= self.animator.tick(dt)

www = w.create_sprite(Notcat)
w.run() 