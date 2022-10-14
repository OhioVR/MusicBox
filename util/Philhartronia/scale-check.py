#!/usr/bin/env python3

# Scott's MusicBox
# scale-check.py by Scott Yannitell
# Copyright 2022 Scott Yannitell all rights reserved

from os.path import exists
import os
import sys
from time import sleep
from instrument_data_and_scales import notes
from instrument_data_and_scales import chromatic_scale
from instrument_data_and_scales import ranges
from instrument_data_and_scales import instruments
from instrument_data_and_scales import nuller
from instrument_data_and_scales import chromatic_progression
from instrument_data_and_scales import pentatonic_scale
from instrument_data_and_scales import major_scale
from instrument_data_and_scales import minor_scale
import audioread
from threading import Timer

# scale-check.py is my best solution for listening to samples grouped together
# along a chromatic scale and identifying the ones that stick out. If something
# sounds amiss I can press a key and enter to break down the group to one sample
# at a time to find the one that seems at the wrong pitch or otherwise has
# an unpleasant sound. Then by entering an any key that sample is added to the
# scale-check-results.dat file which is used by the heal-Philharmonia-script
# to replace the samples that were removed with pitch shifted copies of it's 
# nearest upper neighbor. If an upper neighbor is not found it will shift the 
# nearlest lower neighbor up to it's level.

def get_sound_length(filename):
    with audioread.audio_open(filename) as f:
        return f.duration


print(sys.argv[1], sys.argv[2], sys.argv[3])




scale_check_results_ = open("scale-check-results.dat").read().splitlines()

scale_check_results = []
for i in range(0, len(scale_check_results_)):
    if len(scale_check_results_[i]) > 1:
        scale_check_results.append(scale_check_results_[i].split("-p")[0])



current_scale_note = 0
current_group = []
command = " ".join(sys.argv)

collection = sys.argv[1]
instrument = sys.argv[2]
instrument_filter = sys.argv[3].split(".mp3")[0]

test_scale = []
shift = 0
min_r = ranges[instrument]["min"]
max_r = ranges[instrument]["min"]
first_c = notes.index(ranges[instrument]["1st_C"])


for octave in range(0,10):
    for note in major_scale:
        new_note = note+(octave*12)
        if new_note >= first_c:
            test_scale.append(new_note)
        


exclusive = []
for note_index in test_scale:
    for file in os.listdir("samples/"+collection+"/"+instrument):
        if instrument_filter not in file:
            continue
        if "-c" in file:
            continue
        try:
            if notes[note_index] in file:
                current_group.append(file)
        except:
            print("no")
            pass
    sox_play_group = ""
    
    files_found = []
    for file in current_group:
        sox_play_group += "samples/"+collection+"/"+instrument+"/"+file
        files_found.append(file)
    if len(sox_play_group) > 0:
        
        play_command = "play -m "+sox_play_group
        print(notes[note_index])
        for file in current_group:
            do_print = True
            for item in scale_check_results:
                if item in file:
                    do_print = False
            if do_print:
                print(file)
            else:
                print("-X-: ", file)
        if len(files_found) > 1:
            os.system(play_command+nuller+" & ")
        else:
            os.system("play "+sox_play_group+nuller+" &")
        totaltime = get_sound_length(sox_play_group.split()[0])
        
        sleep(totaltime/3)
        os.system("killall play")
        sleep(0.25)
            
    exclusive = []    
    current_group = []

# comment out the scriptline it came from
recheck_script = open("recheck.sh", "r").read()
file1 = open("recheck.sh", "w")
oldline = "./"+sys.argv[1]+" "+sys.argv[2]+" "+sys.argv[3]
newline = "#"+oldline
file1.write(recheck_script.replace(oldline,newline))
file1.close()
