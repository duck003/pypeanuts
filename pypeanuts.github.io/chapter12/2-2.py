from pycat.core import Window, Sprite, Color

list0 = [ 
    'abbbbbbc',
    'eddddddf',
    'eddddddf',
    'eddddddf',
    'eddddddf',
    'eddddddf',
    'eddddddf',
    'giiiiiih'
]



color0 = {
    'a' : "tile_020.png",
    'b' : "tile_021.png",
    'c' : "tile_022.png",
    'd' : "tile_029.png",
    'e' : "tile_030.png",
    'f' : "tile_032.png",
    'g' : "tile_033.png",
    'h' : "tile_034.png",
    'i' : "tile_021.png" 
}
IMG_SIZE = 16
PIXEL_SIZE = 100

w = Window(width= len(list0[0])*PIXEL_SIZE,
           height= len(list0)*PIXEL_SIZE)

class PixelR(Sprite):

    def on_create(self):
        self.scale =  PIXEL_SIZE/IMG_SIZE


x0 = PIXEL_SIZE/2
y0 = w.height - PIXEL_SIZE/2

for i in range (len(list0)):
    for j in range (len(list0[0])):
        p = w.create_sprite(PixelR)
        p.x = x0 + PIXEL_SIZE *j
        p.y = y0 - PIXEL_SIZE * i
        p.image = color0[list0[i][j]]
        
        

w.run()