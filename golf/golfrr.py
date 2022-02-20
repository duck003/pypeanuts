from pycat.core import Window, Sprite, Point

w = Window()

class Line(Sprite):

    def on_create(self):
        
        self.line = w.create_line() 
    
    def on_update(self, dt):
        a = Point(0,0)
        b = w.mouse_position
        self.line.set_start_end(a,b)

line = w.create_sprite(Line)
w.run()