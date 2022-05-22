from pycat.core import Window, Sprite, KeyCode
from pycat.experimental.animation import Animator
from seemsneeded import eachmove

w = Window(is_sharp_pixel_scaling= True)
a = Animator()

class Cat(Sprite):
    def on_create(self):
        self.position = w.center
        self.scale = 22
        self.animator = Animator(eachmove)
        self.animator.play("jump")
        self.image = self.animator.tick(0)
        self.la = w.create_label()
        self.la.text = "Genius"
        self.la.font_size = 60
        self.la.x = self.x - self.x/4
        self.la.y = self.y + 165
        self.la.is_visible = False
    
    def on_update(self, dt):
        self.image = self.animator.tick(dt)
        if w.is_key_pressed(KeyCode.Z):
            self.la.is_visible = True
            self.animator.play("look")
        if w.is_key_pressed(KeyCode.X):
            self.la.is_visible = False
            self.animator.play("paw")
        if w.is_key_pressed(KeyCode.C):
            self.la.is_visible = False
            self.animator.play("run")
        if w.is_key_pressed(KeyCode.V):
            self.la.is_visible = False
            self.animator.play("scared")
        if w.is_key_pressed(KeyCode.B):
            self.la.is_visible = False
            self.animator.play("sit")
        if w.is_key_pressed(KeyCode.N):
            self.la.is_visible = False
            self.animator.play("sleep")
        if w.is_key_pressed(KeyCode.M):
            self.la.is_visible = False
            self.animator.play("sprint")
        if w.is_key_pressed(KeyCode.SPACE):
            self.la.is_visible = False
            self.animator.play("jump")
        if w.is_key_pressed(KeyCode.LSHIFT):
            self.la.is_visible = False
            self.animator.play("lickb")
        if w.is_key_pressed(KeyCode.LCTRL):
            self.la.is_visible = False
            self.animator.play("lick")


cat = w.create_sprite(Cat)
w.run() 