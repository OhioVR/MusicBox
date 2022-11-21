Welcome to Scott's MusicBox

To get started download the repo and go into the folder util/Philhartronia/

In that folder is a file called Build-Philharmonia.sh which will install all dependencies and download ffmpeg and compile it along with all the required processing. The script takes about 2 hours to finish depending on how fast your CPU core is. I advise you to read the script first to see if anything looks like it would conflict with your system or otherwise install MusicBox in a KDE NEON virtual machine. Or plain Ubuntu should also work.

Then after that is finished without errors you may try "rendering" the example projects. The debut.sh file on the base of MusicBox's folder renders them all at once. That takes about 40 minutes on my Ryzen.

Then after you have a project render proof start making your own chamber orchestra music!

For an example of what it sounds like please visit this link:

https://www.youtube.com/watch?v=EdIQ7aXIECM


ABOUT
A project born of an obsession to see what could be done with the Philharmonia sample collection. I am not a musician by trade or by training I only know some basic music theory from self study.

I've developed this as a simple arranging tool useful for discovery of old classic works that you wish to bring to life with more instruments and timbrel texture.

Arranging music that sounds plausibly realistic was a goal of the project from the first day I discovered the samples.

I developed this as a series of experiments over the course of 6 months until I formulated a stable framework with less than 2400 lines of easy to read python code. It is not made for performing artists like a midi synth. Rather it is a music recording software program. Much like a real musicbox, first the notes have to be hammered, it follows a set of instructions then it renders the music in one shot.

Usually the rendering takes less time than the length of the file and it is possible render single instrument parts if you are just tweaking a part of your composition.

As you use the software you will gain knowledge of what sounds good for an arrangement and what doesn't. Something I've learned include:

Less can be more if more instruments make it sound muddy.
Fast notes sometimes just sound better with a plucked instrument like pizzicato strings, guitar, mandolin or banjo.

You can turn a treble part into a base line by shifting the score an octave for the part, and filtering notes shorter than say, .5 seconds.

It is brain dead easy to get realism with musicbox and usually "good enough" to make a backup track if you were a vocalist or if you are an instrumentalist and you want to hear what a part would be like without the trouble of mastering it first (part of the discovery benefit).



Ok so it isn't as good as I thought. But maybe it would still be fun to play with in realtime with the keyboard-lyre.py script

https://www.youtube.com/watch?v=VPxsbsEu0_s

My next expermiment will be a kind of fundamental music language based on chords, intervals and scales.