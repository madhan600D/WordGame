import random
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import LabelBase
from kivy.properties import ObjectProperty
from kivy.animation import Animation
LabelBase.register(name="pacifico",fn_regular="Pacifico.ttf")
LabelBase.register(name="tusj",fn_regular="FFF_Tusj.ttf")
LabelBase.register(name="lcd",fn_regular="game_over.ttf")
LabelBase.register(name="3D",fn_regular="3D.ttf")


class Console(BoxLayout):
    counter=5
    found=1
    words= {
    'happy': 'A emotion we seek',
    'enemy': 'The person who opposes you',
    'ironman': "Famous dialogue I'M *******",
    'keyboard': 'Has all alphabets in it',
    'supercar': 'Has more cylinders',
    'space': 'Cold vast emptiness',
    'jupiter': 'can have 1000 earth inside it',
    'computer': 'A artificial Brain',
    'science': 'The universe comes under its principals',
    'programming': 'Used to communicate with a device with Multiple transistors',
    'python': 'Relation SNAKE-COMPUTER',
    'awesome': 'A cheer word',
    'moon': 'A mini satellite we didnt intend to put',
    'stars': 'cant count them'
    }

    currword = random.choice(list(words.keys()))
    curlist=list(currword)
    temp=list(currword)
    displaylist=[]
    for i in range(len(currword)):
        displaylist.append('_')
    def start(self):
        self.counter=5
        self.ids.display_label.text = " ".join(self.displaylist)
        self.ids.chance_display.text=f"YOUR LIVES: {self.counter}"
    def game(self,key):
        if(self.counter<=0):
            self.ids.display_label.text=f"You lose,the word is {self.currword}"
            return
        if(self.found==len(self.currword)):
            self.ids.display_label.text=f"You won,the word is {self.currword}"
            return
        if(key not in self.curlist):
            self.counter-=1
            self.ids.chance_display.text=f"YOUR LIVES: {self.counter}"
            return
        for i in self.curlist:
            if(key==i):
                self.curlist.remove(i)
                self.found+=1
                for j in range(len(self.temp)):
                    if(self.temp[j]==key):
                        self.displaylist[j]=key
        
        self.ids.display_label.text=" ".join(self.displaylist)
    def hint(self):
        hintdisp=self.words[self.currword]
        self.ids.hint_label.text=hintdisp
        self.counter-=2
        self.ids.chance_display.text=f"YOUR LIVES: {self.counter}"
class wordHunt(App):
    pass
class BackgroundColorLayout(BoxLayout):
    pass
class Button_animate(Button):
    def on_press(self):
        animate = Animation(size=(self.height * 0.8, self.width * 0.8),background_color=(0,0,0,.2), duration=0.2)
        animate.start(self)
    def on_release(self):
        animate = Animation(size=(self.height * 1, self.width * 1),background_color=(0,0,0,.4),duration=0.2)
        animate.start(self)


    def reset_button(self):
        self.size=(self.height,self.width)
        self.background_color=(0,0,0,.9)


wordHunt().run()
