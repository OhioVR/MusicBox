#!/usr/bin/env python3

# Scott's Music Box
# midi_file_to_playlist.py by Scott Yannitell
# Copyright 2022 Scott Yannitell all rights reserved

# midi_file_to_playlist.py takes note on and off times and translates them to
# a list of on times and lengths. It encounters different situations for midi
# files and tries to accommodate their peculiarities to get the correctly ordered
# and structured results. Midi files seem to handle note off events differently
# sometimes and this script tries to get it right depending on the situation.

# the purpose of the playlist generator is to get the time on, time while, the
# note is sounding and its intensity and number of partners. The program
# also records what channel was used.

# I used this fellows broken code to make this program work I hope he
# doesn't mind..
# https://github.com/mido/mido/issues/350
import sys
import os
import time
import mido
from mido import MidiFile, MetaMessage

# all units in seconds
def sec2milisecond(seconds):
    miliseconds_per_second = 1000 # 60 fps
    return seconds * miliseconds_per_second # Note: round(seconds * milisecondrate) gives inconsistencies of playback syncing with audio file


def process_midi(settings, backwards):
    preprocess = []
    # Load MIDI Data
    mid = MidiFile(settings["input_midi"])

    #print(mid)

    #print("TYPE: " + str(mid.type))
    #print("LENGTH: " + str(mid.length))
    #print("TICKS PER BEAT: " + str(mid.ticks_per_beat))

    # Assign Tracks to different channels before merging to know the message origin
    for k in range(len(mid.tracks)):
        for msg in mid.tracks[k]:
            if not msg.is_meta and msg.type in ['note_on', 'note_off']:
                
                try:
                    msg.channel = k
                except:
                    msg.channel = 1

    # Merge tracks
    all_tracks = mido.merge_tracks(mid.tracks)

    current_time = 0
    # we can't have negative offsets with the rendering engine
    # so it is necessary to start the playlist with a delay
    delay = 5.0

    # Get tempo
    def get_tempo(mid):
        for k in range(len(mid.tracks)):
            for msg in mid.tracks[k]:
                if msg.is_meta:
                    if msg.type == 'set_tempo':
                        return msg.tempo
        return 50000

    tempo = get_tempo(mid)
    if backwards:
        all_tracks.reverse()
        for msg_index in range(0,len(all_tracks)):
            if all_tracks[msg_index].is_meta:
                if all_tracks[msg_index].type == 'set_tempo':
                    tempo = all_tracks[msg_index].tempo
            current_time += mido.tick2second(all_tracks[msg_index].time, mid.ticks_per_beat, tempo)
            if not all_tracks[msg_index].is_meta:
                if all_tracks[msg_index].type in ['note_on', 'note_off']:
                    try:
                        midi_channel = msg.channel
                    except:
                        midi_channel = 1
                    midiNote = all_tracks[msg_index].note
                    noteType = all_tracks[msg_index].type
                    noteVelocity = all_tracks[msg_index].velocity
                    noteTempo = mido.tempo2bpm(tempo)
                    if str(noteType) == 'note_off' or ( str(noteType) == 'note_on' and noteVelocity == 0) :
                        for search_index in range(0,msg_index):
                            if all_tracks[search_index].type in ['note_on', 'note_off']:
                                if all_tracks[search_index].note == midiNote and all_tracks[search_index].type == "note_on":
                                    seconds = ( current_time + delay ) - 1
                                    preprocess.append([midi_channel,midiNote,noteType,noteVelocity,noteTempo,seconds])
                                    break 
                                
    else:
        for msg in all_tracks:
            if msg.is_meta:
                if msg.type == 'set_tempo':
                    tempo = msg.tempo
            current_time += mido.tick2second(msg.time, mid.ticks_per_beat, tempo)
            if not msg.is_meta:
                if msg.type in ['note_on', 'note_off']:
                    try:
                        midi_channel = msg.channel
                    except:
                        midi_channel = 1
                    midiNote = msg.note
                    noteType = msg.type
                    noteVelocity = msg.velocity
                    noteTempo = mido.tempo2bpm(tempo)
                    if str(noteType) == 'note_on' and noteVelocity != 0:
                        seconds = (current_time + delay ) - 1 
                    if str(noteType) == 'note_off' or (str(noteType) == 'note_on' and noteVelocity == 0):
                        seconds = ( current_time + delay ) - 1 
                    preprocess.append([midi_channel,midiNote,noteType,noteVelocity,noteTempo,seconds])
    return preprocess 
                
