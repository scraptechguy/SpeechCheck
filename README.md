# AzureCup 2021 project - speech recognition and subsequent speech check

All links you might need are in the [Links](https://github.com/scraptechguy/SpeechCheck/blob/main/Links.txt) file. Issues I encountered on the way are in the [corresponding file](https://github.com/scraptechguy/IssuesIEncoutered/blob/main/AzureSpeechToText) in the [IssuesEncountered](https://github.com/scraptechguy/IssuesIEncoutered/) repo. :)

+ To run this yourself, review <a href="https://github.com/scraptechguy/SpeechCheck/blob/main/requirements.md" target="_blank">requirements.md</a> file and do the following in terminal: 

```sh
cd <path of the project on your computer>
```

```sh
pip install -r requirements.txt
python main.py
```
+ Note: Don't forget to input valid key, endpoint and region! (Only works with Microsoft Azure)

# In Git Bash...
To run this, create a new folder.
```sh
  $ mkdir /c/kivy
```
Then access the directory through terminal by
```sh
  $ cd /c/kivy/
```
(Result: abc@xyz MINGW64 /c/kivy)

Download all required libraries. (above)

Create and activate virtual enviroment for that directory.
```sh
  $ python -m venv virt

  $ source virt/Scripts/activate
```
(virt) should appear above

Then save Python file with copy pasted code as SC_main.py into the kivy folder and run it by
```sh
  $ python SC_main.py
```

# When error [CRITICAL] Unable to *something* occures:
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




