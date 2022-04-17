from pycat.base import NumpyImage as ni
from pycat.core import Window ,Sprite, Color, Label
from pycat.base.event import MouseEvent
from typing import List
from random import shuffle

w = Window(width =600, height = 400)


class Button(Sprite):

    def on_create(self):
        self.image = "button.png"
        self.scale = 0.24
        self.position = 500 ,100
    
    def on_click(self, mouse_evwnt:MouseEvent):
        if test_win():
            print("wow")
        else:
            print("nope")


class Where(Label):
        def on_create(self):
            self.font_size = 2


class Drable(Sprite):
    current = None
    

    def on_create(self):
        self.layer = 2
        w.subscribe(on_mouse_drag = self.on_mouse_drag,
                    on_mouse_release = self.on_mouse_release)
        self.labell = w.create_label()
        self.labell.x = self.x - self.width/2
        self.labell.y = self.y - self.height/2
    
    def on_click(self, mouse_event: MouseEvent):
        Drable.current = self

    def on_mouse_drag(self, mouse_event: MouseEvent):
        if Drable.current is self :
            self.position = mouse_event.position

    def on_mouse_release(self, mouse_event: MouseEvent):
        Drable.current = None
        targets = self.get_touching_sprites_with_tag("target")
        if targets:
            self.position = targets[0].position

    def set_ij(self, i, j):
        self.i = i
        self.j = j
             
class Pointf(Sprite):

    def on_create(self):
        self.add_tag("target")
        self.scale = 21
        self.color = Color.WHITE
        self.layer = 1
        self.label2 = w.create_label()
        self.label2.x = self.x - self.width/2
        self.label2.y = self.y - self.height/2
    
    def set_ij(self, i, j):
        self.i = i
        self.j = j
             

pointf = []
        

def get_image_grid(img, rows, cols, x0, y0, scale) -> List[List[Sprite]]:
    oimage = ni.get_array_from_file(img) 
    img_rows, img_cols, _ = oimage.shape
    
    imag_grid = []
    rows_step = img_rows // rows
    cols_step = img_cols // cols

    for i in range(rows):
        pointf_row = []
        imag_row = [] 
        for j in range(cols): 
            mini = i * rows_step
            maxi = (i+1) * rows_step
            minj = j * cols_step
            maxj = (j+1) * cols_step

            sub_img = oimage [mini:maxi, minj:maxj, :]
            p = w.create_sprite(Drable)
            p.set_ij(i , j)
            z = w.create_sprite(Pointf)
            z.set_ij(i , j)
            p.texture = ni.get_texture_from_array(sub_img)
            p.scale = scale
            p.x = x0 + j*(1+p.width)
            p.y = y0 + i*(1+p.height)
            z.x = p.x
            z.y = p.y         
            pointf_row.append(z)
            imag_row.append(p)

        imag_grid.append(imag_row)
        pointf.append(pointf_row)
    
    return imag_grid, pointf

wo, target0 = get_image_grid("hummmm.png", 2, 2, 250, 120, 0.98)

def get_random(stuff: List[List[Sprite]]):
    cposition = []

    for row in stuff:
        for q in row:
            cposition.append(q.position)

    shuffle(cposition)

    for row in stuff:
        for i in row:
            i.position = cposition.pop()


def test_win():
    for a in wo:
        for q in a:
            t:List[target0] =  q.get_touching_sprites_with_tag("target")
            if t:
                target1 = t[0]
                if (target1.i != q.i) or (target1.j != q.j):
                    return False
            
            else:
                return False
    return True

get_random(wo)              

button = w.create_sprite(Button)
w.run()