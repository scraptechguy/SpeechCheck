# AzureCup 2021 project - speech recognition and subsequent speech check

All links you might need are in the [Links.md](https://github.com/scraptechguy/SpeechCheck/blob/main/Links.md) file. Issues I encountered on the way are in the [corresponding file](https://github.com/scraptechguy/IssuesEncoutered/blob/main/Windows/HOWTO.md) in the [IssuesEncountered](https://github.com/scraptechguy/IssuesEncoutered/) repo. :)

+ Note: Don't forget to input valid key, endpoint and region! (Only works with Microsoft Azure)

### Table of contents

+ <a href="https://github.com/scraptechguy/SpeechCheck#running-speechcheck-on-windows-10">Running SpeechCheck on Windows 10</a>
+ <a href="https://github.com/scraptechguy/SpeechCheck#critical-unable-to-something">[CRITICAL] unable to something</a>

## Running SpeechCheck on Windows 10

### In Git BASH without cloning the repo 

To run this yourself, review <a href="https://github.com/scraptechguy/SpeechCheck/blob/main/requirements.md" target="_blank">requirements.md</a> file and do the following in terminal: 

```sh
  pip install -r requirements.txt
```

+ Create a directory for SpeechCheck project 

```sh
  $ mkdir /c/speechcheck
```

+ Then access the directory through terminal 

```sh
  $ cd /c/speechcheck/
```
Output: abc@xyz MINGW64 /c/kivy

+ Download all <a href="https://github.com/scraptechguy/SpeechCheck/blob/main/requirements.md" target="_blank">required libraries</a>.

+ Create and activate virtual enviroment for that directory.

```sh
  $ python -m venv virt

  $ source virt/Scripts/activate
```
(virt) should appear above

+ Then save Python file with copy pasted code as main.py into the kivy folder and run it by

```sh
  $ python main.py
```

## [CRITICAL] unable to *something*

(Python and pip needs to be preinstalled)

You either haven't installed kivy yet. To fix that run 

```sh
  $ pip install kivy
```

Or haven't activated virtual enviroment. Run

```sh
  $ cd /c/kivy/
  $ source virt/Scripts/activate
```

If still having trouble, try running 

```sh
  $ pip uninstall kivy

  $ pip install kivy

  $ pip install docutils pygments pypiwin32 kivy.deps.sdl2

  $ pip install kivy.deps.glew
```


## Running SpeechCheck on MacOS


## Understand the code 

+ Import of Azure Cognitive Services API libraries

```py
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import azure.cognitiveservices.speech as speechsdk
```
