from ip_sprite import IPSprite, np
from pycat.core import Window
from typing import List

w = Window(height=800)

class SeamCarvedImage(IPSprite):

    def on_create(self):
        self.image = 'tower.jpg'
        self.position = w.center
        self.array = self.get_image_array()
        self.gradient = self.get_gradient()
        self.resized_width = self.width-1
        self.show_seam = True
        self.seam = None
        # self.output_gif()

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
        
        for j in range (1, cols):
            for i in range(rows):
                a = dp[i-1][j-1]
                b = dp[i][j-1]
                if i == 0:
                    c = dp[i+1][j-1]
                    dp[i][j] += min(b,c)
                elif i == rows-1:     
                    dp[i][j] += min(a,b)
                else:
                    c = dp[i+1][j-1]                
                    dp[i][j] += min(a,b,c)
        
        col = dp[-1]
        self.seam = []
        i = col.index(min(col))
        self.seam.append(i)
        for j in range(cols-2,-1,-1):
            if i == 0:
                a = dp[i][j]
                b = dp[i+1][j]
                if b < a:
                    i += 1
                self.seam.append(i)
            elif i == rows-1:
                b = dp[i-1][j]
                c = dp[i][j]
                if a < b:
                    i -= 1     
                self.seam.append(i)
            else:
                a = dp[i-1][j]
                b = dp[i][j]
                c = dp[i+1][j]
                if a < b and a < c:
                    i -= 1
                elif c < b and c < a:
                    i += 1
                self.seam.append(i)
        self.seam.reverse()
                
    def remove_min_seam(self):

        self.gradient = np.transpose(self.gradient)
        self.array = np.transpose(self.array, (1, 0, 2))
        rows, _ = self.gradient.shape
        assert(len(self.seam) == rows)
        self.gradient = np.array([np.delete(self.gradient[i], self.seam[i])
                                  for i in range(rows)])
        self.array = np.array([np.delete(self.array[i], self.seam[i], axis=0)
                               for i in range(rows)])
        self.gradient = np.transpose(self.gradient)
        self.array = np.transpose(self.array, (1, 0, 2))
        
            
    def show_min_seam(self):
        cols = self.array.shape[1]
        assert(len(self.seam) == cols)
        for j in range(cols):
            self.array[self.seam[j], j ] = [255, 0, 0]

w.create_sprite(SeamCarvedImage)
w.run()