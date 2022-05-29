from pycat.core import Window, Color, Sprite, KeyCode
from pycat.experimental.ldtk import LdtkFile
from pycat.experimental.movement import FourWayMovementController as Controller
from enum import Enum, auto

w= Window(width=17*32, height=12*32)

ldtk_file = LdtkFile('jumping_levels2.ldtk')
print(ldtk_file.get_level)
ldtk_file.render_level(w, 'Level_0')


class Player(Sprite):

    class State(Enum):
        WALK = auto()
        JUMP_UP = auto()
        JUMP_DN = auto()
        DROWN =auto()
    
    Normal_scale = 0.11
    MAX_scale = 0.2
    scale_speed = 0.01

    def on_create(self):
        self.movement_controller = Controller(w, speed_factor=25)
        self.layer = 10
        self.scale = 0.11
        self.image = "slimee.jpg"
        self.state = Player.State.WALK


    def jump(self, cspeed):
        self.scale += cspeed       

    def on_update(self, dt):
        self.position += self.movement_controller.get_movement_delta(dt)
    
        if self.state is Player.State.WALK:
            if w.is_key_down(KeyCode.SPACE):
                self.state = Player.State.JUMP_UP
    
        elif self.state is Player.State.JUMP_UP:
            self.jump(self.scale_speed)
            if self.scale > self.MAX_scale:
                self.state = Player.State.JUMP_DN

        elif self.state is Player.State.JUMP_DN: 
            self.jump(-self.scale_speed)
            if self.scale < self.Normal_scale:
                self.state = Player.State.WALK

player = w.create_sprite(Player)

w.run()