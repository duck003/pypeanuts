from turtle import position, window_height, window_width
from pycat.base import NumpyImage
from pycat.core import Window

w = Window(width =600, height = 400)

oimage = NumpyImage.get_array_from_file("hummmm.png")
print(oimage.shape)

image01 = NumpyImage.get_texture_from_array(oimage[:84, :150 :])
image02 = NumpyImage.get_texture_from_array(oimage[:84, 150: :])
image03 = NumpyImage.get_texture_from_array(oimage[84:, :150 :])
image04 = NumpyImage.get_texture_from_array(oimage[84:, 150: :])

x0y0 = w.create_sprite(x = 225,y = 158)
x1y0 = w.create_sprite(x = 375,y = 158)
x0y1 = w.create_sprite(x = 225,y = 242)
x1y1 = w.create_sprite(x = 375,y = 242)

x0y0.texture = image01
x1y0.texture = image02
x0y1.texture = image03
x1y1.texture = image04

w.run()