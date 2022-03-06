from pycat.core import Window, Sprite, Color

thew = 9
theh = 9     
gap = 2

w = Window(width=thew*60, height=theh*60)

class Blank (Sprite):
    
    def on_create(self):
        self.color = Color.WHITE
        self.scale = 60
    
    def on_click(self):
        self.delete()

blankr = w.create_sprite(Blank)
blankr.position = w.center
        
# for i in range (thew):
#     for j in range(theh):
#         blankr = w.create_sprite(Blank)
#         blankr.x = 60*i - blankr.width/2 + gap 
         

w.run()