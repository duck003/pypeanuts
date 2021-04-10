from pycat.core import Color, KeyCode, Scheduler, Sprite, Window, Label
import random

w = Window()

class Duck(Sprite):

    def on_create(self):
        self.add_tag('aa')
        self.color = Color.AMBER
        self.x = 100
        self.scale = 60
        self.speed = 10
        self.health = 100
        self.point = 0
    def on_update(self, dt):
        if w.get_key(KeyCode.W):
            self.y += self.speed
        if w.get_key(KeyCode.S):
            self.y -= self.speed
        if w.get_key(KeyCode.D):
            w.create_sprite(Bullet)
        if w.get_key(KeyCode.A):
            w.create_sprite(Bullet)            

    def on_left_click_anywhere(self):
        w.create_sprite(Bullet)

class Bullet(Sprite):

    def on_create(self):
        self.add_tag('bb')
        self.position = player.position
        self.scale = 10
        self.color = Color.random_rgb()
        self.speed = 10
        self.point_toward_mouse_cursor()
    
    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.touching_window_edge():
            self.delete()

class Emeny(Sprite):

    def on_create(self):
        self.goto_random_position()
        self.scale = 40
        self.x = 1100 
        self.speed = 5
        self.time01 = 0
        self.time02 = 2
    def on_update(self, dt):
        self.x -= self.speed
        self.time01 += dt
        if self.time01 > self.time02:
            b = w.create_sprite(EBullet) 
            b.rotation = 180
            b.position = self.position
            self.time01 = 0
        if self.touching_window_edge():
            self.delete()
            player.health -= 1 
            scllabel.text = "HEALTH: " +str(player.health)
        elif self.touching_any_sprite_with_tag("bb"):
            self.delete()
            player.point += 1 
            sclabel.text = "POINT: " +str(player.point)
        elif self.touching_any_sprite_with_tag('aa'):
            self.delete()
            player.point += 1 
            sclabel.text = "POINT: " +str(player.point)
            player.health -= 1 
            scllabel.text = "HEALTH: " +str(player.health)

class EBullet(Sprite):

    def on_create(self):
        self.scale = 10
        self.color = Color.RED
        self.speed = 10
    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.touching_window_edge():
            self.delete()
            if self.touching_window_edge():
                self.delete()
                player.health -= 1 
                scllabel.text = "HEALTH: " +str(player.health)
        elif self.touching_any_sprite_with_tag("bb"):
                self.delete()
        elif self.touching_any_sprite_with_tag('aa'):
                self.delete()
                player.health -= 1 
                scllabel.text = "HEALTH: " +str(player.health)


sclabel = Label("POINT: 0",x=200,y=600)
w.add_label(sclabel)
scllabel = Label("HEALTH: 100",x=20,y=600)
w.add_label(scllabel)

li01 = Label("You LOSE!",x=600,y=600)
li02 = Label("You WIN!",x=600,y=600)

player = w.create_sprite(Duck)
EM = Emeny
def spawn_enemy():
    w.create_sprite(Emeny)


Scheduler.update(spawn_enemy, delay=0.99)


# if float(player.health) == 0:
#     w.add_label(li01)
# if float(player.point) == 100:
#     w.add_label(li02)

w.run()