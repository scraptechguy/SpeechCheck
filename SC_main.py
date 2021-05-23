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

