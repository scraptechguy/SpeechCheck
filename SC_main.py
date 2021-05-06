
# import of elements from libraries for Microsoft Text Analytics 

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


# import of elements from libraries for Microsoft Speech Services 

import azure.cognitiveservices.speech as speechsdk


# import of elements from libraries for Natural Language Tool Kit

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


# import of matplot for data visualization

import matplotlib.pyplot as plt


# input of keys and endpoints from Microsoft Azure

key1 = "key"
endpoint1 = "endpoint" # without the slash at the end ;)

# endpoint2 = "https://uksouth.api.cognitive.microsoft.com/sts/v1.0/issuetoken"
 

def from_mic():
    speech_config = speechsdk.SpeechConfig(subscription="key", region="region")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
    print("Talk now mate")
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)
    
    return result.text
    
text = from_mic()



#  creation of Azure client in code 

def authenticate_client():
    ta_credential = AzureKeyCredential(key1)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint1, 
            credential=ta_credential) 
    return text_analytics_client

client = authenticate_client()


# sentiment analysis

def sentiment_analysis_example(client):

    documents = [text]
    response = client.analyze_sentiment(documents = documents)[0]
    print("Document Sentiment: {}".format(response.sentiment))
    print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
        response.confidence_scores.positive,
        response.confidence_scores.neutral,
        response.confidence_scores.negative,
    ))
    for idx, sentence in enumerate(response.sentences):
        print("Sentence: {}".format(sentence.text))
        print("Sentence {} sentiment: {}".format(idx+1, sentence.sentiment))
        print("Sentence score:\nPositive={0:.2f}\nNeutral={1:.2f}\nNegative={2:.2f}\n".format(
            sentence.confidence_scores.positive,
            sentence.confidence_scores.neutral,
            sentence.confidence_scores.negative,
        ))
          


# key meaning of phrase

def key_phrase_extraction_example(client):

    try:
        documents = [text]

        response = client.extract_key_phrases(documents = documents)[0]

        if not response.is_error:
            print("\tKey Phrases:")
            for phrase in response.key_phrases:
                print("\t\t", phrase)
        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))
        


# create funciton that calls mic and voice recognition 
def mic():
    text = from_mic()


# create main funciton that executes everything 

def main():

    # split up text to separate words

    tokenized_word=word_tokenize(text)


    # execute Azure functions 

    sentiment_analysis_example(client)

    key_phrase_extraction_example(client)


    # execute NLTK 

    fdist = FreqDist(tokenized_word)    
    print(fdist)

    print(fdist.most_common(2)) # most common words (or words, change number in brackets)


    # execute matplot (data visualization)

    fdist.plot(30,cumulative=False)
    plt.show()



# create class for gui 

class Grid(GridLayout):

    def __init__(self, **kwargs):

        super(Grid, self).__init__(**kwargs)


        # create the main grid layout

        self.cols = 2 # make the grid have 2 coloums

        self.add_widget(Label(text="hello"))


        # create second grid layout in the main grid layout

        self.top_grid = GridLayout()
        self.top_grid.cols = 1

        # create a button that executes click() (main function)
        def press(self, instance):
            click()
        self.submitreq = Button(text="Listen to me now!", font_size=72)
        self.submitreq.bind(on_press=click())
        self.top_grid.add_widget(self.submitreq)




# create class that builds "DaApp"

class DaApp(App):
    def build(self):
        return Grid()



# make an accessible library from all of above

if __name__ == '__main__':
    DaApp().run()
