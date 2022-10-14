#!/usr/bin/env pypy3

# Scott's Music Box
# arranger.py by Scott Yannitell
# Copyright 2022 all rights reserved

# A settings dictionary containing general settings and instrument specific
# settings along with a source midi file and details on output names is fed 
# into this script from a project file to be processed. The midi file is read
# and notes are filtered according to settings parameters. If notes are within
# an instrument register they can be played. If outside of it, they are ignored.
# But it is setup not to raise an error when this happens so that the notes can
# drift gracefully, if you wish, to other instruments. In this way it is trivial
# to make a simple instrument ensemble from a single track.

# And instrument can use all notes from a composition, or just those found in a 
# midi track or a combination of tracks specified by an array. You can have more
# than the same kind of instrument doing different things in the settings by
# labeling them like this: violin0, violin2, violin3.

# There are some settings that could be used which may indeed have no practical
# application as of yet. But I didn't remove them as they cause no harm to
# workflow when simply avoided or ignored. For example, maximizing dynamics
# like normalizing midi seems to have no pleasent application as of now.
# but why not keep it..

from util import midi_file_to_playlist
from util.Philhartronia import get_sample
import os
from time import sleep
from time import time
from util.recorder import render
from util.recorder import mixdown
from os.path import exists
import audioread
import sys
import copy
import datetime

from util.Philhartronia.instrument_data_and_scales import instruments
from util.Philhartronia.instrument_data_and_scales import nuller
from util.Philhartronia.instrument_data_and_scales import notes

def debug(filename,data):
    file1 = open("diagnostics-logs/"+filename, "a")
    file1.write(str(data)+"\n")
    file1.close()


# the default values are good to reference for your settings
# in most cases you can simply load defaults with an include
# as shown in the template file

defaults = {}
defaults["instruments"] = []
defaults["banned_effects"]                      = ["snap","battuto", "tremolo", "glissando"]
defaults["effect_exceptions"]                   = []
defaults["maximize_dynamics"]                   = False
defaults["key_offset"]                          = 0
defaults["reverberance"]                        = 50
defaults["reverb_room_scale"]                   = 100
defaults["reverb_stereo_depth"]                 = 100
defaults["master_tempo"]                        = 1.0
defaults["master_volume"]                       = 0.8
defaults["round_robin"]                         = 0
defaults["global_velocity"]                     = 1
defaults["expression_multiplier"]               = 1 # set this to a lower value to make get_sample fetch longer samples
for instrument_index in range (0, len(instruments)):
    instrument = instruments[instrument_index]
    defaults[instrument]                        = {}
    defaults[instrument]["octave"]              = 0
    defaults[instrument]["low_pass"]            = -999
    defaults[instrument]["high_pass"]           = 999
    
    defaults[instrument]["length_upperlimit"]   = 999
    defaults[instrument]["length_lowerlimit"]   = 0
    defaults[instrument]["velocity_multiplier"] = 1.0
    if instrument == "violin":
        defaults[instrument]["velocity_multiplier"] = .69
    defaults[instrument]["volume"]              = .5
    defaults[instrument]["polyphony"]           = 1
    defaults[instrument]["note_length_adjust"]  = 1.0
    defaults[instrument]["pizz_threshold"]      = -1
    if instrument == "mandolin":
        defaults[instrument]["pizz_threshold"]  = 999
    #defaults[instrument]["midi_channel"]        = instrument_index
    
for instrument_index in range (0, len(instruments)):
    for i in range(0,10):
        instrument = instruments[instrument_index]+str(i)
        defaults[instrument]                        = {}
        defaults[instrument]["octave"]              = 0
        defaults[instrument]["length_upperlimit"]   = 999
        defaults[instrument]["length_lowerlimit"]   = 0
        defaults[instrument]["velocity_multiplier"] = 1.0
        if instrument == "violin":
            defaults[instrument]["velocity_multiplier"] = .69
        defaults[instrument]["volume"]              = .5
        defaults[instrument]["polyphony"]           = 1
        defaults[instrument]["note_length_adjust"]  = 1.0
        defaults[instrument]["pizz_threshold"]      = -1
        if instrument == "mandolin":
            defaults[instrument]["pizz_threshold"]  = 999
        defaults[instrument]["low_pass"]            = -999
        defaults[instrument]["high_pass"]           = 999
        #defaults[instrument]["midi_channel"]        = instrument_index
    
    
