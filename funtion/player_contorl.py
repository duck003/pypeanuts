from pycat.core import Point

class Control1D:

    def __init__(self, forward_key, backward_key, direction:Point, player):
        self.forward_key = forward_key
        self.backward_key = backward_key
        self.direction:Point = direction
        self.player = player

    def update(self):
        if self.player.window.is_key_pressed(self.forward_key):
            self.player.position += self.direction*10
        elif self.player.window.is_key_pressed(self.backward_key):
            self.player.position -= self.direction*10


class Control2D:
    
    def __init__(self, up_key, down_key, left_key, right_key, directon1:Point, directon2:Point, player):
        self.up_key = up_key
        self.down_key = down_key
        self.left_key = left_key
        self.direction1 = directon1
        self.direction2 = directon2
        self.right_key = right_key
        self.player = player

        self.control01 = Control1D(self.up_key, self.down_key, self.direction1, self.player) 
        
        self.control02 = Control1D(self.left_key, self.right_key, self.direction2, self.player) 

    def update(self):
        self.control01.update()
        self.control02.update()