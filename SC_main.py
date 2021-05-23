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


# input of keys and endpoints from Microsoft Azure

key1 = "d7861716f1714640b4049fd55d038cab"
endpoint1 = "https://textana007.cognitiveservices.azure.com" # without the slash at the end ;)

# endpoint2 = "https://uksouth.api.cognitive.microsoft.com/sts/v1.0/issuetoken"




# call mic and execute voice recognition 

def from_mic():
    speech_config = speechsdk.SpeechConfig(subscription="49b58a88a23b4026bd5dd389b68eda84", region="uksouth")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    result = speech_recognizer.recognize_once_async().get()
    
    return result.text



# authenticate client on Azure

def authenticate_client():
    ta_credential = AzureKeyCredential(key1)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint1, 
            credential=ta_credential) 
    return text_analytics_client

client = authenticate_client()



# analyze sentiment

def sentiment_analysis_example(client):

    global doc_sentiment
    global overall_scores

    documents = [text]
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

        documents = [text]

        response = client.extract_key_phrases(documents = documents)[0]

        if not response.is_error:
            
            for phrase in response.key_phrases:

                keyphr = "\t\t {}".format(phrase)
                return keyphr

        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))


