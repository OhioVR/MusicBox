#!/usr/bin/env python3

# Scott's MusicBox
# crossfade_arco.py by Scott Yannitell
# Copyright 2022 Scott Yannitell all rights reserved

from os.path import exists
import librosa
import os
from pydub import AudioSegment
from time import sleep
from random import uniform as randuniform
from instrument_data_and_scales import nuller
from instrument_data_and_scales import notes
from instrument_data_and_scales import chromatic_scale
from instrument_data_and_scales import compression_setting

import json
import sys
import KEYS


os.system("rm -rf samples/Philharmonia_extended/"+nuller)


shorts = ["violin", "viola", "cello", "double-bass"]
longs = ["violin", "viola", "cello"]

ignore = ["phrase", "ponticello", "tenuto", "legato", "detache", "-col-legno-battuto", "phrase", "non-vibrato", "harmonic", "tratto", "snap", "trill", "glissando", "staccato", "pizz"]

# Reading a JSON file
def read_json(file):
    with open(file, 'r') as f:
        result = json.load(f)
    return result

metadata = read_json("db/Philharmonia_healed.json")

def commando(command, item,allow_fail=False):
    global nuller

    if item != None:
        print(str(item)+" "+command)
        pass

    else:
        pass
        #print(command)

    result = os.system(command+nuller)
    if result != 0 and not allow_fail:
        os.system(command)
        print("failed with exit code: "+str(result))
        return False
    sleep(0.033/16.0)
    return True


# I'm not sure why I left this here. I set all the
# filtering to be in the sample-filter script
def trim_func(input_file, output_file, plucked=False):
    fade_duration = 1.0/48

    if "pian" in output_file:
        file_duration = librosa.get_duration(filename=input_file)
        sox = "sox "+input_file+compression_setting+output_file+" highpass 90 fade 0 "+str(file_duration-fade_duration)+" "+str(fade_duration)
        #print(sox)
        os.system(sox)
        return
    else:
        file_duration = librosa.get_duration(filename=input_file)
        os.system("sox "+input_file+compression_setting+output_file+" fade 0 "+str(file_duration-fade_duration)+" "+str(fade_duration))
        return



original_notes = 0
new_notes      = 0
def generate_shorts():
    global original_notes, new_notes
    for note in notes:
        for instrument in shorts:
            os.system("mkdir -p samples/Philharmonia_extended/"+instrument)
            for sample_num in range(0, len(metadata[note][instrument])):
                sample = metadata[note][instrument][sample_num]
                note_length = sample[KEYS.NOTE_LENGTH]
                note_offset = sample[KEYS.SAMPLE_OFFSET]
                note_middle = note_offset + (note_length/2)
                file_length = sample[KEYS.FILE_TRUE_DURATION]
                sample_file = sample[KEYS.SAMPLE]
                file_loudness = sample[KEYS.FILE_LOUDNESS]
                infile      = "samples/Philharmonia_healed/"+instrument+"/"+sample_file

                original_notes+=1
                if "crescendo" in sample_file: continue
                if instrument not in shorts:
                    continue

                # We have already popfaded the file and filtered it,
                # so if it is not to be extended, just continue now that it has been copied
                ignored = False
                for item in ignore:
                   if item in sample_file:
                       ignored = True
                       break

                if "normal" not in sample_file: ignored = True
                if ignored: continue

                # if the note is plucked, then move along
                if note_length == 0: continue

                # create a normalized version of the file for processing
                normalized = "/tmp/crossfade_normalized.wav"
                commando("sox --norm "+infile+" "+normalized, instrument)

                chunk_size            = 0.3
                stepsize = int(note_length / 0.125)

                for i in range(2,stepsize+2):
                    print("i", i)
                    output = "samples/Philharmonia_extended/"+instrument+"/"+sample_file.replace(".mp3", "")+"-c-"+str(i-1)+".mp3"
                    midpointA      = note_offset+(note_length/i)
                    midpointB      = (note_length - midpointA)
                    midpointB_fade = (file_length - midpointB)*.8
                    crossfade_len  = note_length*0.95/i
                    print("A", "note_offset", note_offset, "note_length", note_length, "midpointA", midpointA, "midpointB", midpointB, "crossfade_len", crossfade_len  )

                    if not commando("sox "+normalized+" /tmp/crossfade_begin.wav trim "+str(0)+" "+str(midpointA),instrument): continue
                    file_size = os.path.getsize("/tmp/crossfade_begin.wav")
                    if file_size < 26988: continue

                    print("B")
                    if not commando("sox "+normalized+" /tmp/crossfade_end1.wav trim "+str(midpointB)+" -0",instrument): continue
                    if not commando("sox /tmp/crossfade_end1.wav /tmp/crossfade_end.wav fade 0 "+str(midpointB_fade)+ " " + str(midpointB_fade), instrument): quit()
                    file_size = os.path.getsize("/tmp/crossfade_end.wav")
                    if file_size < 26988: continue

                    print("C")
                    crossfade_command = "ffmpeg -i /tmp/crossfade_begin.wav -i /tmp/crossfade_end.wav -filter_complex acrossfade=d="+str(crossfade_len)+" /tmp/crossfade_before_loud.wav -y"
                    commando(crossfade_command, instrument)

                    file_size = os.path.getsize("/tmp/crossfade_before_loud.wav")
                    if file_size < 26988: continue

                    os.system("sox --norm /tmp/crossfade_before_loud.wav /tmp/crossfade_normedagain.wav")

                    file_size = os.path.getsize("/tmp/crossfade_normedagain.wav")
                    if file_size < 26988: continue

                    print("E")
                    amplification = (file_loudness / 2**15)
                    commando("sox -v "+str(amplification)+" /tmp/crossfade_normedagain.wav "+output, instrument) # band reject helps remove a thumping sound
                    print(output)
                    if not exists(output): quit()
                    new_notes+=1

                print()

