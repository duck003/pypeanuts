import cv2 as cv
import numpy as np
from PIL.Image import Image, fromarray, FLIP_TOP_BOTTOM, new
from pycat.base import NumpyImage as IP
from pycat.base.numpy_image import ndarray
from pycat.core import Sprite, Window

from os.path import abspath, dirname, exists
from os import makedirs

from typing import List
from transparent_gif import save_transparent_gif


class IPSprite(Sprite):
    def on_create(self):
        self.image = 'tower_small.jpeg'
        self.position = w.center
        self.save_image('test.png')
        self.set_texture(self.get_gradient())

    def get_image_array(self) -> ndarray:
        array = IP.get_array_from_texture(self.texture)
        return array[:, :, :3]

    def get_luminance_array(self, array: ndarray = None) -> ndarray:
        if array is None:
            IP.get_luminance_array(self.get_image_array())
        return IP.get_luminance_array(array)

    def set_texture(self, array: ndarray):
        self.texture = IP.get_texture_from_array(array)

    def get_gradient(self, array: ndarray = None) -> ndarray:
        if array is None:
            array = self.get_luminance_array(self.get_image_array())
        else:
            array = self.get_luminance_array(array)
        sobelx64f = cv.Sobel(array, cv.CV_64F, 1, 0, ksize=3)
        sobely64f = cv.Sobel(array, cv.CV_64F, 0, 1, ksize=3)
        abs_sobelx64f = np.absolute(sobelx64f)
        sobelx_8u = np.uint8(abs_sobelx64f)
        abs_sobely64f = np.absolute(sobely64f)
        sobely_8u = np.uint8(abs_sobely64f)
        return cv.addWeighted(sobelx_8u, 0.5, sobely_8u, 0.5, 0)

    def get_image(self, array: ndarray = None) -> Image:
        if array is None:
            array = self.get_image_array()
        img = fromarray(array)
        return img.transpose(FLIP_TOP_BOTTOM)

    def get_clear_background_image(self, array: ndarray = None) -> Image:
        if array is None:
            array = self.get_image_array()
        h, w = array.shape[:2]
        return new('RGBA', (w, h), (0, 0, 0, 0))

    def save_image(self, filename: str, img: Image = None):
        if img is None:
            img: Image = self.get_image()
        dir = dirname(abspath(__file__)) + '/saved_images'
        if not exists(dir):
            makedirs(dir)
        img.save(dir + '/' + filename)

    def make_gif(self, frames: List[Image], duration: List[int] = None):
        if duration is None:
            duration = 1
        else:
            assert len(duration) == len(frames)
        dir = dirname(abspath(__file__)) + '/saved_images'
        if not exists(dir):
            makedirs(dir)
        save_transparent_gif(frames, duration, dir + '/' + 'out.gif')


if __name__ == '__main__':
    w = Window()
    img = w.create_sprite(IPSprite)
    w.run()
