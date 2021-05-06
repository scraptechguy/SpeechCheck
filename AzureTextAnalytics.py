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


# and finally import of kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


# input of keys and endpoints from Microsoft Azure

key1 = "46f6aa6b2b304571a4c0c8f701b467e2"
endpoint1 = "https://textanalytics007.cognitiveservices.azure.com" # without the slash at the end ;)

# endpoint2 = "https://uksouth.api.cognitive.microsoft.com/sts/v1.0/issuetoken"


def from_mic():
    speech_config = speechsdk.SpeechConfig(subscription="3d0bcba6fb344b02a714d31e9f65faa2", region="uksouth")
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

