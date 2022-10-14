#!/usr/bin/env pypy3

from util.arranger import arrange
from util.arranger import defaults

import os
import sys

os.system("clear")

# again this is another piano work simply extended into a quartet.

# midi file credit: ?
# samples provided by the London Philharmonia Orchestra

###############################
# Create settings dictionary. #
###############################
settings = defaults

settings["project_name"] = "Mozart-turkish-march"
settings["input_midi"]   = "MIDI/el-atril-midi/www.el-atril.com/midis/Mozart/Mozart_PianoSonatas/allaturk.mid"

# "violin", "viola", "cello", "double-bass", "bass-clarinet", "bassoon", "clarinet", "contrabassoon", "english-horn", "flute", "french-horn", "oboe", "saxophone", "trombone", "trumpet", "tuba", "guitar", "mandolin", "banjo"

settings["instruments"] = ["violin", "viola", "cello", "double-bass"]

settings["maximize_dynamics"]                   = True
settings["key_offset"]                          = -10
settings["reverberance"]                        = 50
settings["reverb_room_scale"]                   = 100
settings["reverb_stereo_depth"]                 = 100
# I slowed the tempo a little bit because my synth doesn't fair well with
# very fast notes. Well the violin at least sounds like of like an organ if it
# is too fast.
settings["master_tempo"]                        = 1.2
settings["master_volume"]                       = 0.8
settings["round_robin"]                         = 6
settings["expression_multiplier"]               = 1 # set this to a lower value to make get_sample

# these are practically simple default settings...
# if you don't specify a midi channel it just goes and uses all of them for
# an instrument
settings["violin"]["octave"]                = 0
settings["violin"]["length_upperlimit"]   = 999
settings["violin"]["length_lowerlimit"]   = 0
settings["violin"]["velocity_multiplier"] = 1.0
settings["violin"]["volume"]              = .5
settings["violin"]["polyphony"]           = 1
settings["violin"]["note_length_adjust"]  = 1.0
settings["violin"]["pizz_threshold"]      = .1 # I set this for another project
# for some reason it sounds fairly ok in this one..
#settings["violin"]["midi_channel"]        = 1

settings["viola"]["octave"]                = 0
settings["viola"]["length_upperlimit"]   = 999
settings["viola"]["length_lowerlimit"]   = 0
settings["viola"]["velocity_multiplier"] = 1.0
settings["viola"]["volume"]              = .5
settings["viola"]["polyphony"]           = 1
settings["viola"]["note_length_adjust"]  = 1.0
settings["viola"]["pizz_threshold"]      = .1
#settings["violin"]["midi_channel"]       = 1

settings["cello"]["octave"]              = 0
settings["cello"]["length_upperlimit"]   = 999
settings["cello"]["length_lowerlimit"]   = 0
settings["cello"]["velocity_multiplier"] = 1.0
settings["cello"]["volume"]              = .5
settings["cello"]["polyphony"]           = 1
settings["cello"]["note_length_adjust"]  = 1.0
settings["cello"]["pizz_threshold"]      = -1
#settings["violin"]["midi_channel"]       = 1

settings["double-bass"]["octave"]              = 0
settings["double-bass"]["length_upperlimit"]   = 999
settings["double-bass"]["length_lowerlimit"]   = 0
settings["double-bass"]["velocity_multiplier"] = 1.0
settings["double-bass"]["volume"]              = .5
settings["double-bass"]["polyphony"]           = 1
settings["double-bass"]["note_length_adjust"]  = 1.0
settings["double-bass"]["pizz_threshold"]      = -1
#settings["double-bass"]["midi_channel"]        = 1




arrange(settings)
