AzureCup project 2021 - speech recognition and subsequent speech check. 

# In Git Bash...
To run this, create a new folder for kivy.

  $ mkdir /c/kivy

Then access it through terminal by

  $ cd /c/kivy/

(Result: abc@xyz MINGW64 /c/kivy)

Then we active virtual enviroment.

  $ source virt/Scripts/activate

(virt) should appear above

Then save Python file with copypasted code as SC_main.py into kivy folder and run it by

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




