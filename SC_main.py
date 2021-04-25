from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

from speech_recognition import Microphone, Recognizer 

rec = Recognizer()
mic = Microphone()

# don't forget to input right key and endpoint. 
key = "key"
endpoint = "endpoint" # without the slash at the end ;)


with mic:
    rec.adjust_for_ambient_noise(mic, duration=1)

    print("Talk now mate")
    speech = rec.record(mic, 10)

try:
    script = rec.recognize_google(speech)        

except:
    print("Sorry, inaudible. :(")


def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential) 
    return text_analytics_client

client = authenticate_client()

def sentiment_analysis_example(client):

    documents = [script]
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
          

def key_phrase_extraction_example(client):

    try:
        documents = [script]

        response = client.extract_key_phrases(documents = documents)[0]

        if not response.is_error:
            print("\tKey Phrases:")
            for phrase in response.key_phrases:
                print("\t\t", phrase)
        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))
        

tokenized_word=word_tokenize(script)

fdist = FreqDist(tokenized_word)



sentiment_analysis_example(client)
key_phrase_extraction_example(client)
print(fdist)
print(fdist.most_common(3))
