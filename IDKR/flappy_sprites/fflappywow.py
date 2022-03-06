from pycat.core import Window, Sprite, KeyCode, Scheduler
import random

from pyglet.image import TextureRegion

w = Window(background_image="background.png",
           width=900,
           height=504,
           enforce_window_limits=False)






class Bird(Sprite):

    def on_create(self):
        self.image = "bird.gif"
        self.y = w.center.y
        self.x = 120
        self.scale = 0.25
        self.is_dying = False
    def on_update(self, dt):
        self.y -= 1
        if w.is_key_down(KeyCode.SPACE):
            self.y += 20
        
        if self.is_touching_any_sprite:
            self.is_dying = True
        
        if self.is_dying == True:
            for i in range (1,1000000,1):
                self.rotation += i
        
        if self.is_touching_window_edge():
            w.close()

class Pipe(Sprite):

    def on_create(self):
        self.add_tag ("piper")
        self.image = "pipe.png"
        self.scale =0.65
        self.x = w.width + self.width/2 
            
    
    def on_update(self, dt):
        self.x -= 4
        if self.x < -self.width/2 :
            self.delete()

def create_pipe01(dt):
    dpipe = w.create_sprite(Pipe)
    upipe = w.create_sprite(Pipe)
    xy = random.randint(-int(dpipe.width/2),int(dpipe.width/2)  )
    upipe.rotation = 180
    upipe.y = w.height
    dpipe.y += xy
    upipe.y += xy
    gapxy = random.randint(-50,50)
    dpipe.y -= gapxy
    upipe.y += gapxy


Scheduler.update(create_pipe01, delay=1.6)




bird = w.create_sprite(Bird)


w.run()