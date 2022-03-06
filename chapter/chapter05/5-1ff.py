from pycat.core import Window , Sprite, Label
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
   'OH! man, where is the nut.',
   'Woooooo, i am colorful. ',
   'GRESSSSSSSSSSSSSS.',
   '(Seems like it is feel comfortable after pooping.)',
   'AH! Feeling like a piece of meat which can breate is comfortable.',
   'OH! MAN! Keep going on, tha..that is comforble. ',
   'Touch me if you want to go to hospital.',
   'HOLD ON! (Turn around.) Who is bothering us. It just got started.',
]

imnum = 0
text0 = Label('', 100, 50)
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
      imnum = random.randint(0,len(ima)-1)
      w.background_image = ima[imnum]
      text0.text = texts[imnum]
            
button = w.create_sprite(NButton)

w.run()