# https://www.pythonpool.com/python-clamp/
def clamp(num, min_value, max_value):
    num = max(min(num, max_value), min_value)
    return num

def get_sound_length(filename):
    with audioread.audio_open(filename) as f:
        return f.duration

def arrange(settings):
    os.system("kill -9 `ps aux | grep ffmpeg | grep -v grep | awk '{print $2}'`")

    try:
        global_velocity = settings["global_velocity"]
    except:
        global_velocity = 1

    try:
        string_offset = settings["strings_overlay_time"]
    except:
        string_offset = 0.07
    start = time()
    os.system("clear")
    
    project_folder="project_outputs/"+settings["project_name"]

    os.system("mkdir -p '"+project_folder+"'")

    slide_show_folder="YouTube/"+settings["project_name"]
    os.system("mkdir -p '"+slide_show_folder+"'")

    
    # get all notes, we'll deal with a copy next
    playlist = midi_file_to_playlist.generate_playlist(settings)
    for item in playlist:
        debug("playlist.txt", item)
    
    
    velocity_ceiling = 128
    try:
        velocity_ceiling = settings["velocity-ceiling"]
    except:
        pass
        
    velocity_floor = 0
    try:
        velocity_floor = settings["velocity-floor"]
    except:
        pass
   
   
    an_octave = 12
    
    if len(sys.argv) > 1:
        the_instruments = sys.argv[1:]
    else:
        os.system("rm diagnostics-logs/*")
        the_instruments = settings["instruments"]
    
    for item in playlist:
        debug("playlist.txt", item)
    
    
    for instrument in the_instruments:
        try:
            low_pass  = settings[instrument]["low_pass"]
        except:
            low_pass = -999
        
        try:
            high_pass = settings[instrument]["high_pass"]
        except:
            high_pass = 999
        track = []
        
        for record_index in range(0,len(playlist)):
            record = playlist[record_index]
            midi_channel     = record[0]
            try:
                instrument_channel = settings[instrument]["midi_channel"] ###+ 1 what is this here for
            except:
                instrument_channel = -1
                
            # allow multiple tracks per instrument
            if type(instrument_channel) is int:
                if instrument_channel >= 0:
                    if instrument_channel != midi_channel:
                        continue
            else:
                if midi_channel not in instrument_channel:
                    continue
            semitone_adjust = 0
            try:
                if settings[instrument]["semitones-off"]:
                    semitone_adjust = settings[instrument]["semitones-off"]
            except:
                pass
            note             = record[1] + settings["key_offset"] + (an_octave * settings[instrument]["octave"]) 
            print("note", note, "record[1]", record[1])
            
            ontime           = record[2]
            length           = record[3]
            # don't let our note filter filter out notes we lengthened or shortened.
            if length >= settings[instrument]["length_upperlimit"]:
                continue
            
            if length <= settings[instrument]["length_lowerlimit"]:
                continue
                
            if note < low_pass: continue
            if note > high_pass: continue
            
            length = length * settings[instrument]["note_length_adjust"]
            if instrument in ["viola", "cello", "violin", "double-bass"]:
                length+=string_offset
            # https://www.shadertoy.com/view/tscGzs
            
            
            polyphony        = settings[instrument]["polyphony"]
            time_polyphony   = record[5]
        
            chorus_list = []
            ###########################
            # allow instrument clones #
            ###########################
            if instrument[-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                instrument_original = copy.copy(instrument[:])
                instrument2         = copy.copy(instrument[0:-1])
            else:
                instrument_original = copy.copy(instrument[:])
                instrument2         = copy.copy(instrument[:])
            
           
            
            if instrument2 == "guitar": length = 0.0
            if instrument2 == "banjo": length = 0.0
            final_polyphony = int(abs(polyphony/time_polyphony))
            if final_polyphony == 0:
                final_polyphony = 1
            velocity         = record[4] * settings[instrument]["velocity_multiplier"] * global_velocity / final_polyphony
            velocity = clamp(velocity, velocity_floor,velocity_ceiling)
            debug("playlist_labels.txt", "midi_channel: " + str(midi_channel) + " note: " + str(note) + " note_name: " + str(notes[note]) + " ontime: " + str(ontime) + " length: " + str(length) + " velocity: " + str(velocity) + " polyphony: " + str(polyphony))
            for i in range(0, final_polyphony):
                print("note from arranger", note)
                sample, offset, note_speed, plucked, search_level, loudness_adjust, true_length = get_sample.get_sample(note, instrument2, velocity, length, settings,instrument_original )
                
                # if no sample, do not cause error
                if sample != None:
                    chorus_list.append([sample, offset,instrument, note_speed, plucked, search_level, loudness_adjust, true_length])
                     
            
            file1 = open("diagnostics-logs/playlist."+instrument+".sh", "a")
            if len(chorus_list) != 0:
                pan_segment = (1/len(instruments))/len(chorus_list)
            else:
                pan_segment = 0
            pan_segment_counter = 0
            strum_offset = 0
            this_time   = ontime
            
            #####################################################
            # a plucked instrument should be strummed on chords #
            #####################################################
            # try avoidance
            if len(chorus_list) > 0: # sometimes nothing gets to this point
                if time_polyphony > 3: # 3+ notes and we can strum. Two are ok plucked
                    # if the instrument is plucked, we can strum it
                    # should there be multpile notes for one beat
                    # I can't do this in any realistic fashion because
                    # I can't predict what kind of polyphony I'll get
                    # So pretend the guitar is not guitar and it is a harp
                    # Or maybe imagine a 12 string guitar that is it is some how
                    # possible to strum a huge veriety of notes
                    strumlist = []
                    if chorus_list[0][4]: # if it is a plucked instrument
                        # make a list of all notes played at this time
                        # and add information about it's note index and 
                        # also a reference to it's identity index
                        
                        for i in range(0, len(playlist)):
                            if playlist[i][2] == this_time:
                                strumlist.append([playlist[i][1], i])
                        
                        # sort the list based on note index and if the note
                        # identity lines up with the one we are playing
                        # figure out from here how much time to shift it 
                        # to make it appear notes are being strummed
                        # from low notes to high notes
                        strumlist.sort(key=lambda row: (row[0]), reverse=False)
                        for strum_index in range(0,len(strumlist)):
                            strummed_note = strumlist[strum_index]
                            if strummed_note[1] == record_index:
                                strum_offset = strum_index/90.0
                                
                            
                            
                    
                        
                        
            for i in range(0, len(chorus_list)):
                sample          = chorus_list[i][0]
                offset          = chorus_list[i][1]
                instrument      = chorus_list[i][2]
                sample_tempo    = chorus_list[i][3]
                plucked         = chorus_list[i][4]
                search_level    = chorus_list[i][5]
                loudness_adjust = chorus_list[i][6]
                note_name       = notes[note]
                true_length     = chorus_list[i][7]
                pan_shift       = pan_segment_counter * pan_segment * 2
                pan_segment_counter += 1
                if instrument in ["viola", "cello", "violin", "double-bass"]:
                    offset-=string_offset/2
                ffmpeg_unit     = [sample, ontime-offset+strum_offset, sample_tempo, plucked, search_level, note_name, loudness_adjust, true_length, pan_shift]
                track.append(ffmpeg_unit)
                file1.write("echo play ../util/Philhatronia/samples/Philhartronia/"+instrument2+"/"+sample+" tempo "+str(sample_tempo)+"\n")
                file1.write("play ../util/Philhartronia/samples/Philhartronia/"+instrument2+"/"+sample+" tempo "+str(1.5)+nuller+" &\n")
                 
                file1.write("echo "+str(datetime.timedelta(seconds=ontime-offset))+" "+sample+"\n")
                
                file1.write("read test\n")
            file1.close()
            os.system("chmod +x diagnostics-logs/playlist."+instrument_original+".sh")
        
        for item in track:
            debug(instrument_original+"_track.txt", item)
        
        render(settings, track, instrument2, instrument_original)

        
    mixdown(settings)
    outpath = "project_outputs/"+settings["project_name"]+"/"
    final_filename =settings["input_midi"].split("/")[-1].split(".mid")[0]+".wav"
    length_of_final = get_sound_length(outpath+final_filename)
    print("total time taken for "+str(round(length_of_final))+" second long file was: "+str(round(time()-start))+ " seconds")
