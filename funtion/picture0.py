from pycat.base import NumpyImage as ni
from pycat.core import Window ,Sprite
from pycat.base.event import MouseEvent
from typing import List
from random import shuffle

w = Window(width =600, height = 400)

class Drable(Sprite):
    current = None
    def on_create(self):
        w.subscribe(on_mouse_drag = self.on_mouse_drag,
                    on_mouse_release = self.on_mouse_release)
    
    def on_click(self, mouse_event: MouseEvent):
        Drable.current = self

    def on_mouse_drag(self, mouse_event: MouseEvent):
        if Drable.current is self :
            self.position = mouse_event.position

    def on_mouse_release(self, mouse_event: MouseEvent):
        # if Drable.current is self :
            Drable.current = None
        

def get_image_grid(img, rows, cols) -> List[List[Sprite]]:
    oimage = ni.get_array_from_file(img) 
    img_rows, img_cols, _ = oimage.shape
    
    imag_grid = []
    rows_step = img_rows // rows
    cols_step = img_cols // cols

    for i in range(rows):
        imag_row = [] 
        for j in range(cols): 
            mini = i * rows_step
            maxi = (i+1) * rows_step
            minj = j * cols_step
            maxj = (j+1) * cols_step

            sub_img = oimage [mini:maxi, minj:maxj, :]
            p = w.create_sprite(Drable)
            p.texture = ni.get_texture_from_array(sub_img)
            p.scale = 0.98
            p.x = (minj + maxj) / 2
            p.y = (mini + maxi) / 2

            k = imag_row.append(p)

        imag_grid.append(k)

    return imag_grid

wo:List = get_image_grid("hummmm.png", 5, 5)
# shuffle(wo)
# for i in range(len(wo)):
#     for j in range(len(wo[i])):
#         w = wo[i][j].width
              
w.run()