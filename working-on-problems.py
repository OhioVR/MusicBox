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

settings["project_name"] = "working-on-problems"
settings["input_midi"]   = "MIDI/working-on-problems.mid"

settings["instruments"] = ["flute", "oboe", "saxophone", "clarinet", "english-horn", "trumpet", "french-horn", "bass-clarinet", "bassoon", "contrabassoon", "tuba" ]

settings["maximize_dynamics"]                   = False
settings["key_offset"]                          = -4
settings["reverberance"]                        = 50
settings["reverb_room_scale"]                   = 100
settings["reverb_stereo_depth"]                 = 100
settings["master_tempo"]                        = 1
settings["master_volume"]                       = 0.8
settings["global_velocity"]                     = 0.8
settings["round_robin"]                         = 0
settings["expression_multiplier"]               = 1 # set this to a lower value to make get_sample
settings["strings_overlay_time"]                = 0.07

settings["bass-clarinet"]["octave"]              = 1
settings["bass-clarinet"]["length_upperlimit"]   = 999
settings["bass-clarinet"]["length_lowerlimit"]   = 0
settings["bass-clarinet"]["velocity_multiplier"] = .8
settings["bass-clarinet"]["volume"]              = 1.2
settings["bass-clarinet"]["polyphony"]           = 1
settings["bass-clarinet"]["note_length_adjust"]  = 1.0

settings["flute"]["octave"]                = 1
settings["flute"]["length_upperlimit"]   = 999
settings["flute"]["length_lowerlimit"]   = 0
settings["flute"]["velocity_multiplier"] = .8
settings["flute"]["volume"]              = 2
settings["flute"]["polyphony"]           = 1
settings["flute"]["note_length_adjust"]  = 1.0

settings["bassoon"]["octave"]              = 1
settings["bassoon"]["length_upperlimit"]   = 999
settings["bassoon"]["length_lowerlimit"]   = 0
settings["bassoon"]["velocity_multiplier"] = .8
settings["bassoon"]["volume"]              = 2
settings["bassoon"]["polyphony"]           = 1
settings["bassoon"]["note_length_adjust"]  = 1.0

settings["trumpet"]["octave"]                = 0
settings["trumpet"]["length_upperlimit"]   = 999
settings["trumpet"]["length_lowerlimit"]   = 0
settings["trumpet"]["velocity_multiplier"] = .8
settings["trumpet"]["volume"]              = 1
settings["trumpet"]["polyphony"]           = 1
settings["trumpet"]["note_length_adjust"]  = 1.0

settings["french-horn"]["octave"]                = 0
settings["french-horn"]["length_upperlimit"]   = 999
settings["french-horn"]["length_lowerlimit"]   = 0
settings["french-horn"]["velocity_multiplier"] = .8
settings["french-horn"]["volume"]              = 1
settings["french-horn"]["polyphony"]           = 1
settings["french-horn"]["note_length_adjust"]  = 1.0

settings["oboe"]["octave"]                = 0
settings["oboe"]["length_upperlimit"]   = 999
settings["oboe"]["length_lowerlimit"]   = 0
settings["oboe"]["velocity_multiplier"] = 1.0
settings["oboe"]["volume"]              = 1.5
settings["oboe"]["polyphony"]           = 1
settings["oboe"]["note_length_adjust"]  = 1.0

settings["clarinet"]["octave"]              = 0
settings["clarinet"]["length_upperlimit"]   = 999
settings["clarinet"]["length_lowerlimit"]   = 0
settings["clarinet"]["velocity_multiplier"] = 1
settings["clarinet"]["volume"]              = 1
settings["clarinet"]["polyphony"]           = 1
settings["clarinet"]["note_length_adjust"]  = 1.0

settings["contrabassoon"]["octave"]              = -1
settings["contrabassoon"]["length_upperlimit"]   = 999
settings["contrabassoon"]["length_lowerlimit"]   = 0
settings["contrabassoon"]["velocity_multiplier"] = 1
settings["contrabassoon"]["volume"]              = .5
settings["contrabassoon"]["polyphony"]           = 1
settings["contrabassoon"]["note_length_adjust"]  = 1.0
settings["contrabassoon"]["high_pass"]           = 12*3

settings["tuba"]["octave"]              = -1
settings["tuba"]["length_upperlimit"]   = 999
settings["tuba"]["length_lowerlimit"]   = 0
settings["tuba"]["velocity_multiplier"] = 1
settings["tuba"]["volume"]              = .5
settings["tuba"]["polyphony"]           = 1
settings["tuba"]["note_length_adjust"]  = 1.0
settings["tuba"]["high_pass"]           = 12*3

settings["english-horn"]["octave"]              = 0
settings["english-horn"]["length_upperlimit"]   = 999
settings["english-horn"]["length_lowerlimit"]   = 0
settings["english-horn"]["velocity_multiplier"] = 1
settings["english-horn"]["volume"]              = .8
settings["english-horn"]["polyphony"]           = 1
settings["english-horn"]["note_length_adjust"]  = 1.0
settings["english-horn"]["high_pass"]           = 12*5




arrange(settings)
