#!/usr/bin/env pypy3

# Scott's MusicBox'
# database_builder.py by Scott Yannitell
# Copyright 2022 Scott Yannitell all rights reserved

# the product of this script is used by get_sample.py

# the product is a dictionary with the first round of keys being the notes
# like 0,1,2,3,4,,
# with an instrument in each object like this:
# metadata[notes.index("E6")]["violin"]
# metadata[88]["violin"]
# in that address is a list for every sample we have of the violin playing
# on the G4 note. That includes different intensities, lengths, or styles
# searching for styles is simple keyword matching in python by get_sample.py

# get_sample.py simply loops through a few hundred samples and picks out the
# best native one to be stretched, placed, and volume adjusted by recorder.py


import os
import sys
from time import time
from time import sleep
from random import uniform as randuniform
from random import randrange
from operator import itemgetter
import audioread
import wave
import numpy
start = time()

from instrument_data_and_scales import notes
from instrument_data_and_scales import chromatic_scale
from instrument_data_and_scales import ranges
from instrument_data_and_scales import instruments
from instrument_data_and_scales import nuller

samples_dir=sys.argv[1] # its usually either Philharmonia_healed or Philhartronia

import json
import sys
import KEYS
only_process_end = True

metadata = {}

def get_sound_length(filename):
    with audioread.audio_open(filename) as f:
        return f.duration

def get_sound_length(filename):
    with audioread.audio_open(filename) as f:
        return f.duration

# https://janakiev.com/blog/python-pickle-json/
# Writing a JSON file
def write_json(data, file):
    with open(file, 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4)

# Reading a JSON file
def read_json(file):
    with open(file, 'r') as f:
        result = json.load(f)
    return result

# find usable inflections and instruments
pluckers = ["pizz", "banjo", "guitar"]
absolute_loud = 32768



# https://stackoverflow.com/questions/44222651/converting-16-bit-integer-into-0-100
# yes apparently there are people as stupid as I am....
def aud_to_mid_loud(loudness):
    return int(loudness / (absolute_loud * 1 / 128.0))

def get_adj_volume(target_bit15, minbit15, maxbit15):
    range_loud   = maxbit15 - minbit15
    ranger_ratio = absolute_loud / maxbit15
    adjusted_loud = target_bit15 * ranger_ratio
    return adjusted_loud



for i in range(0,len(notes)):
    metadata[notes[i]] = {}
    for ii in range(0,len(instruments)):
        metadata[notes[i]][instruments[ii]] = []

# https://stackoverflow.com/a/62298670
def get_sound_amplitude(filename):
    os.system("sox "+filename+" /tmp/amplitudetest.wav")
    # Read file to get buffer
    ifile = wave.open("/tmp/amplitudetest.wav")
    samples = ifile.getnframes()
    audio = ifile.readframes(samples)

    # Convert buffer to float32 using NumPy
    s = abs(numpy.frombuffer(audio, dtype=numpy.int16))
    maxY = int(max(s))
    return maxY

