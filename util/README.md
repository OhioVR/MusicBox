Get inside the musicbox!

There are a lot of scripts here that will hopefully not be necessary to deeply change but it would help to know what these scripts do. The build process is explained in the file "6 steps to a building the Philhartronia Synth". That covers what is needed to understand the build process. But since this is scripting, you may never need to know or care.

In your command line interface (CLI) copy this code and paste it in, press enter.

cd Philhatronia

./Build-Philhartronia.sh

This will do everything needed to run prepare your system to become a SIPR engine with the scripts in this folder.

You may run this script any time you wish to make a change and it will efficiently rebuild everything without erasing
anything important.

After that script is run all you really need to focus on to make your music are the following 3 files:

arranger.py
midi-file-to-playlist.py
recorder.py

Use a template file from the templates folder to get started with SIPR recording.

As of this time the main restrictions are that the settings file has to be in your base musicbox directory. and you must
avoid spaces in the mid file names and project names. This is due to sox messing up.

If you fix this I will mail you a very nice shiny penny. Brand new one in fact!
