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
    

    ###################################################################################
    
    
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords


from speech_recognition import Microphone, Recognizer 


rec = Recognizer()
mic = Microphone()

with mic:
    rec.adjust_for_ambient_noise(mic, duration=5)

    print("Talk now mate")
    audio = rec.record(mic, 3)


try:
    text = rec.recognize_google(audio)
    print("You said: ", text)        

except:
    print("Sorry, inaudible. :(")

# breaking down a text paragraph to sentenses

tokenized_sent=sent_tokenize(text)
print(tokenized_sent)


# breaking down a text paragraph to words

tokenized_word=word_tokenize(text)
print(tokenized_word)


# displaying number of samples and outcomes

fdist = FreqDist(tokenized_word)
print(fdist)


# finding most common word (or words, for that change number in brackets)

print(fdist.most_common(1))


# filtering stopwords 

stop_words=set(stopwords.words("english"))

filtered_sent=[]
for w in tokenized_sent:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Sentence:",tokenized_sent)
print("Filterd Sentence:",filtered_sent)

