from pycat.core import Window, Sprite


w = Window(is_sharp_pixel_scaling=True)

class Cat(Sprite):

    def on_create(self):
        self.position = w.center
        self.scale = 22
        self.nowphoto = 1
        self.finalphoto = 7
        self.happened = "animation_data/cat/jump"+str(self.nowphoto)+".png"
        self.image = self.happened
        self.time = 0

    def on_update(self, dt):
        self.time += dt

        self.happened = "animation_data/cat/jump"+str(self.nowphoto)+".png"
        self.image = self.happened
        
        if self.time > 0.2:
            self.nowphoto += 1
            if self.nowphoto > self.finalphoto:
                self.nowphoto = 1
            self.time =0
      
cat = w.create_sprite(Cat)
w.run()