from pycat.core import Window, Sprite, Color, Scheduler
from random import randint

M = 6
N = 8

CELL_SIZE = 100

w = Window(width=N*CELL_SIZE, height= M*CELL_SIZE)

class Cell0(Sprite):

    def on_create(self):
        self.scale = CELL_SIZE * 0.98
        self.color = Color.GREEN

    def on_left_click(self):
        self.toggle_neghbor()
        self.test_win()
    
    def grid_ij (self, i , j):
        self.i = i
        self.j = j

    def toggle_neghbor(self):
        i = self.i
        j = self.j
        if i+1 < M:
            grid0[i+1][j].toggle_color()
        if i-1 >= 0 :
            grid0[i-1][j].toggle_color()
        if j+1 < N :
            grid0[i][j+1].toggle_color()
        if j-1 >= 0 :
            grid0[i][j-1].toggle_color()
        
    
    def toggle_color(self):
        if self.color == Color.GREEN:
            self.color = Color.AZURE
        else:
            self.color = Color.GREEN

    def test_win(self):
        for i in range(M):
            for j in range(N):
                if grid0[i][j].color == Color.AZURE:
                    return
        print("YOU WIN! huh!")
        Scheduler.wait(0.26, w.close)  

grid0 = [
    [w.create_sprite(Cell0)for j in range (N)]for i in range (M) 
]

x0 = y0 = CELL_SIZE/2

for i in range (M):
    for j in range (N):
        grid0[i][j].x = x0 + j * CELL_SIZE
        grid0[i][j].y = y0 + i * CELL_SIZE
        grid0[i][j].grid_ij(i,j)

def ran(dt):
    c = 0
    i = randint(0,M-1)
    j = randint(0,N-1)
    grid0[i][j].toggle_neghbor()
    c += 1
    if c > 9:
        Scheduler.cancel_update()

Scheduler.update(ran, delay=1)

w.run()