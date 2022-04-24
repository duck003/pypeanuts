from numpy import ndarray
from pycat.core import Window, Sprite, Color
from pycat.base import NumpyImage as ni
from pycat.base import Texture
from pycat.base.event import MouseEvent
from typing import List

w = Window(is_sharp_pixel_scaling=True, draw_sprite_rects=True)

def split_png(file, rows, cols) -> List[List[ndarray]]:
    pictures = ni.get_array_from_file(file)
    n, m, _ = pictures.shape
    di = n//rows
    dy = m//cols

    return [[pictures[i*di:(i+1)*di, j*di: (j+1)*dy, :]
            for j in range(cols)]for i in range(rows)]

def create_sprite(splited, scale, x0, y0, w:Window, Csprite=Sprite):
    rows ,cols = len(splited), len(splited[0])
    grid = []
    for i in range(rows):
        row =  []
        for j in range(cols): 
            p = w.create_sprite(Csprite)
            p.texture = ni.get_texture_from_array(splited[i][j])
            p.scale = scale
            p.x = x0 + j*(2+p.width)
            p.y = y0 + i*(2+p.height)
            r = row.append(p)
        grid.append(r)

def create_level(n, m, scale, x0, y0, w:Window, Csprite=Sprite):
    rows ,cols = n, m
    grid = []
    for i in range(rows):
        row =  []
        for j in range(cols): 
            q = w.create_sprite(Csprite)
            q.scale = scale
            q.x = x0 + j*(2+q.width)
            q.y = y0 + i*(2+q.height)
            r = row.append(q)
        grid.append(r)

currentr:Texture = None


class Clicked(Sprite):
    
    def on_left_click(self):
        global currentr
        currentr = self.texture
        
class Levelr(Sprite):
    
    def on_left_click(self):
        widthr = self.width
        self.texture = currentr
        self.scale_to_width(widthr)
        

wo = split_png("tiles_packed.png", 10, 12)
pic = create_sprite(wo, 2.6, 100, 145, w, Clicked)
lv = create_level(10, 12, 41.6, 690 ,145, w, Levelr)
w.run()