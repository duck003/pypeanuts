from pycat.core import Window , Sprite , Label
import random 

w = Window(width=1000)

ima = [
   'squirrel.jpg',
   'bird.jpg',
   'sheep.jpg',
   'cow.jpg',
   'seal.jpg',
   'cat.jpg',
   'hedgehog.jpg',
   'meerkat.jpg',
]

texts = [
   'Red squirrel',
   'Pheasant',
   'Sheep',
   'Cow',
   'Seal',
   'Cat',
   'Hedgehog',
   'Meerkat',
]

imnum = 0
text0 = Label('', 400, 50)
w.add_label(text0)
w.background_image = ima[imnum]
text0.text = texts[imnum]

class NButton(Sprite):
    def on_create(self):
       self.image = "button_next.png"
       self.x = 900
       self.y = 60
       self.scale = 0.5  
    
    def on_left_click(self):
        global imnum
        imnum +=1
        if imnum >= len(ima):
            w.close()
            return
        w.background_image = ima[imnum] 
        text0.text = texts[imnum]
            
button = w.create_sprite(NButton)

w.run()