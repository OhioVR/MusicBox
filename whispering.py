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

settings["project_name"] = "whispering"
settings["input_midi"]   = "MIDI/musescore.com/Whispering_piano_roll_transcription-scott-modified.mid"



# "violin", "viola", "cello", "double-bass", "bass-clarinet", "bassoon", "clarinet", "contrabassoon", "english-horn", "flute", "french-horn", "oboe", "saxophone", "trombone", "trumpet", "tuba", "guitar", "mandolin", "banjo"

settings["instruments"] = ["flute", "clarinet", "violin", "viola", "trombone", "cello", "double-bass", "tuba"]

settings["maximize_dynamics"]                   = False
settings["key_offset"]                          = 0
settings["reverberance"]                        = 50
settings["reverb-room-scale"]                   = 100
settings["reverb-stereo-depth"]                 = 100
settings["master_tempo"]                        = 1.0
settings["master_volume"]                       = 0.8
settings["round_robin"]                         = 1
settings["expression_multiplier"]               = 1
settings["violin"]["octave"]                = 0
settings["violin"]["length_upperlimit"]   = 999
settings["violin"]["length_lowerlimit"]   = 0
settings["violin"]["velocity_multiplier"] = 1.0
settings["violin"]["volume"]              = .5 
settings["violin"]["polyphony"]           = 1
settings["violin"]["note_length_adjust"]  = 1.0
settings["violin"]["pizz-threshold"]      = -1
settings["violin"]["low_pass"]            = 12*4
settings["violin"]["high_pass"]           = 12*8

settings["flute"]["octave"]                = 1
settings["flute"]["length_upperlimit"]   = 999
settings["flute"]["length_lowerlimit"]   = 0
settings["flute"]["velocity_multiplier"] = 1.0
settings["flute"]["volume"]              = .5
settings["flute"]["polyphony"]           = 1
settings["flute"]["note_length_adjust"]  = 1.0
settings["flute"]["pizz-threshold"]      = -1
settings["flute"]["low_pass"]            = 12*5
settings["flute"]["high_pass"]           = 12*8

settings["clarinet"]["octave"]                = 0
settings["clarinet"]["length_upperlimit"]   = .3
settings["clarinet"]["length_lowerlimit"]   = 0
settings["clarinet"]["velocity_multiplier"] = 1.0
settings["clarinet"]["volume"]              = .5 
settings["clarinet"]["polyphony"]           = 1
settings["clarinet"]["note_length_adjust"]  = 1.0
settings["clarinet"]["pizz-threshold"]      = -1
settings["clarinet"]["low_pass"]            = 12*4
settings["clarinet"]["high_pass"]           = 12*6

settings["viola"]["octave"]                = 0
settings["viola"]["length_upperlimit"]   = 999
settings["viola"]["length_lowerlimit"]   = 0
settings["viola"]["velocity_multiplier"] = 1.0
settings["viola"]["volume"]              = .5 / 8
settings["viola"]["polyphony"]           = 1
settings["viola"]["note_length_adjust"]  = 1.0
settings["viola"]["pizz-threshold"]      = -1
settings["viola"]["low_pass"]            = 12*3
settings["viola"]["high_pass"]           = 12*5

settings["cello"]["octave"]              = 0
settings["cello"]["length_upperlimit"]   = 999
settings["cello"]["length_lowerlimit"]   = 0
settings["cello"]["velocity_multiplier"] = 1.0
settings["cello"]["volume"]              = .5 
settings["cello"]["polyphony"]           = 1
settings["cello"]["note_length_adjust"]  = 1.0
settings["cello"]["pizz-threshold"]      = -1
settings["cello"]["low_pass"]            = 12*3
settings["cello"]["high_pass"]           = 12*5

settings["double-bass"]["octave"]              = 0
settings["double-bass"]["length_upperlimit"]   = 999
settings["double-bass"]["length_lowerlimit"]   = 0
settings["double-bass"]["velocity_multiplier"] = 1.0
settings["double-bass"]["volume"]              = .5 
settings["double-bass"]["polyphony"]           = 1
settings["double-bass"]["note_length_adjust"]  = 1.0
settings["double-bass"]["pizz-threshold"]      = -1

settings["tuba"]["octave"]              = 0
settings["tuba"]["length_upperlimit"]   = 999
settings["tuba"]["length_lowerlimit"]   = 0
settings["tuba"]["velocity_multiplier"] = 1.0
settings["tuba"]["volume"]              = .5
settings["tuba"]["polyphony"]           = 1
settings["tuba"]["note_length_adjust"]  = 1.0
settings["tuba"]["pizz-threshold"]      = -1
settings["tuba"]["low_pass"]            = 0


settings["trombone"]["octave"]              = 0
settings["trombone"]["length_upperlimit"]   = 999
settings["trombone"]["length_lowerlimit"]   = 0
settings["trombone"]["velocity_multiplier"] = 1.0
settings["trombone"]["volume"]              = .5 
settings["trombone"]["polyphony"]           = 1
settings["trombone"]["note_length_adjust"]  = 1.0
settings["trombone"]["pizz-threshold"]      = -1
settings["trombone"]["low_pass"]            = 0
settings["trombone"]["high_pass"]           = 12*6



arrange(settings)
