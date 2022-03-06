from pycat.core import Window, Sprite, Color, Point, KeyCode, Label, Scheduler
import random
from enum import Enum
from os import path, read

window = Window(width=1200, height=800)

filer = path.dirname(__file__) 


def get_words_from_file(filename):

    file1 = open(filer +'/'+ filename)
    word = file1.readline()
    file1.close()
    return word
    

verbs = get_words_from_file('verbs.txt')
nouns = get_words_from_file('nouns.txt')
adjectives = get_words_from_file('adjectives.txt')

class GameMode(Enum):
    Noun=1
    Verb=2
    Adjective=3

state = GameMode.Noun
goal_label = window.create_label(text=str(state))

score = 0
score_label = window.create_label(text='0', x=400)

class Word(Sprite):
    def on_create(self):
        self.image = '1.png'
        
        self.x = random.randint(100,1100)
        self.y = 800
        self.label = window.create_label(font_size=30)        

        self.label.text = random.choice(verbs+nouns+adjectives)        

        self.scale = 0.5
        self.width = self.label.content_width + 100
        self.label.x = self.x - self.label.content_width / 2
        self.label.y = self.y + self.label.content_height / 2

    def on_update(self,dt):
        self.y -= 1
        self.label.y -= 1

        if self.is_touching_window_edge():
            self.delete()
            self.label.delete()

    def process_click(self, score_change_value):
        global score 
        score += score_change_value
        score_label.text = str(score)
        self.delete()
        self.label.delete()           

    def on_left_click(self):
        if state == GameMode.Noun and self.label.text in nouns:
            self.process_click(1)
        elif state == GameMode.Verb and self.label.text in verbs:
            self.process_click(1)
        elif state == GameMode.Adjective and self.label.text in adjectives:
            self.process_click(1)
        else:
            self.process_click(-1)
        

def change_to_random_state():
    global state
    state = random.choice([GameMode.Noun, GameMode.Verb, GameMode.Adjective])
    goal_label.text = str(state)

Scheduler.update(change_to_random_state, 5)


def make_a_word():
    window.create_sprite(Word)

Scheduler.update(make_a_word, 1)


window.run()

