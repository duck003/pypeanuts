from pycat.core import Window, Sprite, Color
from pycat.base.event import MouseEvent, MouseButton
import random
from pycat.label import Label
from typing import List
from enum import Enum

thew = 9
theh = 9     
gap = 2

w = Window(width=thew*60-gap*thew, height=theh*60)

class State(Enum):
    PLAY = 1
    STOP = 0

now_state = State.PLAY

class CountBomb(Label):

    def on_create(self):
        self.layer = 1
        self.font_size = 25


class Flag(Sprite):

    def on_create(self):
        self.image = "flag.png"
        self.scale = 0.18
        self.layer = 4

    def on_left_click(self):
        self.delete()

def test(i ,j):
    global now_state
    if grid[i][j]:
        print("win")
        now_state = State.STOP
        

class Blank (Sprite):
    
    def on_create(self):
        self.color = Color.WHITE
        self.scale = 40
        self.layer = 2

    def set_ij(self, i, j):
        self.i = i
        self.j = j
    
    def on_left_click(self):
        global now_state
        if now_state == State.PLAY:
            self.delete()
            test(self.i, self.j)

    def on_click(self, mouse_event: MouseEvent):
        if mouse_event.button == MouseButton.RIGHT and now_state == State.PLAY: 
            flag = w.create_sprite(Flag)
            flag.position = self.position

    
class Bomb (Sprite):
    
    def on_create(self):
        self.scale = 0.2
        self.image = "bomb.png"
        self.layer = 1


class ABlank(Sprite):

    def on_create(self):
        self.color = Color.AZURE    
        self.scale = 40
        self.layer = 0
        self.lw = w.create_label(CountBomb)
        self.lw.color = Color.BLACK
        
    
    def count(self, i, j):
        count = 0
        neighbors = []
        neighbors = [[i-1,j-1],[i-1,j],[i-1,j+1],
                    [i  ,j-1],[i,j+1],
                    [i+1,j-1],[i+1,j],[i+1,j+1]]
        for n in neighbors:
            ii, jj = n
            #check ii jj in range
            if ii >=0 and jj >= 0:
                if ii < theh and jj < thew:
                    if grid[ii][jj] and grid[ii][jj].image == 'bomb.png':
                        count += 1
        if grid[i][j]:
            return
        if count > 0:
            self.lw.text = str(count)

        
for i in range (thew):
    for j in range(theh):
        blankr = w.create_sprite(Blank)
        blankr.x = blankr.width/2 + gap + j*60
        blankr.y = blankr.height/2 + gap + i*60
        blankr.set_ij(i,j)

grid: List[List[Bomb]] = [[None for i in range(theh)]for j in range (thew)]

def spawnbomb(): 
    i = random.randint(0,theh-1)    
    j = random.randint(0,thew-1)
    while not grid[i][j] is None:
        i = random.randint(0,theh-1)    
        j = random.randint(0,thew-1)
    bombr = w.create_sprite(Bomb)
    bombr.x = blankr.width/2 + gap + j*60
    bombr.y = blankr.height/2 + gap + i*60
    grid[i][j] = bombr
         

for i in range(9):
    spawnbomb() 

for i in range (thew):
    for j in range(theh):
        blanklr = w.create_sprite(ABlank)
        blanklr.x = blankr.width/2 + gap + j*60
        blanklr.y = blankr.height/2 + gap + i*60
        blanklr.count(i, j)
        blanklr.lw.x = blanklr.x - blanklr.width/2 + gap
        blanklr.lw.y = blanklr.y + blanklr.height/2 - gap
        blanklr.lw.layer = 1

w.run()