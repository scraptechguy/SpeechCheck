from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords


from speech_recognition import Microphone, Recognizer 



rec = Recognizer()
mic = Microphone()

with mic:
    rec.adjust_for_ambient_noise(mic, duration=0)

    print("Talk now mate")
    audio = rec.record(mic, 10)


try:
    text = rec.recognize_google(audio)
    print("You said: ", text)        

except:
    print("Sorry, inaudible. :(")



