#!/usr/bin/env pypy3

from util.arranger import arrange
from util.arranger import defaults
import os
os.system("util/./banned-sample-translater.py")
import sys

os.system("clear")

# I made this file in 30 minutes just fiddling with the knobs
# This was orignally made for piano.

# midi file credit: the Lectern
# samples provided by the London Philharmonia Orchestra

###############################
# Create settings dictionary. #
###############################
settings = defaults

settings["project_name"] = "Chopin-Mazurka-en-F#-m-Op.6-Nº.1"
settings["input_midi"]   = "MIDI/el-atril-midi/chopin/Mazurka-en-F#-m-Op.6-Nº.1.mid"

settings["banned_effects"]                      = ["snap","battuto", "tremolo", "glissando"]
settings["effect_exceptions"]                   = []

# "violin", "viola", "cello", "double-bass", "bass-clarinet", "bassoon", "clarinet", "contrabassoon", "english-horn", "flute", "french-horn", "oboe", "saxophone", "trombone", "trumpet", "tuba", "guitar", "mandolin", "banjo"

settings["instruments"] = ["violin", "viola", "cello", "double-bass"]

settings["maximize_dynamics"]                   = False
settings["key_offset"]                          = 0
settings["reverberance"]                        = 50
settings["reverb_room_scale"]                   = 100
settings["reverb_stereo_depth"]                 = 100
settings["master_tempo"]                        = 1
settings["master_volume"]                       = 1.05
settings["round_robin"]                         = 1
settings["expression_multiplier"]               = 1


settings["violin"]["octave"]                = 0
settings["violin"]["length_upperlimit"]   = 999
settings["violin"]["length_lowerlimit"]   = 0
settings["violin"]["velocity_multiplier"] = .7
settings["violin"]["volume"]              = .5
settings["violin"]["polyphony"]           = 1
settings["violin"]["note_length_adjust"]  = 1.0
settings["violin"]["pizz_threshold"]      = .1
#settings["violin"]["midi_channel"]        = 1

settings["viola"]["octave"]                = 0
settings["viola"]["length_upperlimit"]   = 999
settings["viola"]["length_lowerlimit"]   = 0
settings["viola"]["velocity_multiplier"] = .7
settings["viola"]["volume"]              = .5
settings["viola"]["polyphony"]           = 1
settings["viola"]["note_length_adjust"]  = 1.0
settings["viola"]["pizz_threshold"]      = .1
#settings["violin"]["midi_channel"]       = 1

settings["cello"]["octave"]              = 0
settings["cello"]["length_upperlimit"]   = 999
settings["cello"]["length_lowerlimit"]   = 0
settings["cello"]["velocity_multiplier"] = .7
settings["cello"]["volume"]              = .35
settings["cello"]["polyphony"]           = 1
settings["cello"]["note_length_adjust"]  = 1.0
settings["cello"]["pizz_threshold"]      = -1
#settings["violin"]["midi_channel"]       = 1

settings["double-bass"]["octave"]              = 0
settings["double-bass"]["length_upperlimit"]   = 999
settings["double-bass"]["length_lowerlimit"]   = 0
settings["double-bass"]["velocity_multiplier"] = .7
settings["double-bass"]["volume"]              = .3
settings["double-bass"]["polyphony"]           = 1
settings["double-bass"]["note_length_adjust"]  = 1.0
settings["double-bass"]["pizz_threshold"]      = -1
#settings["double-bass"]["midi_channel"]        = 1




arrange(settings)
