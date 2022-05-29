from pycat.core import Window, Sprite, KeyCode
from pycat.experimental.animation import Animator

w = Window(is_sharp_pixel_scaling= True)
a = Animator()

def get_easier(name, frames, drectory):
    images = [[drectory + name[i]+ str(j+1) +".png"
              for j in range(1,frames[i])]
              for i in range(len(name))]
    return {name[i]:images[i] for i in range(len(name))}

class Cat(Sprite):
    def on_create(self):
        self.position = w.center
        self.scale = 22
        self.names = ["jump","lick","lickb","look","paw","run","scared","sit","sleep","sprint"]
        frames = [7,4,4,4,6,8,8,4,4,8]
        directory = "animation_data/cat/"
        eachmove = get_easier(self.names,frames,directory)
        self.animator = Animator(eachmove)
        self.animator.play("jump")
        self.image = self.animator.tick(0)
        
    def on_update(self, dt):
        self.image = self.animator.tick(dt)
        if w.is_key_pressed(KeyCode.Z):
            
            self.animator.play("look")
        if w.is_key_pressed(KeyCode.X):
            
            self.animator.play("paw")
        if w.is_key_pressed(KeyCode.C):
            
            self.animator.play("run")
        if w.is_key_pressed(KeyCode.V):
            
            self.animator.play("scared")
        if w.is_key_pressed(KeyCode.B):
            
            self.animator.play("sit")
        if w.is_key_pressed(KeyCode.N):
            
            self.animator.play("sleep")
        if w.is_key_pressed(KeyCode.M):
            
            self.animator.play("sprint")
        if w.is_key_pressed(KeyCode.SPACE):
           
            self.animator.play("jump")
        if w.is_key_pressed(KeyCode.LSHIFT):
            
            self.animator.play("lickb")
        if w.is_key_pressed(KeyCode.LCTRL):
            
            self.animator.play("lick")


cat = w.create_sprite(Cat)
w.run() 