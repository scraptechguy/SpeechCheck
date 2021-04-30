# AzureCup 2021 project - speech recognition and subsequent speech check

## The main code is in SC_main.py file 

All links you might need are in the Links file. Issues I encountered on the way are in the IssuesIEncountered file. :)

# Required Libraries: 

PyAudio ($ pip install pyaudio)

NLTK ($ pip install nltk)

Kivy ($ pip install kivy)

Azure Text Analytics ($ pip install azure-ai-textanalytics)

Azure Speech Services ($ pip install azure-cognitiveservices-speech)

*commands without brackets

# In Git Bash...
To run this, create a new folder for kivy.

  $ mkdir /c/kivy

Then access the directory through terminal by

  $ cd /c/kivy/

(Result: abc@xyz MINGW64 /c/kivy)

Then activate virtual enviroment for that directory.

  $ source virt/Scripts/activate

(virt) should appear above

Then save Python file with copy pasted code as SC_main.py into the kivy folder and run it by

  $ python SC_main.py
  

# When error [CRITICAL] Unable to *something* occures:
(Python and pip needs to be preinstalled)

You either haven't installed kivy yet. To fix that run 

  $ python -m pip install kivy

Or haven't activated virtual enviroment. Run

  $ cd /c/kivy/

  $ source virt/Scripts/activate


If still having trouble, try running 

  $ python pip uninstall kivy

  $ python pip install kivy

  $ python pip install docutils pygments pypiwin32 kivy.deps.sdl2

  $ pythoon pip install kivy.deps.glew