def collect_metadata():

    counter = 0
    # collect all information concerning the selected instruments and their inflections
    for instrument in instruments:
        folder="samples/"+samples_dir+"/"+instrument+"/"

        files = os.listdir(folder)
        for file in files:
            sample = file
            plucked = False
            for plucker in pluckers:
                if plucker in file:
                    plucked = True

            if instrument == "banjo" or instrument == "guitar":
                plucked = True

            if instrument == "mandolin" and "tremolo" not in sample:
                plucked = True

            #########################################################
            # first find note offset time by using sox to trim the  #
            # silence at the beginning, then subtract the length of #
            # the original minus the length of the trimmed to get   #
            # the offset value. #####################################
            #####################

            # the file is normalized to treat them more consistantly
            sox_command = "sox --norm "+folder+file+" /tmp/tmp-norm.wav"
            os.system(sox_command+nuller)

            # total length of file
            file_true_duration =  get_sound_length("/tmp/tmp-norm.wav")

            # "threshold"
            # generally speaking, the lowest this number the better
            # because this defines exactly when the sample should line up
            # with the note in the offset.
            # I made it a string because strings are cool too.

            if instrument != "banjo":
                start_threshold = "1.5%"
            else:
                start_threshold = "3%"

            # cut off the part of silence up until the note sounds
            sox_command = "sox /tmp/tmp-norm.wav /tmp/tmp-start-trim.wav silence 1 0.01 "+start_threshold
            os.system(sox_command)

            # then do the math to find the offset
            sample_offset  = file_true_duration - get_sound_length("/tmp/tmp-start-trim.wav")

            # do the process in reverse to find when the note ends
            sox_command = "sox /tmp/tmp-start-trim.wav /tmp/start-trim-reverse.wav reverse"
            os.system(sox_command)


            end_threshold = "1.5%"

            sox_command = "sox /tmp/start-trim-reverse.wav /tmp/end-trim.wav silence 1 0.01 "+end_threshold
            os.system(sox_command)

            note_length =  get_sound_length("/tmp/end-trim.wav")

            # really short notes messes up the recorder.py script
            if note_length < 0.09:
                if samples_dir == "Philhartronia":
                    os.system("rm "+folder+file)
                continue

            # sample_offset and note_length are now obtained

            # arco cross fade helper stuff
            if samples_dir == "Philharmonia_healed" and instrument in ["violin", "viola", "cello", "double-bass"]:
                sox_command = "sox /tmp/tmp-norm.wav /tmp/tmp-start-trim2.wav silence 1 0.1 25%"
                os.system(sox_command)

                middle_min_offset  = file_true_duration - get_sound_length("/tmp/tmp-start-trim2.wav")

                sox_command = "sox /tmp/tmp-start-trim2.wav /tmp/start-trim2-reverse.wav reverse"
                os.system(sox_command)

                sox_command = "sox /tmp/start-trim2-reverse.wav /tmp/tmp-start-trim2.wav silence 1 0.1 45%"
                os.system(sox_command)

                middle_max_offset = file_true_duration - get_sound_length("/tmp/tmp-start-trim2.wav")
                file_loudness       = get_sound_amplitude(folder+file)

                # the middle_min_offset finds where the sound is 25% loud from the start
                # and the middle_max_offset finds where teh sound is 25% loud to the start
            else:
                middle_min_offset = 0
                middle_max_offset = 0
                file_loudness = 0

            if plucked:
                note_length = 0

            # these four lines have no meaning, but they must be kept
            ranger_max_loudness = 'none'
            ranger_min_loudness = 'none'
            midi_loudness       = 'none'
            length_key = None

            loudness_id = 0
            loudness_name = ""
            if "fortissimo" in sample:
                loudness_id = int(6/7*128.0)
                loudness_name = "fortissimo"
            elif "forte" in sample:
                loudness_id = int(5/7*128.0)
                loudness_name = "forte"
            elif "mezzo-forte" in sample:
                loudness_id = int(4/7*128.0)
                loudness_name = "mezzo-forte"
            elif "mezzo-piano" in sample or "forte-mute" in sample:
                loudness_id = int(3/7*128.0)
                loudness_name = "mezzo-piano"
            elif "_piano" in sample:
                loudness_id = int(2/7*128.0)
                loudness_name = "piano"
            elif "pianissimo" in sample:
                loudness_id = int(1/7*128.0)
                loudness_name = "pianissimo"
            note_relative_loud = 128

            for i in range(0,len(notes)):
                if notes[i] in file:
                    note_index = i
                    note_name  = notes[i]
                    #write data
                    # there is a better way than this mess
                    print("\n\n\nnote_index\n",note_index, "\n\nnote_name\n", note_name, "\n\ninstrument\n", instrument,"\n\nnote_length\n", note_length, "\n\nfile_loudness\n", file_loudness, "\n\nfile_true_duration\n",file_true_duration,"\n\nsample_offset\n",sample_offset, "\n\nmiddle_min_offset\n", middle_min_offset, "\n\nmiddle_max_offset\n", middle_max_offset, "\n\nplucked\n",plucked, "\n\nranger_max_loudness\n", ranger_max_loudness, "\n\nranger_min_loudness\n", ranger_min_loudness, "\n\nmidi_loudness\n", midi_loudness, "\n\nsample\n", sample, "\n\nlength_key\n",length_key, "\n\nloudness_id\n", loudness_id, "\n\nloudness_name")

                    result = [note_index, note_name, instrument, note_length, file_loudness, file_true_duration, sample_offset, middle_min_offset, middle_max_offset, plucked, ranger_max_loudness, ranger_min_loudness, midi_loudness, sample, loudness_id,loudness_name,note_relative_loud ]

                    metadata[notes[i]][instrument].append(result)
                    counter+=1
                    print("\n\n\n"+str(counter)+"\n\n")

    write_json(metadata, "db/"+samples_dir+"-unsorted.json")
    return(counter)

def sort_metadata():
    metadata = read_json("db/"+samples_dir+"-unsorted.json")
    for note in notes:
        for instrument in instruments:
            metadata[note][instrument].sort(key=lambda row: (-row[KEYS.NOTE_LENGTH], -row[KEYS.LOUDNESS_ID]))

    write_json(metadata, "db/"+samples_dir+".json")

number_of_samples = collect_metadata()

sort_metadata()
os.system("rm db/"+samples_dir+"-unsorted.json")

print("processed ",number_of_samples, " in ", time()-start, " seconds")
