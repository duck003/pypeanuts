from pycat.core import Window, Color, Sprite, KeyCode
from pycat.experimental.ldtk import LdtkFile
from pycat.experimental.movement import FourWayMovementController as Controller
from enum import Enum, auto
from os.path import dirname

w= Window(width=17*32, height=12*32)

dir = dirname(__file__)
ldtk_file = LdtkFile(dir + '/jumping_levels2.ldtk')
ldtk_file.render_level(w, 'Level_0')


class Player(Sprite):

    class State(Enum):
        WALK = auto()
        JUMP = auto()
        DROWN =auto()
    
    normal_scale = 0.11
    Gravity = -1
    timeneed = 1

    def on_create(self):
        self.movement_controller = Controller(w, speed_factor=25)
        self.layer = 10
        self.scale = 0.11
        self.image = "slimee.jpg"
        self.state = Player.State.WALK
        self.time = 0
        self.reset = w.get_sprites_with_tag("player_start")[0].position

    def jump(self,dt):
        self.time += dt
        self.scale = Player.Gravity * self.time * (self.time - Player.timeneed) + Player.normal_scale

    def on_update(self, dt):
        self.position += self.movement_controller.get_movement_delta(dt)
    
        if self.state is Player.State.WALK:
            if w.is_key_down(KeyCode.SPACE):
                self.state = Player.State.JUMP
                self.time = 0
            elif not self.is_touching_any_sprite_with_tag('land'):
                self.position = self.reset
                self.state = Player.State.WALK
    
        elif self.state is Player.State.JUMP:
            self.jump(dt)
            if self.time > self.timeneed:
                self.state = Player.State.WALK
                self.scale = self.normal_scale
                if not self.is_touching_any_sprite_with_tag("land"):
                    self.position = self.reset

player = w.create_sprite(Player)

w.run()