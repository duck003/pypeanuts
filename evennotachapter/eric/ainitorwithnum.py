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
        for i in range(min(len(self.names),10)):
            if w.is_key_down(ord(str(i))):
                self.animator.play(self.names[i])


cat = w.create_sprite(Cat)
w.run() 