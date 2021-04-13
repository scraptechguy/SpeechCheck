from speech_recognition import Microphone, Recognizer 


recog = Recognizer()
mic = Microphone()

with mic:
    recog.adjust_for_ambient_noise(mic, duration=5)

    print("Talk")
    audio = recog.record(mic, 3)


try:
    recognized = recog.recognize_google(audio)
    print("you said: ", recognized)        

except:
    print("Sorry, inaudible. :(")
