from pycat.core import Window, Sprite, Color

list0 = [ 
    'grlallar',
    'rargagrw',
    'rbbwrbbw',
    'gbbrgbbr',
    'grgbbwgr',
    'albbbbra',
    'wgbbbbrl',
    'rgbgwblr'
]

color0 = {
    'r' : (0,125,0),
    'g' : Color.GREEN,
    'l' : (0,125,75),
    'b' : Color.BLACK,
    'a' : (75,75,75),
    'w' : Color.WHITE
}

ccolor = {
    Color.BLACK,
    Color.BLUE,
    Color.CYAN,
    Color.GREEN,
    Color.MAGENTA,
    Color.ORANGE,
    Color.YELLOW,
    Color.RED
}

PIXEL_SIZE = 100

w = Window(width= (len(list0[0])+2)*PIXEL_SIZE,
           height= len(list0)*PIXEL_SIZE)

ncolor = Color.WHITE

class PixelR(Sprite):

    def on_create(self):
        self.scale = PIXEL_SIZE
        

x0 = PIXEL_SIZE/2
y0 = w.height - PIXEL_SIZE/2

for i in range (len(list0)):
    for j in range (len(list0[0])):
        p = w.create_sprite(PixelR)
        p.x = x0 + PIXEL_SIZE *j
        p.y = y0 - PIXEL_SIZE * i
        p.color = color0[list0[i][j]]
        

class Ccolor(Sprite):

    def on_create(self):
        self.scale = PIXEL_SIZE


for i in range (len(ccolor)):
    c:Ccolor = w.create_sprite(Ccolor)
    c.x = w.width - c.width/2
    c.y = w.height -c.width/2 - i*c.height
    c.color = ccolor

w.run()