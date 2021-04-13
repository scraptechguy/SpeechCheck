from speech_recognition import Microphone, Recognizer 


rec = Recognizer()
mic = Microphone()

with mic:
    rec.adjust_for_ambient_noise(mic, duration=5)

    print("Talk now mate")
    speech = rec.record(mic, 3)


try:
    script = rec.recognize_google(speech)
    print("You said: ", script)        

except:
    print("Sorry, inaudible. :(")
