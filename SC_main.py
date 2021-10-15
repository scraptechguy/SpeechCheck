# read README.md file on my GitHub. It walks you through the instalation of necessary
# libraries, helps you solve common errors and provides useful references ;)

# https://github.com/scraptechguy/SpeechCheck


# import library to report time in debug printing

import datetime


# import elements from libraries for Microsoft Text Analytics 

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


# import elements from libraries for Microsoft Speech Services 

import azure.cognitiveservices.speech as speechsdk


# import elements from libraries for Natural Language Tool Kit

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


# import matplot for data visualization

import matplotlib.pyplot as plt


# import wordcloud for common words visualization

from wordcloud import WordCloud, STOPWORDS


# and finally import kivy for gui

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
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView


# input of keys and endpoints from Microsoft Azure for service authentication
# I left those here for you, so you don't have to create new resources. Please don't share those! :)

key1 = "<key>"
endpoint1 = "<endpoint>" # without the slash at the end ;)

speech_key, service_region = "<key>", "<region>"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_config.speech_recognition_language="en-US"
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)



# authenticate client on Azure

def authenticate_client():
    ta_credential = AzureKeyCredential(key1)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint1, 
            credential=ta_credential) 
    return text_analytics_client

client = authenticate_client()



# analyze document sentiment

def sentiment_analysis_example(client):

    global doc_sentiment
    global overall_scores

    documents = [result]
    response = client.analyze_sentiment(documents = documents)[0]
    doc_sentiment = "Document Sentiment: {}".format(response.sentiment)
    overall_scores = "Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    )



# display key meaning of phrase

def key_phrase_extraction_example(client):

    global keyphr

    try:

        documents = [result]

        response = client.extract_key_phrases(documents = documents)[0]

        if not response.is_error:
            
            for phrase in response.key_phrases:

                keyphr = " {}".format(phrase)
                return keyphr

        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))



# load file with kivy design language for gui design (not in a separate file, it's easier)

Builder.load_string(""" 
<w1>
    BoxLayout:
        
        orientation: "vertical"
        size: root.width, root.height
        spacing: 50
        padding: 50

        ScrollView:

            do_scroll_x: False
            do_scroll_y: True
            size_hint: (7, 7)

            Label:
                size_hint_y: None
                height: self.texture_size[1]
                text_size: self.width, None
                text: root.term_text
                pos_hint: {"center_x": 0.5}


        Button:

            id: button1
            text: "Listen to me now!"
            background_normal: 'none'
            background_color: (0, 64/255, 77/255)
            on_release: root.listen()


        Button:

            id: button2
            text: "Stop listening to me"
            background_normal: 'none'
            background_color: (0, 64/255, 77/255)
            on_press: root.stop()


        BoxLayout:

            orientation: "horizontal"


            Button:

                text: "Clear"
                background_normal: 'none'
                background_color: (0, 77/255, 64/255)
                pos_hint: {"center_x": 0.25}
                size_hint: (0.75, 0.75)
                on_press: root.clear()


            Button:

                text: "Spit out charts"
                background_normal: 'none'
                background_color: (0, 77/255, 64/255)
                size_hint: (0.75, 0.75)
                pos_hint: {"center_x": 0.25}
                on_press: root.display_charts()


            Button:
            
                text: "Redo clear"
                background_normal: 'none'
                background_color: (0, 77/255, 64/255)
                pos_hint: {"center_x": 0.75}
                size_hint: (0.75, 0.75)
                on_press: root.redo_clear()
        
""")



# set result (variable to which recognized speech is stored) to blank and done (variable that when False keeps calling 
# azure speech recognition and when True stops listening session) to False

result = " "
done = False


# stop_cb() cuts off azure speech recognition session and set done to True -> in check() if done processes 
# the recognized text

def stop_cb(evt):
    print('CLOSING on {}'.format(evt))
    speech_recognizer.stop_continuous_recognition()
    global done
    done = True


# collectResult() stores recognized utterances into variable result

def collectResult(evt):
    global result 
    result += " {}".format(evt.result.text)


def prn(text):
    now = datetime.datetime.now()
    print("at {}: {} ".format(now, text))



class w1(Widget):

    # term_text is what is displayed in the top label

    term_text = StringProperty()
    

    def __init__(self, **kwargs):

        super(w1, self).__init__(**kwargs)

        self.term_text = "terminal"
        self.fdist = None
        

        # code from here to the three hashes must be called only once as it would otherwise create
        # multiple listening sessions and the variable result would store doubled or tripled (based on how many
        # times have you started the session) results. 

        # create a listening session on Azure for speech recognition
        
        speech_recognizer.recognized.connect(lambda evt: collectResult(evt))
        speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED:    {}'.format(evt)))
        speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
        speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))

        speech_recognizer.session_stopped.connect(stop_cb)
        speech_recognizer.canceled.connect(stop_cb)

        ###



    # create a function listen() that is bined with "Listen to me now!" button 
    # and starts speech recognition. Last but not least listen() runs check() funciton
    # result is cleaned, we don't want to append new results

    def listen(self):

        prn("listen() called")

        global result
        global done

        done = False
        result = " "

        speech_recognizer.start_continuous_recognition()

        self.term_text = "Listening..."

        self.check(0)


    # create a function check() that checks (duh...) if done is True (done is set to True in stop_cb() function)
    # recognized text is processed and result is displayed on screen
    # if done is false, check() checks again after a little while (love my function naming xd)

    def check(self, dt):    # dt stands for delta time and is not crucial
        global done
        prn("check() called")


        if done:
            prn("check() - done = True")
            self.process()
            done = False

        else:
            prn("check scheduled")
            Clock.schedule_once(self.check, 1)
            

    # stop() function is binded to "stop listening to me" button and when pressed, stops speech recognition 
    # by stop_cb(), it then triggers process function and displays results on the screen

    def stop(self):

        stop_cb(None)
        

    # process function processes (duh... x2) recognized text and is triggered by stop() function

    def process(self):

        prn("process() called")

        # split up text to separate words

        tokenized_word = word_tokenize(result)


        # execute Azure functions 

        sentiment_analysis_example(client)

        key_phrase_extraction_example(client)


        # execute NLTK 

        self.fdist = FreqDist(tokenized_word)    

        moscom = self.fdist.most_common(2) # most common words (or words, change number in brackets


        # display 

        self.term_text = " {} \n \n {} \n {} \n {} \n {} ".format(
        result,
        doc_sentiment,
        overall_scores,
        keyphr,
        moscom,
            )

    
    # display_charts() binded to "stpit out charts" button displays (duh... x3) most frequent words' plot and wordcloud

    def display_charts(self):

        if self.fdist == None:
            return
        
        # execute matplot (data visualization)
       
        self.fdist.plot(30,cumulative=False)


        # Create and generate a word cloud image:

        wordcloud = WordCloud().generate(result)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")

        wordcloud.generate(result)
        plt.show()


    # Clear stores term_text to a separate variable and 
    # clears (duh... x4) text displayed in the top label 

    def clear(self):

        global redo

        self.redo = self.term_text
        self.term_text = "terminal"


    # if you're stupid enough to accidentaly press a button, I got you. redo_clear() redos
    # clear() function (bet you were expecting duh... x5, hah)

    def redo_clear(self):
        self.term_text = self.redo




class DaApp(App):
    def build(self):
        return w1()


if __name__ == '__main__':
    DaApp().run()
