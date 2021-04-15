# Just a place for ideas

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from speech_recognition import Microphone, Recognizer

rec = Recognizer()
mic = Microphone()


class Grid(GridLayout):

    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="Name: "))

        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.speak = Button(text="Listen to me now!", font_size=32)
        self.speak.bind(on_press=self.speak_click)
        self.add_widget(self.speak)

    def speak_click(self, instance):

        with mic:
            rec.adjust_for_ambient_noise(mic, duration=5)

            print("Talk now mate")
            speech = rec.record(mic, 3)

        while True:

            try:
                script = rec.recognize_google(speech)
                print("You said: ", script)
                break

            except:
                print("Sorry, inaudible. :(")

        self.add_widget(Label(text="You said: {}". format(script)))


class DaApp(App):
    def build(self):
        return Grid()


if __name__ == '__main__':
    DaApp().run()
    
