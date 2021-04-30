# import of elements from libraries for Microsoft Text Analytics 

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


# import of elements from libraries for Microsoft Speech Services 

import azure.cognitiveservices.speech as speechsdk


# import of elements from libraries for Natural Language Tool Kit

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


# input of keys and endpoints from Microsoft Azure

key1 = "EnterYourKeyHere"
endpoint1 = "EnterYourEndpointHere" # without the slash at the end ;)

# key2 = "3d0bcba6fb344b02a714d31e9f65faa2" called subscription
# endpoint2 = "https://uksouth.api.cognitive.microsoft.com/sts/v1.0/issuetoken"


# getting speech input from user and converting it to text (rewrite to True loop)

time = input("Enter estimated time of your speech (in seconds): ")

act_time = int(time) + int(time) / 10

print("Recording will end after {} seconds".format(act_time))   

def from_mic():
    speech_config = speechsdk.SpeechConfig(subscription="EnterYourKeyHere", region="EnterYourRegionHere")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    print("Talk now mate")
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)

from_mic()


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

    documents = [result.text]
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
        documents = [result.text]

        response = client.extract_key_phrases(documents = documents)[0]

        if not response.is_error:
            print("\tKey Phrases:")
            for phrase in response.key_phrases:
                print("\t\t", phrase)
        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))
        

# splitting up script to separate words

tokenized_word=word_tokenize(result.text)


# execute Azure functions 

sentiment_analysis_example(client)

key_phrase_extraction_example(client)


# executing NLTK functions 

fdist = FreqDist(tokenized_word)    
print(fdist)

print(fdist.most_common(3)) # most common words (or words, change number in brackets )
