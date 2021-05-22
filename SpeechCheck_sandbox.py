# Just a place for ideas

import kivy
from kivy.app import App
from kivy.core import text 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.properties import StringProperty


Builder.load_string(""" 

<w1>

    BoxLayout:
        
        orientation: "vertical"
        size: root.width, root.height
        spacing: 50
        padding: 50


        Label:

            id: label1
            text: root.term_text
            bold: True
            size_hint: (3, 3)
            pos_hint: {"center_x": 0.5}


        Button:

            id: button1
            text: "Listen to me now!"
            background_color: (0, 64/255, 77/255)
            on_press: root.press()


        BoxLayout:

            orientation: "horizontal"


            Button:

                text: "Clear"
                background_color: (0, 77/255, 64/255)
                pos_hint: {"center_x": 0.25}
                size_hint: (0.75, 0.75)
                on_press: root.clear()

            Button:
            
                text: "Redo clear"
                background_color: (0, 77/255, 64/255)
                pos_hint: {"center_x": 0.75}
                size_hint: (0.75, 0.75)
                on_press: root.redo_clear()

        
        BoxLayout:

            orientation: "horizontal"


            Button:

                text: "Save total score"
                background_color: (0, 77/255, 64/255)
                size_hint: (0.75, 0.75)
                pos_hint: {"center_x": 0.25}


            Button:

                text: "Display total score progression"
                background_color: (0, 77/255, 64/255)
                size_hint: (0.75, 0.75)
                pos_hint: {"center_x": 0.75}


                 

""")


class w1(Widget):
    term_text = StringProperty()
    
    def __init__(self, **kwargs):
        super(w1, self).__init__(**kwargs)
        self.term_text = "terminal"

    def press(self):
        self.term_text = "Listening"

    def clear(self):
        global redo 
        self.redo = self.term_text
        self.term_text = "terminal"

    def redo_clear(self):
        self.term_text = self.redo

class DaApp(App):
    def build(self):
        return w1()



