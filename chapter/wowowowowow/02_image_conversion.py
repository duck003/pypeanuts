from pycat.core import Window, Sprite, KeyCode
from pycat.base import NumpyImage as Image
import random
w = Window()
original_image = Image.get_array_from_file("baboon.jpeg")


def get_max_rgb_image():
    rows, cols, channels = original_image.shape
    new_image = Image(rows, cols)
    for i in range(rows):
        for j in range(cols):
            r, g, b, a = original_image[i][j]
            new_image[i][j] = max(r, g, b)
    return new_image


def get_luminance_image():
    rows, cols, channels = original_image.shape
    luminance_image = Image(rows, cols)
    for i in range(rows):
        for j in range(cols):
            r, g, b, a = original_image[i][j]
            luminance_image[i][j] = .299 * r + .587 * g + .114 * b
    return luminance_image


def get_complement_image():
    rows, cols, channels = original_image.shape
    complement_image = Image(rows, cols, channels)
    for i in range(rows):
        for j in range(cols):
            r, g, b, a = original_image[i][j]
            complement_image[i][j] = [255-r, 255-g, 255-b, a]
    return complement_image

def what_the():
    rows, cols, channels = original_image.shape
    ohman_image = Image(rows, cols, channels)
    for i in range(rows):
        for j in range(cols):
            r, g, b, a = original_image[i][j]
            ohman_image[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    return ohman_image

    


max_rgb_image = get_max_rgb_image()
luminance_image = get_luminance_image()
complement_image = get_complement_image()
ohman_image = what_the()
# Extensions: add functions to extract the R G B functions


class ImageTest(Sprite):

    def on_create(self):
        self.texture = Image.get_texture_from_array(original_image)
        self.scale = 2
        self.position = w.center

    def on_update(self, dt):
        if w.get_key_down(KeyCode.UP):
            self.texture = Image.get_texture_from_array(original_image)
        if w.get_key_down(KeyCode.DOWN):
            self.texture = max_rgb_image.texture
        if w.get_key_down(KeyCode.LEFT):
            self.texture = luminance_image.texture
        if w.get_key_down(KeyCode.RIGHT):
            self.texture = complement_image.texture
        if w.get_key_down(KeyCode.Z):
            self.texture = ohman_image.texture

w.create_sprite(ImageTest)
w.run()
