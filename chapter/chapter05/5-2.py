from pycat.core import Window , Sprite , Label
import random 

w = Window(width=1000)

like = []

dislike = []

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
def testwow ():
   global imnum
   imnum +=1
   if imnum >= len(ima):
      w.close()
      return
   w.background_image = ima[imnum] 
   text0.text = texts[imnum]


text0 = Label('', 400, 50)
w.add_label(text0)
w.background_image = ima[imnum]
text0.text = texts[imnum]

class Yeah(Sprite):
    def on_create(self):
       self.image = "thumbs_up.png"
       self.x = 900
       self.y = 140
       self.scale = 0.25
    
    def on_left_click(self):
        like.append(ima[imnum])
        print("That you like:",like)
        testwow ()

class Nope(Sprite):
    def on_create(self):
       self.image = "thumbs_up.png"
       self.x = 100
       self.y = 140
       self.scale = 0.25 
       self.rotation = 180
    def on_left_click(self):
        dislike.append(ima[imnum])
        print("That you hate:", dislike)
        testwow ()    
            
button01 = w.create_sprite(Yeah)
button001 = w.create_sprite(Nope)
w.run()