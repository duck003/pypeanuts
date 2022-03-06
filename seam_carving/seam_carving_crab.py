from ip_sprite import IPSprite, np
from pycat.core import Window
from typing import List

w = Window()


class SeamCarvedImage(IPSprite):

    def on_create(self):
        self.image = 'crab.jpg'
        self.position = w.center
        self.array = self.get_image_array()
        self.gradient = self.get_gradient()
        self.resized_width = self.width // 2
        self.show_seam = True
        self.seam = None
        self.output_gif()

    def output_gif(self):
        frames = []
        for i in range(50):
            background = self.get_black_background_image()
            img = self.get_image(self.seam_carve())
            background.paste(img, (0, 0))
            frames.append(background)
            print(i)

        img = self.get_image(self.seam_carve(get_seam=False))
        background.paste(img)
        frames.append(background)
        self.make_gif(frames)

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

        for i in range (1, rows):
            for j in range(cols):
                if j == 0:
                    dp[i][j] += min(dp[i-1][j:j+2])
                elif j == cols-1:     
                    dp[i][j] += min(dp[i-1][j-1:j+1])
                else:                
                    dp[i][j] += min(dp[i-1][j-1:j+2])
        
        row = dp[-1]
        self.seam = []
        j = row.index(min(row))
        self.seam.append(j)
        for i in range(rows-2,-1,-1):
            if j == 0:
                a,b = dp[i][j:j+2]
                if b < a:
                    j += 1
                self.seam.append(j)
            elif j == cols-1:
                a,b = dp[i][j-1:j+1]
                if a < b:
                    j -= 1     
                self.seam.append(j)
            else:
                a,b,c = dp[i][j-1:j+2]
                if a < b and a < c:
                    j -= 1
                elif c < b and c<a:
                    j += 1
                self.seam.append(j)
        self.seam.reverse()
                
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