def generate_longs():
    global original_notes, new_notes
    for note in notes:
        for instrument in longs:
            os.system("mkdir -p samples/Philharmonia_extended/"+instrument)
            for sample_num in range(0, len(metadata[note][instrument])):
                sample          = metadata[note][instrument][sample_num]
                note_length     = sample[KEYS.NOTE_LENGTH]
                note_offset     = sample[KEYS.SAMPLE_OFFSET]
                note_middle_min = sample[KEYS.MIDDLE_MIN_OFFSET]
                note_middle_max = sample[KEYS.MIDDLE_MAX_OFFSET]

                mid_time        = note_middle_max - note_middle_min
                note_middle = note_offset + (note_length/2)
                file_length = sample[KEYS.FILE_TRUE_DURATION]
                sample_file = sample[KEYS.SAMPLE]
                file_loudness = sample[KEYS.FILE_LOUDNESS]
                infile      = "samples/Philharmonia_healed/"+instrument+"/"+sample_file
                max_to_end      = file_length - note_middle_max
                original_notes+=1
                if "crescendo" in sample_file: continue
                if instrument not in longs:
                    continue

                # We have already popfaded the file and filtered it,
                # so if it is not to be extended, just continue now that it has been copied
                ignored = False
                for item in ignore:
                   if item in sample_file:
                       ignored = True
                       break

                if "normal" not in sample_file: ignored = True
                if ignored: continue

                # if the note is plucked, then move along
                if note_length == 0: continue

                # create a normalized version of the file for processing
                basefile = "/tmp/base-file.wav"
                commando("sox "+infile+" "+basefile, instrument)


                midsection = "/tmp/midsection.wav"
                sox_command = "sox "+basefile+" "+midsection+" trim "+str(note_middle_min)+" "+str(mid_time)
                os.system(sox_command)

                start_section = "/tmp/front.wav"
                sox_command = "sox "+basefile+" "+start_section+" trim "+str(0)+" "+str(note_middle_min)
                os.system(sox_command)

                end_section = "/tmp/end_section.wav"
                sox_command = "sox "+basefile+" "+end_section+" trim "+str(note_middle_max)+" "+str(max_to_end)
                os.system(sox_command)

                ###################
                # lengthen by one #
                ###################
                crossfade_len  = note_length*.65
                midsection_blend = "/tmp/midsection_together.wav"
                crossfade_command = "bin/ffmpeg/./ffmpeg -i "+midsection+" -i "+midsection+" -filter_complex acrossfade=d="+str(crossfade_len)+" "+midsection_blend+" -y"
                commando(crossfade_command, instrument)
                output = "samples/Philharmonia_extended/"+instrument+"/"+sample_file.replace(".mp3", "")+"-cl1.mp3"
                os.system("sox "+start_section + " " + midsection_blend + " " + end_section +" "+ output)

                file_size = os.path.getsize(output)
                if file_size < 13000: os.system("rm "+output)
                ###################
                # lengthen by two #
                ###################
                midsection_blend2 = "/tmp/midsection_together2.wav"
                crossfade_command = "bin/ffmpeg/./ffmpeg -i "+midsection_blend+" -i "+midsection_blend+" -filter_complex acrossfade=d="+str(crossfade_len)+" "+midsection_blend2+" -y"
                commando(crossfade_command, instrument)

                output = "samples/Philharmonia_extended/"+instrument+"/"+sample_file.replace(".mp3", "")+"-cl2.mp3"
                os.system("sox "+start_section + " " + midsection_blend2 + " " + end_section + " " +output)
                file_size = os.path.getsize(output)
                if file_size < 13000: os.system("rm "+output)
                #####################
                # lengthen by three #
                #####################
                midsection_blend3 = "/tmp/midsection_together3.wav"
                crossfade_command = "bin/ffmpeg/./ffmpeg -i "+midsection_blend2+" -i "+midsection+" -filter_complex acrossfade=d="+str(crossfade_len)+" "+midsection_blend3+" -y"
                commando(crossfade_command, instrument)

                output = "samples/Philharmonia_extended/"+instrument+"/"+sample_file.replace(".mp3", "")+"-cl3.mp3"
                os.system("sox "+start_section + " " + midsection_blend3 + " " + end_section +" "+ output)
                file_size = os.path.getsize(output)
                if file_size < 13000: os.system("rm "+output)
                #####################
                # lengthen by four #
                #####################
                midsection_blend4 = "/tmp/midsection_together4.wav"
                crossfade_command = "bin/ffmpeg/./ffmpeg -i "+midsection_blend2+" -i "+midsection_blend2+" -filter_complex acrossfade=d="+str(crossfade_len)+" "+midsection_blend4+" -y"
                commando(crossfade_command, instrument)

                output = "samples/Philharmonia_extended/"+instrument+"/"+sample_file.replace(".mp3", "")+"-cl4.mp3"
                os.system("sox "+start_section + " " + midsection_blend4 + " " + end_section +" "+ output)
                file_size = os.path.getsize(output)
                if file_size < 13000: os.system("rm "+output)

                print(output)
                new_notes+=1
                print()

generate_longs()
generate_shorts()
print("originally there were ",original_notes, "notes. now there are ", new_notes+original_notes)
