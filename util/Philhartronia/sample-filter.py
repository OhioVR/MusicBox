#!/usr/bin/env python3

# Scott's MusicBox
# sample-filter.py by Scott Yannitell
# Copyright 2022 Scott Yannitell all rights reserved


import os
from pydub import AudioSegment
import audioread
def get_sound_length(filename):
    with audioread.audio_open(filename) as f:
        return f.duration

from os.path import exists
import copy
from instrument_data_and_scales import notes
from instrument_data_and_scales import nuller
from instrument_data_and_scales import chromatic_scale
from instrument_data_and_scales import ranges
from instrument_data_and_scales import instruments
from instrument_data_and_scales import major_scale
from instrument_data_and_scales import pentatonic_scale
from instrument_data_and_scales import inter_semitone_ratio
from instrument_data_and_scales import the_8ths_relationship
from instrument_data_and_scales import the_4ths_relationship
from instrument_data_and_scales import wav_setting
from instrument_data_and_scales import compression_setting

import warnings
# suppress this useless warning:
# UserWarning: PySoundFile failed. Trying audioread instead.
warnings.filterwarnings('ignore')

source = "samples/Philharmonia_healed/"
dest = "samples/Philharmonia_healed/"


# the trim function trims complete silence from the file and applies a tiny cross fade at the end of it
# we only need to fade out the end I think

def filter_function(input_file, output_file, note_index):
    print(output_file)
    fade_duration = 1.0/15.0
    
    os.system("rm    /tmp/trimmed.wav")
    os.system("touch /tmp/trimmed.wav")

    # the attacks on so many notes have a fuzz before the strike and a big high pass filter
    # takes care of them all. It is only neccessary to make the highpass filetr on a sliding
    # scale
    lowest = notes.index(ranges["philhatronia"]["min"])
    highest = notes.index(ranges["philhatronia"]["max"])
    the_range = highest - lowest
    the_limit =   note_index - lowest
    the_percent = float(the_limit) / float(the_range)
    the_most_filter = 300
    highpass = str((the_most_filter * the_percent)+60)
    print("input_file",input_file, "output_file", output_file, "note_index", note_index, "lowest", lowest, "highest", highest,"the_range",the_range,"the_limit", the_limit,"the_most_filter", the_most_filter,"highpass", highpass)
    # the crossfade at the start and end is to help eliminate popping noises that sometimes
    # get blended in to the recordings.
    file_duration = get_sound_length(input_file)

    sox = "sox "+input_file+" "+compression_setting+output_file+" highpass "+highpass+" fade 0 "+str(file_duration-fade_duration)+" "+str(fade_duration)

    if os.system(sox) != 0:
        print("sample-filter.py: failed with file "+output_file)
        quit(1)

    return

for folder in instruments:
    fullsource = source+folder+"/"
    finaldest  = dest+folder+"/"
    os.system("mkdir -p "+finaldest)
    ##############################################################################
    ## go up the scale                                                           #
    ## find files with a note on the scale                                       #
    ## make decisions: do we do shifts only down, only up, or somewhere between? #
    ##############################################################################
    for scale_note_index in range(len(notes)-1, -1, -1):
        scale_note = notes[scale_note_index]
        for file in os.listdir(fullsource):
            if scale_note in file:
                if os.path.getsize(fullsource+file) < 100: continue # I found a viola sample with zero bytes

                final_file = finaldest+file

                has_loudness = False
                for loudness in ["fortissimo", "forte", "mezzo-forte","mezzo-piano", "piano", "pianissimo"]:
                    if loudness in file:
                        has_loudness = True
                if not has_loudness: continue


                source_file   = fullsource+file
                file_duration = get_sound_length(source_file)
                if file_duration > 60: continue # one minute note max
                os.system("sox -v 0.96 "+source_file+wav_setting+" /tmp/volume-reduced.wav")
                os.system("rm "+final_file) # prevent sox from becoming upset
                filter_function("/tmp/volume-reduced.wav", final_file, scale_note_index)
                # if the file is too quiet then remove it


