#!/bin/bash
set -e # exit above 0

# MusicBox - Build-Philhartronia-temp.sh
# copyright 2022 Scott Yannitell

# Build-Philhartronia-temp.sh
# this is a bad script that I needed to throw together to get
# musicbox to run on my laptop.
# now that I no longer use a desktop, this laptop is not 
# powerful enough to run ubuntu anymore
# So I use peppermint which is based on debian.
# unfortunately the automatic builder is broken so I used this
# derived script to help me install it on there.
# So if there is still no interest in this software 
# I won't be breaking a sweat perfecting a peppermint installer

# you need to run this at least once before you can use the
# SIPR engine aka Philhartronia Synthesizer to record your
# midi files into wavs.

# You can safely run this script any number of times without
# having to redownload and compile the samples or ffmpeg.
# The whole script takes at least an hour to finish perhaps
# two on a desktop. On a raspberry pi it could take a day.


    sudo apt install \
        curl pypy3-dev sox libsox-fmt-all rubberband-cli python3-pip ffmpeg -y

    # mido is what makes midi work in MusicBox
    # audioread is needed by pypy scripts that
    # can't use librosa
    # numpy is a dependancy of audioread IIRC
    pypy3 -mpip install audioread numpy mido
    pip3 install librosa pydub

    #############################################
    # custom ffmpeg required build dependancies #
    #############################################
    sudo apt-get install git make nasm pkg-config libx264-dev libxext-dev libxfixes-dev zlib1g-dev librubberband-dev rubberband-ladspa  -y




mkdir -p bin/ffmpeg
    # if git sees the folder is not empty it will not download
    # and compile
git clone https://git.ffmpeg.org/ffmpeg.git bin/ffmpeg && {
        cd bin/ffmpeg
        ./configure --enable-nonfree --enable-gpl --enable-libx264 --enable-zlib --enable-librubberband

    make
}