def create_playlist_on_or_off(preprocess,settings):
    playlist = []
    ontime = -1
    offtime = -1
    search_note = -1
    for entity_num in range(0, len(preprocess)):
        if preprocess[entity_num][2] == "note_on":
            ontime      = preprocess[entity_num][5]
            search_note = preprocess[entity_num][1]
            velocity    = preprocess[entity_num][3]
            midi_channel = preprocess[entity_num][0]
            for i in range(entity_num+1,len(preprocess)):
                if preprocess[i][2] == "note_off" and preprocess[i][1] == search_note:
                    offtime = preprocess[i][5]
                    length  = offtime - ontime
                    playlist.append([midi_channel, search_note, ontime/settings["master_tempo"], length/settings["master_tempo"], velocity])
                    break
                    
    return playlist


def create_playlist_on_only(preprocess,settings):
    playlist = []
    ontime = -1
    offtime = -1
    search_note = -1
    offlist = []
    for entity_num in range(0, len(preprocess)):
        if preprocess[entity_num][2] == "note_on":
            ontime      = preprocess[entity_num][5]
            search_note = preprocess[entity_num][1]
            velocity    = preprocess[entity_num][3]
            midi_channel = preprocess[entity_num][0]
            if velocity > 0:
                for i in range(entity_num+1,len(preprocess)):
                    if preprocess[i][1] == search_note and preprocess[i][3] == 0 and i not in offlist:
                        offlist.append(i)
                        offtime = preprocess[i][5]
                        length  = offtime - ontime
                        playlist.append([midi_channel, search_note, ontime/settings["master_tempo"], length/settings["master_tempo"], velocity])
                        break
    return playlist
    
    


def get_polyphony_info(playlist):
    for sound_index in range(0, len(playlist)):
        ontime = playlist[sound_index][2]
        time_polyphony = 1
        for i in range (sound_index+1, len(playlist)):
            if playlist[i][2] == ontime:
                time_polyphony+=1
        playlist[sound_index].append(time_polyphony)
    return playlist

def get_ranged_velocity(target_8bit, min_8bit, max_8bit):
    range_loud   = max_8bit - min_8bit
    if range_loud == 0: return min_8bit
    ranger_ratio = (128.0) / range_loud
    adjusted_loud = (target_8bit * ranger_ratio) - (ranger_ratio * min_8bit)
    if adjusted_loud > 128: adjusted_loud = 128
    if adjusted_loud == 0 : adjusted_loud = 1
    
    return adjusted_loud# round(adjusted_loud)
    
    
# this is activated by arranger if for some reason you wish
# to normalize all the intensities. Though you probably will never do that.
def maximize_dynamics(playlist):
    lowest_dynamic  = 999
    highest_dynamic = -1
    for sound_index in range(0, len(playlist)):
        velocity = playlist[sound_index][4]
        if velocity < lowest_dynamic:
            lowest_dynamic = velocity
        if velocity > highest_dynamic:
            highest_dynamic = velocity
    
    for sound_index in range(0, len(playlist)):
        old_velocity = playlist[sound_index][4]
        new_velocity = get_ranged_velocity(playlist[sound_index][4],lowest_dynamic, highest_dynamic)
        #print("old_velocity", old_velocity, "new_velocity", new_velocity, "lowest", lowest_dynamic, "highest", highest_dynamic)
        playlist[sound_index][4] = new_velocity
    return playlist

# call this from your composition script to generate 
# the music time continum data for use in your compositing script
def generate_playlist(settings):
    try:
        backwards = settings["backwards"]
    except:
        backwards = False
   


    preprocess = process_midi(settings, backwards)
    print("atttempting midi parse with method 1 (on and off)")
    playlist = create_playlist_on_or_off(preprocess,settings)
    
    if len(playlist) == 0:
        print("atttempting midi parse with method 2 (on only)")
        playlist = create_playlist_on_only(preprocess,settings)
    playlist = get_polyphony_info(playlist)
    
    if settings["maximize_dynamics"] == True:
        playlist = maximize_dynamics(playlist)

    return playlist
