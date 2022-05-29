from pycat.core import Window, Color, Sprite, KeyCode
from pycat.experimental.ldtk import LdtkFile
from pycat.experimental.movement import FourWayMovementController as Controller
from pycat.experimental.animation import Animator
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
        self.state = Player.State.WALK
        self.time = 0
        self.reset = w.get_sprite_with_tag("player_start")[0].position
        self.scale = 22
        self.names = ["jump","lick","lickb","look","paw","run","scared","sit","sleep","sprint"]
        frames = [7,4,4,4,6,8,8,4,4,8]
        directory = "animation_data/cat/"
        eachmove = get_easier(self.names,frames,directory)
        self.animator = Animator(eachmove)
        self.animator.play("jump")
        self.image = self.animator.tick(0)
        

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

        self.image = self.animator.tick(dt)
        if w.is_key_pressed(KeyCode.Z):
            
            self.animator.play("look")
        elif w.is_key_pressed(KeyCode.X):
            
            self.animator.play("paw")
        elif w.is_key_pressed(KeyCode.C):
            
            self.animator.play("run")
        elif w.is_key_pressed(KeyCode.V):
            
            self.animator.play("scared")
        elif w.is_key_pressed(KeyCode.B):
            
            self.animator.play("sit")
        elif w.is_key_pressed(KeyCode.N):
            
            self.animator.play("sleep")
        elif w.is_key_pressed(KeyCode.M):
            
            self.animator.play("sprint")
        elif w.is_key_pressed(KeyCode.SPACE):
           
            self.animator.play("jump")
        elif w.is_key_pressed(KeyCode.LSHIFT):
            
            self.animator.play("lickb")
        elif w.is_key_pressed(KeyCode.LCTRL):
            
            self.animator.play("lick")

w = Window(is_sharp_pixel_scaling= True)
a = Animator()

def get_easier(name, frames, drectory):
    images = [[drectory + name[i]+ str(j+1) +".png"
              for j in range(1,frames[i])]
              for i in range(len(name))]
    return {name[i]:images[i] for i in range(len(name))}


player = w.create_sprite(Player)

w.run()