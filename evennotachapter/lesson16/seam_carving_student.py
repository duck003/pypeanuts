from ip_sprite import IPSprite, np
from pycat.core import Window
from typing import List
w = Window()


class SeamCarvedImage(IPSprite):

    def on_create(self):
        self.image = 'tower_small.jpeg'
        self.position = w.center
        self.array = self.get_image_array()
        self.gradient = self.get_gradient()
        self.resized_width = self.width // 2
        self.show_seam = True
        self.seam = None
        # self.output_gif()

    def output_gif(self):
        frames = []
        n = 200
        for i in range(n):
            background = self.get_clear_background_image()
            img = self.get_image(self.seam_carve())
            background.paste(img, (0, 0))
            frames.append(background)
            print(i)

        img = self.get_image(self.seam_carve(get_seam=False))
        background.paste(img)
        frames.append(background)
        duration = (n*[1]) + [2000]
        self.make_gif(frames, duration)

    def seam_carve(self, get_seam=True):
        self.set_minimum_seam()
        self.show_min_seam()
        array = self.array
        self.remove_min_seam()
        self.gradient = self.get_gradient(self.array)
        return array if get_seam else self.array

    def on_update(self, dt):
        if self.width > self.resized_width:
            if self.show_seam:
                self.set_minimum_seam()
                self.show_min_seam()
                self.set_texture(self.array)
            else:
                self.remove_min_seam()
                self.set_texture(self.array)
                self.gradient = self.get_gradient()
            self.show_seam = not self.show_seam

    def set_minimum_seam(self):
        rows, cols = self.gradient.shape
        dp: List[List[int]] = self.gradient.tolist()
        # finish implementing this method in exercise 1 and 2
        # set the min seam in self.seam
        self.seam = [0] * rows

    def remove_min_seam(self):
        rows, _ = self.gradient.shape
        assert(len(self.seam) == rows)
        self.gradient = np.array([np.delete(self.gradient[i], self.seam[i])
                                  for i in range(rows)])
        self.array = np.array([np.delete(self.array[i], self.seam[i], axis=0)
                               for i in range(rows)])

    def show_min_seam(self):
        rows = self.array.shape[0]
        assert(len(self.seam) == rows)
        for i in range(rows):
            self.array[i, self.seam[i]] = [255, 0, 0]


w.create_sprite(SeamCarvedImage)
w.run()
