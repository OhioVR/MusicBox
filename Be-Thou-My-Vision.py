#!/usr/bin/env pypy3

from util.arranger import arrange
from util.arranger import defaults
import os
import sys

os.system("clear")


###############################
# Create settings dictionary. #
###############################
settings = defaults


settings["project_name"] = "Be-Thou-My-Vision"
settings["input_midi"]   = "MIDI/example_midi_files/be-now-thy-vision-performer-unknown-fruity.mid"
settings["key_offset"]   = 0
settings["instruments"]  = ["flute", "violin", "oboe", "banjo", "viola","trombone", "french-horn","english-horn", "double-bass"]
settings["banned_effects"] = ["tremolo", "battuto", "glissando", "arco-tremolo", "trill"]
settings["strings_offset"] = 0.07
settings["flute"]["velocity-multiplier"] = 1.5
settings["strings_overlay_time"]          = 0.07
settings["cello"]["midi_channel"]         = 1+1
settings["violin"]["midi_channel"]        = 1+1
settings["viola"]["midi_channel"]         = 1+1
settings["double-bass"]["midi_channel"]   = 1+1
settings["violin"]["octave"]              = 0
settings["viola"]["octave"]               = 0
settings["cello"]["octave"]               = 0
settings["double-bass"]["pizz_threshold"] = 999
#settings["cello"]["volume"]              = 0.5
#settings["viola"]["volume"]              = 0.5
#settings["violin"]["volume"]             = 1.0
#settings["double-bass"]["volume"]        = 0.3



settings["banjo"]["midi_channel"]         = 6 + 1
settings["banjo"]["octave"]               = 0

settings["trombone"]["midi_channel"]       = 3+1
settings["trombone"]["octave"]             = -1
settings["trombone"]["velocity_multiplier"] = 2

settings["french-horn"]["midi_channel"]        = 3+1
settings["french-horn"]["octave"]              = -1
settings["french-horn"]["velocity_multiplier"] = 2
#settings["violin"]["velocity_multiplier"]      = .3
#settings["viola"]["velocity_multiplier"]       = .3
#settings["cello"]["velocity_multiplier"]       = .3
#settings["double-bass"]["velocity_multiplier"] = .5

settings["english-horn"]["midi_channel"]       = 3 + 1 
settings["english-horn"]["octave"]             = -1
#settings["english-horn"]["volume"]             = .7
settings["english-horn"]["velocity_multiplier"] = 2

settings["oboe"]["midi_channel"]          = 4 + 1
settings["mandolin"]["midi_channel"]      = 5 + 1
settings["mandolin"]["pizz-threshold"]    = 1.4
settings["guitar"]["midi_channel"]        = 6 + 1


#settings["violin"]["shorts-max"]          = 0.125+0.2
#settings["violin"]["shorts-factor"]       = 4

#settings["viola"]["shorts-max"]          = 0.125+0.2
#settings["viola"]["shorts-factor"]       = 4

settings["flute"]["midi_channel"]         = 8 + 1



arrange(settings)
