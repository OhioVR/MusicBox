#!/usr/bin/env pypy3

from util.arranger import arrange
from util.arranger import defaults
import os
import sys

os.system("clear")


# midi file credit: ?
# samples provided by the London Philharmonia Orchestra

###############################
# Create settings dictionary. #
###############################
settings = defaults

settings["project_name"] = "Bad-Year-In-Egypt"
settings["input_midi"]   = "MIDI/bad-year-in-egypt.mid"

# "violin", "viola", "cello", "double-bass", "bass-clarinet", "bassoon", "clarinet", "contrabassoon", "english-horn", "flute", "french-horn", "oboe", "saxophone", "trombone", "trumpet", "tuba", "guitar", "mandolin", "banjo"

settings["instruments"] = ["violin", "viola", "cello", "double-bass"]

settings["maximize_dynamics"]                   = False
settings["key_offset"]                          = 0
settings["reverberance"]                        = 50
settings["reverb_room_scale"]                   = 100
settings["reverb_stereo_depth"]                 = 100
settings["master_tempo"]                        = 1.0
settings["master_volume"]                       = 0.8
settings["round_robin"]                         = 0
settings["expression_multiplier"]               = 1 # set this to a lower value to make get_sample


settings["violin"]["octave"]                = 0
settings["violin"]["length_upperlimit"]   = 999
settings["violin"]["length_lowerlimit"]   = 0
settings["violin"]["velocity_multiplier"] = 1.0
settings["violin"]["volume"]              = .5
settings["violin"]["polyphony"]           = 1
settings["violin"]["note_length_adjust"]  = 1.0
settings["violin"]["pizz_threshold"]      = .2
#settings["violin"]["midi_channel"]        = 1

settings["viola"]["octave"]                = 0
settings["viola"]["length_upperlimit"]   = 999
settings["viola"]["length_lowerlimit"]   = 0
settings["viola"]["velocity_multiplier"] = 1.0
settings["viola"]["volume"]              = .5
settings["viola"]["polyphony"]           = 1
settings["viola"]["note_length_adjust"]  = 1.0
settings["viola"]["pizz_threshold"]      = .2
#settings["viola"]["midi_channel"]       = 1

settings["cello"]["octave"]              = -1
settings["cello"]["length_upperlimit"]   = 999
settings["cello"]["length_lowerlimit"]   = 0
settings["cello"]["velocity_multiplier"] = 1.0
settings["cello"]["volume"]              = .5
settings["cello"]["polyphony"]           = 1
settings["cello"]["note_length_adjust"]  = 1.0
settings["cello"]["pizz_threshold"]      = .2
#settings["cello"]["midi_channel"]       = 1

settings["double-bass"]["octave"]              = 0
settings["double-bass"]["length_upperlimit"]   = 999
settings["double-bass"]["length_lowerlimit"]   = 0
settings["double-bass"]["velocity_multiplier"] = 1.0
settings["double-bass"]["volume"]              = .5
settings["double-bass"]["polyphony"]           = 1
settings["double-bass"]["note_length_adjust"]  = 1.0
settings["double-bass"]["pizz_threshold"]      = .2
#settings["double-bass"]["midi_channel"]        = 1




arrange(settings)
